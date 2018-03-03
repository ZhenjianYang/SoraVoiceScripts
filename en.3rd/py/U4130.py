from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4130   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclActor(
        TriggerX            = 5830,
        TriggerZ            = 4000,
        TriggerY            = 5250,
        TriggerRange        = 1000,
        ActorX              = 6530,
        ActorZ              = 5000,
        ActorY              = 5220,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59930,
        TriggerZ            = 0,
        TriggerY            = -550,
        TriggerRange        = 1000,
        ActorX              = 60000,
        ActorZ              = 1000,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 61900,
        TriggerZ            = 0,
        TriggerY            = -550,
        TriggerRange        = 1000,
        ActorX              = 62000,
        ActorZ              = 1000,
        ActorY              = 150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -59340,
        TriggerZ            = 0,
        TriggerY            = 121250,
        TriggerRange        = 1000,
        ActorX              = -59340,
        ActorZ              = 1000,
        ActorY              = 121250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57530,
        TriggerZ            = 0,
        TriggerY            = 400,
        TriggerRange        = 800,
        ActorX              = 57290,
        ActorZ              = 900,
        ActorY              = 340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2480,
        TriggerZ            = -250,
        TriggerY            = -3810,
        TriggerRange        = 800,
        ActorX              = 2480,
        ActorZ              = 1100,
        ActorY              = -3810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_183",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_3DF",          # 03, 3
        "Function_4_59D",          # 04, 4
        "Function_5_6FE",          # 05, 5
        "Function_6_8C1",          # 06, 6
        "Function_7_979",          # 07, 7
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Return()

    # Function_0_182 end

    def Function_1_183(): pass

    label("Function_1_183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_196")
    OP_B1("U4130_y")
    Jump("loc_19F")

    label("loc_196")

    OP_B1("U4130_n")

    label("loc_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1")
    OP_6F(0x6, 0)
    Jump("loc_1B8")

    label("loc_1B1")

    OP_6F(0x6, 60)

    label("loc_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    OP_6F(0x7, 0)
    Jump("loc_1D1")

    label("loc_1CA")

    OP_6F(0x7, 60)

    label("loc_1D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3")
    OP_6F(0x8, 0)
    Jump("loc_1EA")

    label("loc_1E3")

    OP_6F(0x8, 60)

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC")
    OP_6F(0x9, 0)
    Jump("loc_203")

    label("loc_1FC")

    OP_6F(0x9, 60)

    label("loc_203")

    Return()

    # Function_1_183 end

    def Function_2_204(): pass

    label("Function_2_204")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AC, 1)"), scpexpr(EXPR_END)), "loc_272")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xAC\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2788)
    Jump("loc_2DA")

    label("loc_272")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xAC\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xAC\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_2DA")

    Jump("loc_3D1")

    label("loc_2DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05[9/36] The story truly begins neither with Genevieve nor with Jubilee,\x01",
            "but with the shop in the letter. Located in Bose, cramped between two\x01",
            "of the most popular shops on the block, was a tiny, tiny building. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x100, 0x0)

    label("loc_3D1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_204 end

    def Function_3_3DF(): pass

    label("Function_3_3DF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19C, 1)"), scpexpr(EXPR_END)), "loc_44D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x9C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2789)
    Jump("loc_4B5")

    label("loc_44D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x9C\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x9C\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_4B5")

    Jump("loc_58F")

    label("loc_4B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05(7/12) Each time Hideko reflected on these events, feelings of remorse\x01",
            "would wash over her. If only I'd had the courage to refuse that door-to-\x01",
            "door bargain all those years ago...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x101, 0x0)

    label("loc_58F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3DF end

    def Function_4_59D(): pass

    label("Function_4_59D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_676")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x199, 1)"), scpexpr(EXPR_END)), "loc_60B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x99\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x278A)
    Jump("loc_673")

    label("loc_60B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x99\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x99\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_673")

    Jump("loc_6F0")

    label("loc_676")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05The chest is empty.\x01",
            "Look, YOU try coming up with hundreds of these across three games.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x102, 0x0)

    label("loc_6F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_59D end

    def Function_5_6FE(): pass

    label("Function_5_6FE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x165, 1)"), scpexpr(EXPR_END)), "loc_76C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x65\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2795)
    Jump("loc_7D4")

    label("loc_76C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x65\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x65\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x9, 60)
    OP_70(0x9, 0x0)

    label("loc_7D4")

    Jump("loc_8B3")

    label("loc_7D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Did you know? Early concepts had Joshua as the protagonist while Estelle\x01",
            "had Joshua's current role. Over time, however, the team believed it made\x01",
            "more sense if the roles were switched.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x103, 0x0)

    label("loc_8B3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6FE end

    def Function_6_8C1(): pass

    label("Function_6_8C1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "\x07\x05The Baral Coffee House's specialty!\x01",
            "[Curry of Dreams] - 900 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #13
        (
            "\x07\x05Try our hot curry, cooked to perfection\x01",
            "with our secret spices!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_8C1 end

    def Function_7_979(): pass

    label("Function_7_979")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #14
        (
            "\x07\x05- Menu -\x01",
            "Mocking Pie           400 mira\x01",
            "Tomatrio Sandwich    1,400 mira\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #15
        (
            "\x07\x05- Chef's Recommendations -\x01",
            "Seafood Hotpot     1,200 mira\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_979 end

    SaveToFile()

Try(main)
