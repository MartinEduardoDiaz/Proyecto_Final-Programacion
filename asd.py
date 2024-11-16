            """     
                if Pj.weapon_type == "bow":
                    Pj.shoot(mouse_pos)
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Pj.switch()




        for enemy in enemies:
            enemy.death()
            enemy.draw(screen)
            if Pj.weapon_type == "bow":
                Pj.weapon.update_arrows(enemy)



        
        Pj.UpdatePositionWeapon()
        key = pygame.key.get_pressed()
        Pj.draw(screen)
        Pj.move(key)





            

        Pj.weapon.draw(screen)
|       """