const isLocal = true;

const LOCAL_API_URL = 'http://localhost:8000';
const PROD_API_URL = 'https://acmandi.com/api';

export const API_URL = isLocal ? LOCAL_API_URL : PROD_API_URL;