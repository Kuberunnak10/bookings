import pytest

from app.users.dao import UserDAO


@pytest.mark.parametrize('user_id, email, exist',
                         [(1, 'test@test.com', True),
                          (2, 'example@example.com', True),
                          (4, 'email@email.com', False)
                          ])
async def test_find_by_id(user_id, email, exist):
    user = await UserDAO.find_by_id(user_id)
    # print(user)
    if exist:
        assert user
        assert user.id == user_id
        assert user.email == email
    else:
        assert not user

