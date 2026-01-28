import React, { useState, useRef } from 'react';
import {
  Upload, FileText, BarChart2, CheckCircle, AlertCircle,
  RefreshCw, Briefcase, User, Plus, X, ChevronDown, ChevronUp, Search
} from 'lucide-react';
import { analyzeResumes, type ResumeData } from './api';

export default function App() {
  const [jobDescription, setJobDescription] = useState("Software Engineer\n\nWe are looking for a Python developer with experience in FastAPI and Machine Learning. Must know SQL and React.");

  const [resumes, setResumes] = useState<ResumeData[]>([
    {
      id: 1,
      name: "Ramesh",
      text: "Experienced Python developer with a background in Flask and Django. Familiar with SQL and basic ML concepts.",
      score: 0,
      matches: [],
      missing: []
    },
    {
      id: 2,
      name: "Swathi",
      text: "Project Manager with 5 years experience in Agile and Scrum. Good communication skills.",
      score: 0,
      matches: [],
      missing: []
    },
    {
      id: 3,
      name: "Lokesh",
      text: "Senior Software Engineer expert in FastAPI, React, and Machine Learning pipelines. SQL wizard.",
      score: 0,
      matches: [],
      missing: []
    }
  ]);

  const [isProcessing, setIsProcessing] = useState(false);
  const [activeTab, setActiveTab] = useState<'input' | 'results'>('input');
  const [expandedResumeId, setExpandedResumeId] = useState<number | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // --- Logic: Analysis & Scoring ---

  const analyzeData = async () => {
    setIsProcessing(true);
    try {
      // Call the backend API
      const rankedResumes = await analyzeResumes(jobDescription, resumes);
      setResumes(rankedResumes);
      setActiveTab('results');
    } catch (error) {
      console.error("Analysis failed:", error);
      alert("Analysis failed. Please check if the backend server is running.");
    } finally {
      setIsProcessing(false);
    }
  };

  // --- Logic: Resume Management ---

  const handleAddResume = () => {
    const newId = Math.max(...resumes.map(r => r.id), 0) + 1;
    setResumes([...resumes, {
      id: newId,
      name: `Candidate ${newId}`,
      text: "",
      score: 0,
      matches: [],
      missing: []
    }]);
  };

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (!files) return;

    Array.from(files).forEach(file => {
      const reader = new FileReader();
      reader.onload = (e) => {
        const text = e.target?.result as string;
        const newId = Math.max(...resumes.map(r => r.id), 0) + Math.floor(Math.random() * 1000);
        setResumes(prev => [...prev, {
          id: newId,
          name: file.name.replace(/\.[^/.]+$/, ""), // Remove extension
          text: text,
          score: 0,
          matches: [],
          missing: []
        }]);
      };
      reader.readAsText(file);
    });
  };

  const updateResume = (id: number, field: keyof ResumeData, value: string) => {
    setResumes(resumes.map(r => r.id === id ? { ...r, [field]: value } : r));
  };

  const deleteResume = (id: number) => {
    setResumes(resumes.filter(r => r.id !== id));
  };

  const toggleExpand = (id: number) => {
    setExpandedResumeId(expandedResumeId === id ? null : id);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans selection:bg-indigo-500 selection:text-white">
      {/* Header */}
      <header className="bg-slate-900 border-b border-slate-800 p-6 sticky top-0 z-50">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-br from-indigo-500 to-purple-600 p-2.5 rounded-xl shadow-lg shadow-indigo-500/20">
              <FileText className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">
                ResumeAI
              </h1>
              <p className="text-slate-500 text-xs font-medium tracking-wide uppercase">Smart Screening System</p>
            </div>
          </div>

          <div className="flex gap-2">
            <button
              onClick={() => setActiveTab('input')}
              className={`px-4 py-2 text-sm font-medium rounded-lg transition-all ${activeTab === 'input' ? 'bg-slate-800 text-white shadow-inner' : 'text-slate-400 hover:text-white'}`}
            >
              Data Input
            </button>
            <button
              onClick={() => setActiveTab('results')}
              className={`px-4 py-2 text-sm font-medium rounded-lg transition-all ${activeTab === 'results' ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-600/20' : 'text-slate-400 hover:text-white'}`}
            >
              Results
            </button>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto p-6 pb-32">

        {activeTab === 'input' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 animate-in fade-in slide-in-from-bottom-4 duration-500">

            {/* Left: Job Description */}
            <div className="lg:col-span-5 space-y-4">
              <div className="flex items-center gap-2 text-indigo-400 font-semibold mb-2">
                <Briefcase className="w-5 h-5" />
                <h2>Target Job Description</h2>
              </div>
              <div className="bg-slate-900/50 p-1 rounded-2xl ring-1 ring-slate-800 focus-within:ring-indigo-500 transition-all shadow-xl">
                <textarea
                  value={jobDescription}
                  onChange={(e) => setJobDescription(e.target.value)}
                  className="w-full h-[600px] bg-slate-900 p-6 rounded-xl outline-none text-slate-300 resize-none placeholder:text-slate-600 leading-relaxed scrollbar-thin scrollbar-thumb-slate-700"
                  placeholder="Paste the job description here (JD)..."
                />
              </div>
            </div>

            {/* Right: Resumes */}
            <div className="lg:col-span-7 space-y-4">
              <div className="flex items-center justify-between text-purple-400 font-semibold mb-2">
                <div className="flex items-center gap-2">
                  <User className="w-5 h-5" />
                  <h2>Candidate Pool ({resumes.length})</h2>
                </div>
                <div className="flex gap-2">
                  <input
                    type="file"
                    ref={fileInputRef}
                    onChange={handleFileUpload}
                    className="hidden"
                    accept=".txt"
                    multiple
                  />
                  <button
                    onClick={() => fileInputRef.current?.click()}
                    className="flex items-center gap-2 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 px-4 py-2 rounded-lg transition-colors border border-slate-700"
                  >
                    <Upload className="w-3 h-3" />
                    Upload .txt
                  </button>
                  <button
                    onClick={handleAddResume}
                    className="flex items-center gap-2 text-xs bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2 rounded-lg transition-colors shadow-lg shadow-indigo-600/20"
                  >
                    <Plus className="w-3 h-3" />
                    Add Manual
                  </button>
                </div>
              </div>

              <div className="h-[600px] overflow-y-auto pr-2 space-y-4 scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-transparent">
                {resumes.map((resume) => (
                  <div key={resume.id} className="bg-slate-900 p-5 rounded-xl border border-slate-800 hover:border-slate-700 transition-all group shadow-sm">
                    <div className="flex justify-between items-start mb-3">
                      <div className="flex-1 mr-4">
                        <label className="text-xs text-slate-500 uppercase font-bold tracking-wider mb-1 block">Candidate Name</label>
                        <input
                          type="text"
                          value={resume.name}
                          onChange={(e) => updateResume(resume.id, 'name', e.target.value)}
                          className="bg-transparent font-medium text-lg text-white outline-none w-full placeholder:text-slate-600"
                          placeholder="Candidate Name"
                        />
                      </div>
                      <button
                        onClick={() => deleteResume(resume.id)}
                        className="text-slate-600 hover:text-red-400 p-2 hover:bg-red-400/10 rounded-lg transition-colors"
                        title="Remove Candidate"
                      >
                        <X className="w-4 h-4" />
                      </button>
                    </div>
                    <div className="relative">
                      <textarea
                        value={resume.text}
                        onChange={(e) => updateResume(resume.id, 'text', e.target.value)}
                        className="w-full h-24 bg-slate-950 p-3 rounded-lg text-sm text-slate-400 outline-none resize-none border border-slate-800 focus:border-indigo-500/50 transition-colors"
                        placeholder="Paste resume text content here..."
                      />
                    </div>
                  </div>
                ))}

                {resumes.length === 0 && (
                  <div className="h-full flex flex-col items-center justify-center text-slate-600 border-2 border-dashed border-slate-800 rounded-xl">
                    <Upload className="w-12 h-12 mb-4 opacity-50" />
                    <p>No candidates added yet</p>
                    <p className="text-sm opacity-50">Upload .txt files or add manually</p>
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {activeTab === 'results' && (
          <div className="max-w-4xl mx-auto animate-in fade-in zoom-in-95 duration-500">
            <div className="bg-slate-900 rounded-3xl p-1 border border-slate-800 shadow-2xl">
              <div className="p-8 pb-4">
                <h2 className="text-2xl font-bold text-white mb-2 flex items-center gap-3">
                  <BarChart2 className="w-7 h-7 text-indigo-500" />
                  Analysis Report
                </h2>
                <p className="text-slate-400">Ranked based on keyword relevance and semantic similarity to the Job Description.</p>
              </div>

              <div className="space-y-2 p-4">
                {resumes.map((resume, index) => {
                  const isExpanded = expandedResumeId === resume.id;
                  const isTopMatch = index === 0 && resume.score > 50;

                  return (
                    <div key={resume.id} className={`transition-all duration-300 rounded-2xl overflow-hidden border ${isExpanded ? 'bg-slate-800/50 border-indigo-500/30' : 'bg-slate-950/50 border-slate-800 hover:border-slate-700'}`}>
                      {/* Summary Row */}
                      <div
                        onClick={() => toggleExpand(resume.id)}
                        className="p-4 flex items-center gap-6 cursor-pointer group"
                      >
                        <div className={`flex items-center justify-center w-12 h-12 rounded-full font-bold text-lg shrink-0 ${isTopMatch ? 'bg-indigo-500 text-white shadow-lg shadow-indigo-500/40' : 'bg-slate-800 text-slate-400'}`}>
                          #{index + 1}
                        </div>

                        <div className="flex-1 min-w-0">
                          <h3 className="font-semibold text-lg text-slate-200 group-hover:text-white transition-colors flex items-center gap-2">
                            {resume.name}
                            {isTopMatch && <CheckCircle className="w-4 h-4 text-indigo-400" />}
                          </h3>
                          <p className="text-slate-500 text-sm truncate">{resume.text.substring(0, 80)}...</p>
                        </div>

                        <div className="text-right shrink-0 flex items-center gap-6">
                          <div>
                            <div className={`text-2xl font-bold ${resume.score > 70 ? 'text-emerald-400' : resume.score > 40 ? 'text-indigo-400' : 'text-slate-400'}`}>
                              {resume.score}%
                            </div>
                            <span className="text-[10px] text-slate-500 uppercase tracking-wider font-bold">Match Rate</span>
                          </div>
                          {isExpanded ? <ChevronUp className="w-5 h-5 text-indigo-400" /> : <ChevronDown className="w-5 h-5 text-slate-600" />}
                        </div>
                      </div>

                      {/* Expanded Details */}
                      {isExpanded && (
                        <div className="px-20 pb-8 pt-2 animate-in slide-in-from-top-2">
                          <div className="grid grid-cols-2 gap-8 pt-4 border-t border-slate-700/50">

                            {/* Matches */}
                            <div>
                              <div className="flex items-center gap-2 text-emerald-400 font-semibold mb-3 text-sm uppercase tracking-wide">
                                <CheckCircle className="w-4 h-4" />
                                Matched Keywords
                              </div>
                              <div className="flex flex-wrap gap-2">
                                {resume.matches.length > 0 ? (
                                  resume.matches.map((word, i) => (
                                    <span key={i} className="px-2.5 py-1 rounded-md bg-emerald-500/10 text-emerald-400 text-xs border border-emerald-500/20 capitalize">
                                      {word}
                                    </span>
                                  ))
                                ) : (
                                  <span className="text-slate-500 text-sm italic">No direct keyword matches found.</span>
                                )}
                              </div>
                            </div>

                            {/* Missing */}
                            <div>
                              <div className="flex items-center gap-2 text-rose-400 font-semibold mb-3 text-sm uppercase tracking-wide">
                                <AlertCircle className="w-4 h-4" />
                                Missing Keywords
                              </div>
                              <div className="flex flex-wrap gap-2">
                                {resume.missing.length > 0 ? (
                                  resume.missing.slice(0, 15).map((word, i) => (
                                    <span key={i} className="px-2.5 py-1 rounded-md bg-rose-500/10 text-rose-400 text-xs border border-rose-500/20 capitalize opacity-75">
                                      {word}
                                    </span>
                                  ))
                                ) : (
                                  <span className="text-slate-500 text-sm italic">Great match! No major keywords missing.</span>
                                )}
                                {resume.missing.length > 15 && (
                                  <span className="px-2.5 py-1 text-slate-500 text-xs">+{resume.missing.length - 15} more</span>
                                )}
                              </div>
                            </div>

                          </div>

                          <div className="mt-6 pt-4 border-t border-slate-700/50">
                            <p className="text-slate-400 text-sm">
                              <span className="text-slate-200 font-semibold">HR Summary:</span> This candidate matches <span className="text-white">{resume.matches.length}</span> critical keywords from the job description.
                              {resume.score > 60
                                ? " Strong potential based on technical stack alignment."
                                : " Consider checking for transferable skills not explicitly listed."}
                            </p>
                          </div>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* Floating Action Button */}
        <div className="fixed bottom-10 left-1/2 -translate-x-1/2 z-50">
          <button
            onClick={analyzeData}
            disabled={isProcessing}
            className={`
              group relative flex items-center gap-3 px-8 py-4 rounded-full font-bold text-lg shadow-2xl transition-all hover:scale-105 active:scale-95
              ${isProcessing
                ? 'bg-slate-800 text-slate-400 cursor-wait ring-1 ring-slate-700'
                : 'bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-indigo-500/30 hover:shadow-indigo-500/50'}
            `}
          >
            {isProcessing ? (
              <>
                <RefreshCw className="w-5 h-5 animate-spin" />
                <span>Processing...</span>
              </>
            ) : (
              <>
                <div className="absolute inset-0 rounded-full bg-white/20 group-hover:animate-pulse"></div>
                <Search className="w-5 h-5 fill-current" />
                <span>Analyze Candidates</span>
              </>
            )}
          </button>
        </div>

      </main>
    </div>
  );
}
