import axios from "axios";
import { createStore } from "vuex";
import { IServicio } from "../models/interfaces/serviciointerfaces";

const servicio: IServicio[] = [];
const servicioOwner: IServicio[] = [];

export const store = createStore({
  state() {
    return {
      servicio,
      servicioOwner,
    };
  },
  mutations: {
    async getAllServicio(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.servicio = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async postServicio(state, data: IServicio) {
      try {
        await axios.post("http://127.0.0.1:8000/servicios/create/", data);
        state.servicio.push(data);
      } catch (error) {
        console.log(error);
      }
    },
    async getServicio(state, url: string) {
      try {
        const resp = await axios.get(url);
        state.servicioOwner = [...resp.data];
      } catch (error) {
        console.log(error);
      }
    },
    async putServicio(state, props: { url: string; data: IServicio }) {
      try {
        await axios.put(props.url, props.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
});