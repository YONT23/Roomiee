<template>
    <div class="card card-border-color card-border-color-primary w-76 mx-auto">
        <form class="needs-validation" novalidate>
            <div class="card-header card-header-divider text-center fs-4">Registrarse</div>
            <div class="form-row">
                <div class="col-md-4 mb-3">
                    <label for="nombre" class="form-label">Nombre</label>
                    <input type="text" v-model="persona.nombre" id="nombre" class="form-control" required>
                    <label for="apellido" class="form-label">Apellido</label>
                    <input type="text" v-model="persona.apellido" id="apellido" class="form-control" required>
                    <label for="telefono" class="form-label">Telefono</label>
                    <input type="text" v-model="persona.telefono" id="telefono" class="form-control" required>
                    <label for="email" class="form-label">Correo</label>
                    <input type="email" v-model="persona.correo" id="email" class="form-control" required>
                    <div class="valid-feedback">
                        Looks good!
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="username" class="form-label">Username</label>
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text" id="inputGroupPrepend">@</span>
                        </div>
                        <input type="text" v-model="usuario.username" id="username" class="form-control"
                            placeholder="Username" aria-describedby="inputGroupPrepend" required>
                        <div class="invalid-feedback">
                            Please choose a username.
                        </div>
                    </div>
                    <label for="num_iden" class="form-label">Identificacion</label>
                    <input type="text" v-model="persona.Identificacion" id="num_iden" class="form-control" required>

                    <label for="tipo_iden" class="form-label">Tipo identificacion</label>
                    <select name="tipo_iden" id="tipo_iden" v-model="persona.tipo_identificacion">
                        <template v-for="i in dependencia">
                            <option :value="i['id']">{{ i['maes_nombre'] }}</option>
                        </template>
                    </select>
                    <br />
                    <label for="empleo" class="form-label">Empleo</label>
                    <input type="text" v-model="usuario.empleo" id="empleo" class="form-control" required>
                    <label for="ciudad" class="form-label">Ciudad</label>
                    <input type="text" v-model="persona.ciudad" id="ciudad" class="form-control" required>
                    <label for="salario" class="form-label">Salario</label>
                    <input type="number" v-model="usuario.salario" id="salario" class="form-control" required>
                    <div class="valid-feedback">
                        Looks good!
                    </div>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="password" class="form-label">Password</label>
                    <input type="password" v-model="usuario.password" id="password" class="form-control" required>
                </div>
            </div>
            <div class="form-group">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required>
                    <label class="form-check-label" for="invalidCheck">
                        Agree to terms and conditions
                    </label>
                    <div class="invalid-feedback">
                        You must agree before submitting.
                    </div>
                </div>
            </div>
            <button class="btn btn-success w-25" @click="submitData({ persona, usuario })">Save</button>{{ ' ' }}
            <router-link to="/persona/all/" class="btn btn-danger w-25">Cancel</router-link>
        </form>
    </div>
</template>


<script scope lang="ts">
import FormUsuario from "./formUser.vue";
import { PersonasI, Iusuario } from "../../models/personas";
import { store } from "../../context/store";
import axios from 'axios';

const persona: PersonasI = {
    apellido: '',
    ciudad: '',
    correo: '',
    nombre: '',
    Identificacion: '',
    telefono: '',
    tipo_identificacion: 0,
    tipo_sexo: ''
}

const usuario: Iusuario = {
    empleo: '',
    salario: 0,
    tipo_usuario: '',
    password: '',
    username: ''
}

type Tdata = PersonasI & Iusuario;

export default {
    components: {
        FormUsuario
    },
    data() {
        return {
            persona,
            usuario,
            dependencia: []
        }
    },
    methods: {
        submitData(data: any) {
            store.commit('registerUser', data)
        }
    },
    async beforeMount() {
        const dependencias = await axios.post('http://localhost:8000/maestra/dependencias/', { dependencia: '' });
        const id = (dependencias.data as Array<any>).filter((maestra) => maestra.maes_nombre === 'tipo_identificacion')[0].id
        const resp = await axios.post('http://localhost:8000/maestra/dependencias/', { dependencia: `${id}` });
        this.$data.dependencia = resp.data;
    }
}
</script>


<style>
.container-main {
    height: auto;
}
</style>