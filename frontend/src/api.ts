import { QueryFunctionContext } from "@tanstack/react-query";
import axios, { AxiosRequestConfig } from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
});

// 추후 로그인 할 때 토큰 저장하고 불러오는 방식으로 수정 예정
instance.interceptors.request.use(
  (config) => {
    const token =
      "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwayI6MX0.q_Ii58E_-AK9_Sj7pECy7nsK10NPpD_iMANe0kMTpZI";
    if (token) {
      config.headers.Authorization = token;
    }
    return config;
  },
  (error) => {
    console.error("Interceptor error:", error);
    return Promise.reject(error);
  }
);

// Add a response interceptor for debugging
instance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error("Response error:", error);
    return Promise.reject(error);
  }
);

export const getRooms = async () => {
  try {
    const response = await instance.get("rooms/");
    return response.data;
  } catch (error) {
    console.error("getRooms error:", error);
    throw error;
  }
};

export const getRoom = async ({ queryKey }: QueryFunctionContext) => {
  const [_, roomPk] = queryKey;
  try {
    const response = await instance.get(`rooms/${roomPk}`);
    return response.data;
  } catch (error) {
    console.error("getRoom error:", error);
    throw error;
  }
};
