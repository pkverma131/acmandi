const isLocal = false;

const LOCAL_API_URL = 'http://localhost:8000/api';
const PROD_API_URL = 'https://acmandi.com/api';

export const API_URL = isLocal ? LOCAL_API_URL : PROD_API_URL;