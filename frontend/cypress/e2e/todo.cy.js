describe('R8 - Todo list manipulation', () => {

  after(() => {
    // Hämta användarens ID via email
    cy.request('GET', 'http://localhost:5000/users/bymail/jane.doe@gmail.com')
      .then(response => {
        const userId = response.body._id.$oid
        // Radera användaren (och alla dess tasks/todos)
        cy.request('DELETE', `http://localhost:5000/users/${userId}`)
      })
    // Återskapa testdata
    cy.request('POST', 'http://localhost:5000/populate')
  })

  beforeEach(() => {
    cy.visit('http://localhost:3000')
    cy.get('input[type=text]').first().type('jane.doe@gmail.com')
    cy.get('input[type=submit]').click()
    cy.get('.container-element a').first().click()
  })

  // R8UC1 - TC1: add a todo when there is a description
  it('TC1: add a new todo-item', () => {
    cy.get('input[placeholder="Add a new todo item"]').type('my new todo', {force: true})
    cy.get('input[value="Add"]').click({force: true})
    cy.get('.todo-list').should('contain.text', 'my new todo')
  })

  // R8UC1 - TC2: Add-button is disabled when input is empty
  it('TC2: Add-button is disabled when input is empty', () => {
    cy.get('input[value="Add"]').should('be.disabled')
  })

  // R8UC2 - TC3: Toggle an active todo -> done
  it('TC3: toggle an active todo -> done', () => {
    cy.get('.checker').first().click()
    cy.get('.checker').first().should('have.class', 'checked')
  })

  // R8UC2 - TC4: Toggle a done todo-item back to active
  it('TC4: toggle a done todo-item back to active', () => {
    cy.get('.checker').first().click()
    cy.get('.checker').first().click()
    cy.get('.checker').first().should('have.class', 'unchecked')
  })

  // R8UC3 - TC5: Remove a todo-item
  it('TC5: removes a todo-item', () => {
    cy.get('.remover').first().click()
    cy.get('.todo-list').should('not.contain.text', 'Watch video')
  })
})