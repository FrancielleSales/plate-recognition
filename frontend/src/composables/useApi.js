import { inject, ref } from "vue";

const useApi = () => {
  const axiosInstance = inject("axios");

  const get = async (url, params = null) => {
    try {
      const response = await axiosInstance.get(url, { params });

      if (response.data) return response.data;

      return "";
    } catch (error) {
      throw error;
    }
  };

  const post = async (url, data) => {
    try {
      const response = await axiosInstance.post(url, data);
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  const put = async (url, data) => {
    try {
      const response = await axiosInstance.put(url, data);
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  const remove = async (url, params) => {
    try {
      const response = await axiosInstance.delete(url, { params });
      return response.data;
    } catch (error) {
      throw error;
    }
  };

  return {
    get,
    post,
    put,
    remove,
  };
};

export default useApi;
