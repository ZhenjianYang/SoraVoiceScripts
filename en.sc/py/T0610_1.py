from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0610_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0610_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_5F3",          # 01, 1
        "Function_2_80D",          # 02, 2
        "Function_3_1B34",         # 03, 3
        "Function_4_1FD6",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_8C(0xD, 250, 0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_12B")

    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1E2")
    SetChrName("Percy")

    ChrTalk(    #0
        0xD,
        "#6PFinally! The fog's all cleared up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xD,
        (
            "#6PI'd better start getting ready\x01",
            "to head out myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201")

    label("loc_1E2")


    ChrTalk(    #2
        0xD,
        "#6P*siiigh*... So boring.\x02",
    )

    CloseMessageWindow()

    label("loc_201")


    ChrTalk(    #3
        0x101,
        "#1015F#4PUmm, can I have a moment?\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xD)
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #4
        0xD,
        "#6PHm? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F#4PWe're from the guild.\x02\x03",

            "Are you Percy, the guy who posted a request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        "#6PYeah, you bet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        "#6PThank goodness you're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006F#4PWell, first we'd like to hear\x01",
            "the details of the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#5P#020FFrom what was posted on the bulletin board,\x01",
            "it seems you wanted some kind of investigation,\x01",
            "yes?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #10
        0xD,
        (
            "#6PYeah, actually I'd like to ask you to\x01",
            "search out the fishing spots in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        (
            "#6PI can explain the nitty-gritty if you're\x01",
            "up for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xD,
        "#6PSo, how about it? Will you do it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B8")
    Call(1, 2)
    Jump("loc_5F0")

    label("loc_4B8")


    ChrTalk(    #13
        0x101,
        (
            "#1007F#4PHmm... Sorry, but...\x02\x03",

            "We can't do your request right this second.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0xD,
        "#6POh, dear, dear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xD,
        "#6PYou got some kind of urgent work on hand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#5P#025FYes, I'm sorry.\x02\x03",

            "We'll be right back once we have the time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #17
        0xD,
        "#6PWell, that's fine too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        "#6PTalk to you later then.\x02",
    )

    CloseMessageWindow()
    OP_28(0x73, 0x1, 0x8000)

    label("loc_5F0")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_5F3(): pass

    label("Function_1_5F3")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66D")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_66D")

    TurnDirection(0xD, 0x101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #19
        0xD,
        "#6POh, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xD,
        (
            "#6PYou ready to go on a little fishing expedition,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756")
    Call(1, 2)
    Jump("loc_80A")

    label("loc_756")


    ChrTalk(    #21
        0x101,
        (
            "#1007F#4PSorry... We're still a bit busy.\x02\x03",

            "We'll be back once we've got some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xD,
        "#6POh, still no good, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "#6PWell, talk to you later then.\x01",
            "One day... Someday...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80A")

    EventEnd(0x0)
    Return()

    # Function_1_5F3 end

    def Function_2_80D(): pass

    label("Function_2_80D")


    ChrTalk(    #24
        0x101,
        (
            "#1006F#4PShouldn't be a problem.\x01",
            "You can leave it to us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #25
        0xD,
        "#6PAhh, thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xD,
        (
            "#6PYep, bracers really are the ones\x01",
            "to call when you're in need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1015F#4PBut, why are you looking for fishing spots?\x02\x03",

            "Even going so far as to spend mira on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        (
            "#6PAh, well, actually, I'm a member of\x01",
            "the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "#6PWe plan on holding a fishing class soon,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "#6PSo, I'm here doing a bit of fishing reconnaissance\x01",
            "in Rolent, which is a candidate location for the\x01",
            "class.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A57")

    ChrTalk(    #31
        0x104,
        (
            "#030FOh, a fishing class, hmm?\x01",
            "Quite cultural, excellent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA6")

    label("loc_A57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAF")

    ChrTalk(    #32
        0x108,
        (
            "#070FA fishing class.\x02\x03",

            "I'd like to join myself if I had the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA6")

    label("loc_AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4C")

    ChrTalk(    #33
        0x106,
        (
            "#052FYou guys are that into it, huh?\x02\x03",

            "I'd heard you were just a bunch'a weirdoes, but\x01",
            "looks like you take this stuff pretty seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA6")

    label("loc_B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA6")

    ChrTalk(    #34
        0x107,
        (
            "#560FOooooooh, a fishing class!\x02\x03",

            "Ahaha, I'd kind of like to learn too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA6")


    ChrTalk(    #35
        0xD,
        "#6PIt's a good plan, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "#6PIt went over really well even in the capital,\x01",
            "so I'm sure the next one will be an even\x01",
            "bigger hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xD,
        (
            "#6PReally, I'd like to do the lookin' about myself,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_CDE")

    ChrTalk(    #38
        0xD,
        (
            "#6PThanks to that fog, I don't have any time,\x01",
            "you see. That's why I decided to ask the pros.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D34")

    label("loc_CDE")


    ChrTalk(    #39
        0xD,
        (
            "#6PUnfortunately, we're stuck in this fog.\x01",
            "That's why I decided to ask the pros.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D34")


    ChrTalk(    #40
        0x103,
        (
            "#5P#020F...I see. I think we understand\x01",
            "the point of the investigation.\x02\x03",

            "So what should we be looking for,\x01",
            "specifically?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #41
        0xD,
        (
            "#6PWhat I want you to pinpoint are\x01",
            "the locations of the fishing spots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "#6PPlaces where you can pull up a fish,\x01",
            "basically. That's what I want you to report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1015F#4PSo...\x02\x03",

            "#1000FFind some good looking water and\x01",
            "fish up a fish, and that'll be good?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #44
        0xD,
        "#6PYeah, exactly!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xD,
        (
            "#6POooh, you seem pretty happy about it.\x01",
            "You into fishing?\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F67")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F67")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FB0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB0")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FF9")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1042")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1042")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_108B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10D4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10D4")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_111D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111D")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1166")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1166")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x8, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11AF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11AF")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11F8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11F8")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xA, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1241")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1241")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_128A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_128A")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12D3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D3")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_131C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_131C")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1365")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1365")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0xF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13AE")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13F7")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1440")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1440")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1489")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1489")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x13, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14D2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14D2")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_151B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_151B")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1564")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1564")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15AD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15AD")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x17, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_15F6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15F6")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_163F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_163F")

    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x12, 0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1688")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1698")
    OP_A2(0xB)

    label("loc_1698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1779")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Fishing a lot (normally choice split internally to fishing system)\x01",                   # 0
            "Haven't fished much at all (normally choice split internally to fishing system)\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1779")
    OP_A2(0xB)

    label("loc_1779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_184B")

    ChrTalk(    #46
        0x101,
        (
            "#1001F#4PAhaha, yeah, a bit. ♪\x02\x03",

            "I didn't think I'd be able to fish on the job,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        (
            "#6PHuh, I see we've got comrades even in the bracers.\x01",
            "Our glorious fishing revolution gains strength!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D5")

    label("loc_184B")


    ChrTalk(    #48
        0x101,
        (
            "#1003F#4PI like to fish, but...\x02\x03",

            "#1007FLately I've been so busy that\x01",
            "I've barely had a chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        "#6PHaha, I'm sorry to hear that.\x02",
    )

    CloseMessageWindow()

    label("loc_18D5")


    ChrTalk(    #50
        0xD,
        (
            "#6PWell, then, think of this as a break\x01",
            "in your normal work schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "#6PUltimately, fishing is a fun hobby, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1006F#4PWell, I intend to complete the mission as\x01",
            "thoroughly as I would any job, but I appreciate\x01",
            "you saying that.\x02\x03",

            "Welp, time to have a think about\x01",
            "where might be a good spot, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#5P#020FOnce we've gone over everything,\x01",
            "we'll be back to report.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #54
        0xD,
        "#6PYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xD,
        "#6PBe careful out there.\x02",
    )

    CloseMessageWindow()
    OP_28(0x73, 0x1, 0x1)
    OP_28(0x73, 0x4, 0x4)
    OP_28(0x73, 0x4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_1ABD")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x4)

    label("loc_1ABD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_1AD4")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x8)

    label("loc_1AD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_1AEB")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x10)

    label("loc_1AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_1B02")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x20)

    label("loc_1B02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1B19")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x40)

    label("loc_1B19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_1B30")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x80)

    label("loc_1B30")

    OP_A2(0x8)
    Return()

    # Function_2_80D end

    def Function_3_1B34(): pass

    label("Function_3_1B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1BA0")

    ChrTalk(    #56
        0xD,
        (
            "#6PCome by and report again once\x01",
            "you've made some progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        "#6PYeah, I'm counting on you!\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_1BA0")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -62390, 0, -22680, 270)
    SetChrPos(0x103, -62210, 0, -24020, 315)
    SetChrPos(0xF8, -61170, 0, -23660, 270)
    SetChrPos(0xF9, -61070, 0, -22240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1A")
    SetChrPos(0xF9, -61170, 0, -23660, 270)
    SetChrPos(0xF8, -61070, 0, -22240, 270)

    label("loc_1C1A")

    TurnDirection(0xD, 0x101, 0)
    OP_6D(-63450, 0, -21840, 0)
    OP_67(0, 6710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1CAD")

    ChrTalk(    #58
        0xD,
        "#6PHuh, could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        "#6PAre you already here to report?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D01")

    label("loc_1CAD")


    ChrTalk(    #60
        0xD,
        "#6POh, hey, bracers. Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        "#6PWell, then, let's hear how it's going.\x02",
    )

    CloseMessageWindow()

    label("loc_1D01")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x05Estelle reported on the state of the investigation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1D79")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1D79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1D8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1D8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_1DA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_1DB8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1DCD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_1DE2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1DE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DF6")
    Call(1, 4)
    Jump("loc_1FD3")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(    #63
        0xD,
        "#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "#6PSeems like you've made some progress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        "#6PBut, honestly I'd like you to go a bit further.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F#4PAww...\x02\x03",

            "So still not enough, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xD,
        "#6PYeah, sorry. Basically that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xD,
        (
            "#6PCheck over everything and make sure\x01",
            "you haven't missed anything, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xD,
        "#6PI'm counting on you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_1FD3")

    label("loc_1F41")


    ChrTalk(    #70
        0xD,
        (
            "#6PHuh? You still haven't made any progress\x01",
            "at all in the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "#6PCome back and report once you've\x01",
            "actually made progress.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_1FD3")

    EventEnd(0x0)
    Return()

    # Function_3_1B34 end

    def Function_4_1FD6(): pass

    label("Function_4_1FD6")

    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CE")
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0xD,
        "#6PHmm... Th-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xD,
        (
            "#6PI never thought there would be hidden\x01",
            "fishing spots in places like these!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xD,
        "#6PThis is incredible! Truly a perfect report!\x02",
    )

    CloseMessageWindow()
    OP_2B(0x73, 0x2)
    OP_2C(0x73, 0x7D0)
    Jump("loc_21DD")

    label("loc_20CE")


    ChrTalk(    #75
        0xD,
        "#6PHmm... I see, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xD,
        (
            "#6PIt's not exactly perfect, by the looks of it,\x01",
            "but I think you've investigated plenty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xD,
        "#6PMany thanks. You've really done well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xD,
        (
            "#6PWith an investigation report this good,\x01",
            "I can return to headquarters with my\x01",
            "rod held high.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DD")


    ChrTalk(    #79
        0x101,
        "#1011F#4PSo, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        "#5P#020FOur job's done, in other words?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #81
        0xD,
        "#6PYep, that's what it means.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xD,
        "#6PBut first, let me just say good work.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B5")

    ChrTalk(    #83
        0x104,
        "#034FPhew! Oh, my... Finally over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_22B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E1")

    ChrTalk(    #84
        0x107,
        "#067FPhew! We did it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_22E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231E")

    ChrTalk(    #85
        0x108,
        "#075FPhew! Mission accomplished, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2349")

    label("loc_231E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2349")

    ChrTalk(    #86
        0x106,
        "#551FFinally over, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_2349")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238B")

    ChrTalk(    #87
        0x105,
        "#045FI'm a bit tired from walking all over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_238B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CC")

    ChrTalk(    #88
        0x106,
        "#551FWell, we did end up walking all over.\x02",
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_23CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241D")

    ChrTalk(    #89
        0x108,
        (
            "#070FThis job was quite a bit more\x01",
            "tiring than I expected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_244F")

    label("loc_241D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244F")

    ChrTalk(    #90
        0x107,
        "#067FMy feet are kinda sore...\x02",
    )

    CloseMessageWindow()

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2A1F")

    ChrTalk(    #91
        0x101,
        (
            "#1015F#4PYeah, it was kinda hard, but...\x02\x03",

            "#1001FI got to fish for the first time in a while,\x01",
            "so I'm pretty happy. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        "#5P#021FSeems it was a good break.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #93
        0xD,
        "#6PWell, glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        (
            "#6PI've left the formal reward with the guild,\x01",
            "so that's taken care of, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xD,
        "#6PSince it's come up, here, take this too.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #96
        "\x07\x00Received #595i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x253, 1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #97
        0x101,
        "#1004F#4POh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#6PHeh heh, pretty nice, right? It's a specially-made\x01",
            "rod exclusively for big catches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "#6PI'm sure you'll be able to use it. Let me offer\x01",
            "this as my personal thanks for a job well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1008F#4PY-You sure? This is an awfully nice rod...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "#6PYep. Positive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "#6PThe Fisherman's Guild does not hesitate to\x01",
            "invest in the development and standardization\x01",
            "of fishing culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xD,
        "#6POoh, but anyway, can't stay to chat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xD,
        (
            "#6PI've got to get back to the capital\x01",
            "and deliver the investigation report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1011F#4PAh, okay...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2880")

    ChrTalk(    #106
        0x108,
        "#070FWell, then, take care on your way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2944")

    label("loc_2880")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(    #107
        0x106,
        "#051FTake care on your way to the capital.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2944")

    label("loc_28C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2902")

    ChrTalk(    #108
        0x104,
        "#030FHeh, I'll pray for your safe journey.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2944")

    label("loc_2902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(    #109
        0x107,
        "#560FUm, take care on your way to the capital.\x02",
    )

    CloseMessageWindow()

    label("loc_2944")


    ChrTalk(    #110
        0xD,
        "#6PI guess this is goodbye, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        (
            "#6PYou really helped me out today.\x01",
            "Keep up the good work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xD,
        (
            "#6PIf you get the chance, drop by\x01",
            "the headquarters in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1000F#4PLook forward to it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FC8")

    label("loc_2A1F")


    ChrTalk(    #114
        0x101,
        (
            "#1015F#4PYeah, it was kinda hard, but...\x02\x03",

            "I got to fish for the first time in a while,\x01",
            "so I'm pretty happy.\x02\x03",

            "#1007FWell, given the situation I couldn't\x01",
            "really relax, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #115
        0xD,
        (
            "#6PI see, I guess you bracers must be\x01",
            "pretty busy with this fog business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#6PThanks for taking the time even\x01",
            "though we're in the thick of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#5P#020FIt was no problem at all.\x02\x03",

            "A sincere response to all requests\x01",
            "is our mission, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1006F#4PYeah, what Schera said.\x02\x03",

            "And it was a good chance for\x01",
            "a break, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        "#6PWell, thanks. I 'preciate you saying that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xD,
        (
            "#6PI've left the formal reward with the guild,\x01",
            "so that's taken care of, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xD,
        "#6PSince it's come up, here, take this too.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #122
        "\x07\x00Received #595i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x253, 1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x101,
        "#1004F#4POh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xD,
        (
            "#6PHeh heh, pretty nice, right? It's a specially-made\x01",
            "rod exclusively for big catches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xD,
        (
            "#6PI'm sure you'll be able to use it. Let me offer\x01",
            "this as my personal thanks for a job well done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1008F#4PY-You sure? This is an awfully nice rod...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xD,
        "#6PYep. Positive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xD,
        (
            "#6PThe Fisherman's Guild does not hesitate to\x01",
            "invest in the development and standardization\x01",
            "of fishing culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        "#6PWell, this is goodbye...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xD,
        (
            "#6PYou really helped me out today.\x01",
            "Keep up the good work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1006F#4PWill do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xD,
        (
            "#6PI'll offer my prayers to the Goddess\x01",
            "that this fog clears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x103,
        "#5P#020FTake care on your way.\x02",
    )

    CloseMessageWindow()

    label("loc_2FC8")


    def lambda_2FCE():

        label("loc_2FCE")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2FCE")

    QueueWorkItem2(0x101, 3, lambda_2FCE)

    def lambda_2FDF():

        label("loc_2FDF")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2FDF")

    QueueWorkItem2(0x103, 3, lambda_2FDF)

    def lambda_2FF0():

        label("loc_2FF0")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_2FF0")

    QueueWorkItem2(0xF8, 3, lambda_2FF0)

    def lambda_3001():

        label("loc_3001")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_3001")

    QueueWorkItem2(0xF9, 3, lambda_3001)
    OP_8C(0xD, 0, 400)
    OP_8E(0xD, 0xFFFF0790, 0x0, 0xFFFFAD94, 0x7D0, 0x0)
    OP_8E(0xD, 0xFFFF0DEE, 0x0, 0xFFFFAFCE, 0x7D0, 0x0)
    OP_8C(0xD, 0, 400)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x13)
    OP_73(0x1)
    OP_8E(0xD, 0xFFFF0DEE, 0x0, 0xFFFFB668, 0x7D0, 0x0)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_72(0x1, 0x800)
    OP_6F(0x1, 19)
    OP_70(0x1, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x1, 0x800)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0xF8, 0x3)
    OP_44(0xF9, 0x3)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #134
        "Quest #2C[Fishing Spot Search] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x73, 0x1, 0x100)
    OP_28(0x73, 0x4, 0x10)
    Return()

    # Function_4_1FD6 end

    SaveToFile()

Try(main)
