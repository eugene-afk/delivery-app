FROM node:18-alpine3.15
WORKDIR /app
ARG apiUrl
ARG mediaUrl
ENV PATH /app/node_modules/.bin:$PATH
COPY . ./
RUN yarn --silent
EXPOSE 8080
ENV VUE_APP_BACKEND=$apiUrl
ENV VUE_APP_MEDIA=$mediaUrl
RUN yarn build
RUN yarn global add serve
CMD ["serve", "-s", "dist"]