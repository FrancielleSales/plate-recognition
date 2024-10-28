import { inject, ref } from "vue";

const useApi = () => {
  const axiosInstance = inject("axios");
  const DEFAULT_MESSAGE =
    "Ocorreu um erro interno. Tente novamente mais tarde.";
  const error = ref(DEFAULT_MESSAGE);

  const handleError = (error) => {
    error.value = error.response
      ? error.response.data.error.message
      : DEFAULT_MESSAGE;

    console.log(error.value);
  };

  const defaultError = () => {
    error.value = DEFAULT_MESSAGE;
  };

  const get = async (url, params = null) => {
    defaultError();
    try {
      const response = await axiosInstance.get(url, { params });

      if (response.data.data) return response.data.data;

      return "";
    } catch (error) {
      handleError(error);
      throw error;
    }
  };

  const post = async (url, data) => {
    defaultError();
    try {
      const response = await axiosInstance.post(url, data);
      return response.data;
    } catch (error) {
      handleError(error);
      throw error;
    }
  };

  const put = async (url, data) => {
    defaultError();
    try {
      const response = await axiosInstance.put(url, data);
      return response.data;
    } catch (error) {
      handleError(error);
      throw error;
    }
  };

  const remove = async (url, params) => {
    defaultError();
    try {
      const response = await axiosInstance.delete(url, { params });
      return response.data;
    } catch (error) {
      handleError(error);
      throw error;
    }
  };

  return {
    error,
    get,
    post,
    put,
    remove,
  };
};

export default useApi;
