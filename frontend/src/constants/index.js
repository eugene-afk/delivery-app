export default {
    backendUrl: process.env.VUE_APP_BACKEND ? process.env.VUE_APP_BACKEND : "http://localhost:5000/",
    mediaUrl: process.env.VUE_APP_MEDIA ? process.env.VUE_APP_MEDIA : "http://localhost:5000/static/",
}