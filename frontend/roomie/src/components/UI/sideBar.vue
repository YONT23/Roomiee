<!-- <template>
    <aside class="main-sidebar sidebar-dark-primary elevation-4">

        <a href="#" class="brand-link text-center">
            <span class="brand-text font-weight-light">ROOMIE</span>
        </a>

        <div class="sidebar">
            <nav class="mt-2">
                <ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu">
                    <li class="nav-item">
                        <router-link to="/servicios/all" class="nav-link">
                            <i class="bi bi-house-door fs-5"></i>
                            &nbsp;&nbsp;
                            <p style="cursor: pointer;">
                                Home
                            </p>
                        </router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" @click="changeDisplay">
                            <i class="bi bi-archive fs-5"></i>
                            &nbsp;&nbsp;
                            <p style="cursor: pointer;">
                                Servicios
                                &nbsp;&nbsp;
                                <span v-if="display">
                                    <i class="bi bi-caret-down-fill"></i>
                                </span>
                                <span v-else>
                                    <i class="bi bi-caret-right-fill"></i>
                                </span>

                            </p>
                        </a>
                        <ul class="nav nav-treeview" id="nav-item_view" tabindex="0"
                            :style="[!display ? 'display:none' : 'display:block']">
                            <li class="nav-item ms-3">
                                <router-link to="/servicio/mine/" href="#" class="nav-link">
                                    <i class="bi bi-eye"></i>
                                    &nbsp;&nbsp;
                                    <p>Ver</p>
                                </router-link>
                            </li>
                            <li class="nav-item ms-3">
                                <router-link to="/servicio/register/" href="#" class="nav-link">
                                    <i class="bi bi-folder-plus"></i>
                                    &nbsp;&nbsp;
                                    <p>
                                        Registrar
                                        <i class="right fas fa-angle-left"></i>
                                    </p>
                                </router-link>
                            </li>
                        </ul>
                    </li>
                </ul>
            </nav>
        </div>
    </aside>
</template> -->


<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">ROOMIE</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <router-link to="/servicios/all" class="nav-link">
                    &nbsp;&nbsp;
                    <p style="cursor: pointer;"> Home </p>
                </router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" onclick="changeDisplay">
                    &nbsp;&nbsp;
                    <p style="cursor: pointer;"> Servicios </p>
                </a>
              </li>
              <li class="nav-item">
                <router-link to="/servicios/update/:id" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Actualizar <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/servicios/register/" href="#" class="nav-link">
                    &nbsp;&nbsp;
                    <p> Registrar <i class="right fas fa-angle-left"></i></p>
                </router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
</template>

<script lang="ts" scope>

export default {

    data() {
        return {
            display: false
        }
    },

    methods: {
        changeDisplay() {
            this.display = !this.display;
        }
    }
}

</script>

<style scoped lang="scss">

</style>