export interface ITablaMaestra {
    id?: number;
    tama_nombre1: string;
    tama_nombre2: string;
    tama_dependencia1: string;
    tama_dependencia2: string;
    tama_codigo: string;
    tama_estado: string; 
  }

export interface IPersonas {
    id?: number;
    pers_nombre: string;
    pers_apellido: string;
    pers_telefono: string;
    pers_direccion: string;
    identificacion: any;
    pers_numeroid: string; 
  }
  
  export interface IPropietario {
    id?: number;
    prop_respuesta: string;
    persona: any;
    cliente: any;
  }
  
  export interface ICliente {
    id?: number;
    persona: any;
    clie_nacionalidad: string;
    oficio: any;
  }

  export interface Ipropietariocliente {
    id?: number;
    procl_nota: string;
    propietario: any;
    cliente: any;
  }