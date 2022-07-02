import axios from 'axios'
import consts from '@/constants/index'

const instance = axios.create({
    baseURL: consts.backendUrl,
})

instance.interceptors.request.use(
    config => {
      config.headers = { 
        accept: 'application/json',
      }
      return config
    },
    error => {
      Promise.reject(error)
})

export default instance