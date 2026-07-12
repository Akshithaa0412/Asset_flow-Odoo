import api from "./api";

export const getAssetStatus = async () => {
    const response = await api.get("/reports/asset-status");
    return response.data;
};