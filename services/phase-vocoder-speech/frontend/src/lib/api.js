import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const api = axios.create({
    baseURL: API_URL,
});

export const uploadAudio = async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await api.post('/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const processAudio = async (fileId, effect, params) => {
    // Pass params as a JSON object inside the request body (FastAPI expects a ProcessRequest)
    // Wait, in main.py I defined /process-json
    const response = await api.post('/process-json', {
        file_id: fileId,
        effect: effect,
        params: params
    });
    return response.data;
};

export const getEffects = async () => {
    const response = await api.get('/effects');
    return response.data.effects;
};
