import unittest
from package_viacep.viacep import ViaCep

class TestViaCep(unittest.TestCase):
    def test_verifica_quantidade_digitos_cep_metodo_retorna_error(self):
        with self.assertRaises(ValueError):
            req1 = ViaCep()
            req1.GetData('4280819')
    
    def test_verifica_quantidade_letras_cep_metodo_retorna_error(self):
        with self.assertRaises(ValueError):
            req1 = ViaCep()
            req1.GetData('42b0b193')
    
    def test_verifica_quantidade_digitos_cep_metodo_retorna_Ok(self):
        req2 = ViaCep()
        data = req2.GetData('42808193')
        self.assertEqual(data['uf'], 'BA')

    def test_verifica_limpeza_traco_digitos_cep_metodo_retorna_Ok(self):
        req3 = ViaCep()
        data = req3.GetData('42808-193')
        self.assertEqual(data['uf'], 'BA')

    def test_verifica_limpeza_traco_ponto_digitos_cep_metodo_retorna_Ok(self):
        req4 = ViaCep()
        data = req4.GetData('42.808-193')
        self.assertEqual(data['uf'], 'BA')

    #def test_verifica_quantidade_digitos_cep_atributo_retorna_Error(self):
    #    with self.assertRaises(ValueError):
    #        setattr(ViaCep, 'cep', '42808193')
        

unittest.main(verbosity=2)
