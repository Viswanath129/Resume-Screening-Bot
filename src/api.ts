import axios from 'axios';

const API_URL = 'http://localhost:8000';

export interface ResumeData {
    id: number;
    name: string;
    text: string;
    score: number;
    matches: string[];
    missing: string[];
}

export const analyzeResumes = async (jobDescription: string, resumes: ResumeData[]) => {
    try {
        const response = await axios.post(`${API_URL}/analyze`, {
            job_description: jobDescription,
            resumes: resumes
        });
        return response.data.ranked_resumes;
    } catch (error) {
        console.error("Error analyzing resumes:", error);
        throw error;
    }
};
