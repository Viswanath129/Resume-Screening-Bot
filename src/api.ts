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

export const uploadFiles = async (files: FileList) => {
    try {
        const formData = new FormData();
        Array.from(files).forEach((file) => {
            formData.append("files", file);
        });

        const response = await axios.post(`${API_URL}/upload`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        return response.data;
    } catch (error) {
        console.error("Error uploading files:", error);
        throw error;
    }
};

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
