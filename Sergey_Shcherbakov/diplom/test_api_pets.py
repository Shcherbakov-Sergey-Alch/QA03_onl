from DIPLOM.tools.constans import HOST_PET, PET_ID
from DIPLOM.tools.api_pets_steps import add_pet, get_pet_by_id, delete_pet
import allure


@allure.story("Check add, get and delete pet")
def test_pet():
    with allure.step("Add new pet"):
        add_new_pet = add_pet(HOST_PET, {"id": PET_ID, "name": "dars"})
        assert add_new_pet.status_code == 200, 'Error adding pet'
    with allure.step('Get pet by ID'):
        get_my_pet = get_pet_by_id(HOST_PET, PET_ID)
        assert get_my_pet.status_code == 200, 'Error getting pet'
    with allure.step('Delete pet'):
        delete_my_pet = delete_pet(HOST_PET, PET_ID)
        assert delete_my_pet.status_code == 200, 'Error deleting pet'
    with allure.step('Check pet does not exist'):
        get_my_pet_after_del = get_pet_by_id(HOST_PET, PET_ID)
        assert get_my_pet_after_del.status_code == 404
