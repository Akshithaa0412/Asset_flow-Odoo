import api from "./api";

export const getAssets = async () => {
    const response = await api.get("/assets/");
    return response.data;
};

export const createAsset = async (asset: any) => {
    const response = await api.post("/assets/", asset);
    return response.data;
};

export const updateAsset = async (id: string, asset: any) => {
    const response = await api.put(`/assets/${id}`, asset);
    return response.data;
};

export const deleteAsset = async (id: string) => {
    const response = await api.delete(`/assets/${id}`);
    return response.data;
};