class A:
  Attr =100
  def _init_(self):
    print "Calling Class A Constructor"
    
  def A_method1(self):
      print "calling parent method"
   def A_method2(self, attribute):
       A.Attr = attribute
   def A_method3(self):
       print ("Parent Attribute : ", A.Attr)
       
Class B(A):
     def _init_(self):
         print "Calling Class B constructor"
     def B_method1(self):
          print ("Calling child method")
          
child_class = B()
child_class.A_method2(100)
child_class.A_method3() # it prints the output of -"Parent Attribute : " 100"

