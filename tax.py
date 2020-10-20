
def BCTax(Income):
  tax_dict =dict([(220000,20.50),
                  (157748,16.80),
                  (116344,14.70),
                  (95812,12.29),
                  (83451,10.50),
                  (41725,7.70),
                  (0,5.06)
                  ])
  bcTax=0
  for bracket in tax_dict:
       rate = tax_dict[bracket]
       tax, Income = calc(bcTax, Income, bracket, rate)
       bcTax += tax
  return bcTax

def calc(y, Income, bracket, rate):
  tax=0
  if Income>bracket:
    z = Income-bracket
    tax += z *rate/100
    Income -= z
  return tax, Income

def FedTax(Income):
  tax_dict =dict([(214368,33),
                  (150473,29.00),
                  (97069.01,26),
                  (48535.01,20.5),
                  (0,15)
                  ])
  fedTax=0
  for bracket in tax_dict:
       rate = tax_dict[bracket]
       tax, Income = calc(fedTax, Income, bracket, rate)
       fedTax += tax
  return fedTax

def CanadaTax(Income):
  return FedTax(Income)+BCTax(Income)