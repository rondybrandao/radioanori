'''
Created on 20 de abr de 2017

@author: rondy
'''

class Loteria():
    sorteio = str
    def search_result(self):
        # valores capturados do usuario
        numeros_procurados = '{}'.format(self.search_input.text)
        #print(numeros_procurados)
        # abri arquivo loteria.txt e relaciona dta com valores
        f = open('lotofacil_teste2.txt')
        #print(f)
        dic = {}
        for linha in f:
            # y = str(linha.strip().split())
            # print(y)
            y = str(linha.split())
            # print(y)
            dic[y[1:18]] = y[20:107]
            # dic[y[0:2]] = y[4:19]
        #print(dic)
        f.close()
        v_encontrado = []
        value_encontrado = []
        b = "'',"
        for key_dic, value_dic in dic.items():
            # remove aspas e vigula
            for i in range(0, len(b)):
                value_dic = str(value_dic).replace(b[i], "")
                key_dic = str(key_dic).replace(b[i], "")

            for j in value_dic.split():
                for w in numeros_procurados.strip().split():
                    if w in j:
                        v_encontrado.append(key_dic[0:18])
                        value_encontrado.append(value_dic[0:])

        v = {}
        for p in v_encontrado:
            if p not in v:
                v[p] = 1
            else:
                v[p] += 1
        print(v_encontrado)
        print(v.items())

        #chaves contendo + 2,3,4,5,6 elementos
        k_encontrado=[]
        k_encontrado_12=[]
        k_encontrado_13 = []
        
        for key_v , value_v in v.items():
            if value_v == 2:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado.append(key_v)

            elif value_v == 3:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado_12.append(key_v)

            elif value_v == 4:
                for i in range(0, len(b)):
                    key_v = str(key_v).replace(b[i], "")

                k_encontrado_13.append(key_v)
        
        sorteio = k_encontrado;
        return sorteio;   