from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1501   ._SN',
        MapName             = 'Bose',
        Location            = 'R1501.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
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
        'Ravennue Village',                     # 9
        'Abandoned Mine',                       # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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


    AddCharChip(
        'ED6_DT09/CH10030 ._CH',             # 00
        'ED6_DT09/CH10031 ._CH',             # 01
        'ED6_DT09/CH10860 ._CH',             # 02
        'ED6_DT09/CH10861 ._CH',             # 03
        'ED6_DT09/CH10310 ._CH',             # 04
        'ED6_DT09/CH10311 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10030P._CP',             # 00
        'ED6_DT09/CH10031P._CP',             # 01
        'ED6_DT09/CH10860P._CP',             # 02
        'ED6_DT09/CH10861P._CP',             # 03
        'ED6_DT09/CH10310P._CP',             # 04
        'ED6_DT09/CH10311P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
    )

    DeclNpc(
        X                   = 36890,
        Z                   = 30,
        Y                   = -87580,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7320,
        Z                   = -50,
        Y                   = -39290,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 49340,
        Z                   = -40,
        Y                   = -22100,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 65019,
        Z                   = 0,
        Y                   = -52280,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 86970,
        Z                   = 40,
        Y                   = -28980,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37970,
        Z                   = 40,
        Y                   = 3380,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x130,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36750,
        Z                   = 10,
        Y                   = 20760,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24510,
        Z                   = -50,
        Y                   = -10220,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x12F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 89310,
        TriggerZ            = -90,
        TriggerY            = -37830,
        TriggerRange        = 1000,
        ActorX              = 89340,
        ActorZ              = 1400,
        ActorY              = -37210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22370,
        TriggerZ            = -20,
        TriggerY            = 13370,
        TriggerRange        = 1000,
        ActorX              = 22100,
        ActorZ              = 1480,
        ActorY              = 13030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 99270,
        TriggerZ            = -50,
        TriggerY            = -16890,
        TriggerRange        = 1000,
        ActorX              = 99270,
        ActorZ              = 1450,
        ActorY              = -16890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17400,
        TriggerZ            = 50,
        TriggerY            = -11850,
        TriggerRange        = 1000,
        ActorX              = 16740,
        ActorZ              = 130,
        ActorY              = -11850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 54310,
        TriggerZ            = -130,
        TriggerY            = 8750,
        TriggerRange        = 1000,
        ActorX              = 55060,
        ActorZ              = -130,
        ActorY              = 8750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37000,
        TriggerZ            = 0,
        TriggerY            = -41450,
        TriggerRange        = 1500,
        ActorX              = 37000,
        ActorZ              = 150,
        ActorY              = -41450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2AB",          # 01, 1
        "Function_2_38F",          # 02, 2
        "Function_3_4BA",          # 03, 3
        "Function_4_5C2",          # 04, 4
        "Function_5_680",          # 05, 5
        "Function_6_681",          # 06, 6
        "Function_7_7B9",          # 07, 7
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Return()

    # Function_0_2AA end

    def Function_1_2AB(): pass

    label("Function_1_2AB")

    OP_16(0x2, 0xFA0, 0xFFFEDB08, 0xFFFDAE40, 0x230020)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    OP_B1("R1501_y")
    Jump("loc_2DE")

    label("loc_2D5")

    OP_B1("R1501_n")

    label("loc_2DE")

    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5")
    OP_6F(0x0, 0)
    Jump("loc_2FC")

    label("loc_2F5")

    OP_6F(0x0, 60)

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E")
    OP_6F(0x1, 0)
    Jump("loc_315")

    label("loc_30E")

    OP_6F(0x1, 60)

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_6F(0x2, 0)
    Jump("loc_32E")

    label("loc_327")

    OP_6F(0x2, 60)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_340")
    OP_6F(0x3, 0)
    Jump("loc_347")

    label("loc_340")

    OP_6F(0x3, 60)

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359")
    OP_6F(0x4, 0)
    Jump("loc_360")

    label("loc_359")

    OP_6F(0x4, 60)

    label("loc_360")

    OP_64(0x3, 0x1)
    OP_71(0x3, 0x0)
    OP_71(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_381")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_38E")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_38E")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_38E")

    Return()

    # Function_1_2AB end

    def Function_2_38F(): pass

    label("Function_2_38F")

    OP_EA(0x2, 0xD9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_467")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xE2, 1)"), scpexpr(EXPR_END)), "loc_400")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xE2\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B22)
    Jump("loc_464")

    label("loc_400")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xE2\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE2\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_464")

    Jump("loc_4AC")

    label("loc_467")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05There was an item here. It's gone now.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_38F end

    def Function_3_4BA(): pass

    label("Function_3_4BA")

    OP_EA(0x2, 0xDA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_592")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_52B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B23)
    Jump("loc_58F")

    label("loc_52B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_58F")

    Jump("loc_5B4")

    label("loc_592")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05No.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5B4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4BA end

    def Function_4_5C2(): pass

    label("Function_4_5C2")

    OP_EA(0x2, 0xDB, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x2, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #6
        "Found #2C#58IFire Sepith x200#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B24)
    Jump("loc_66E")

    label("loc_63C")


    AnonymousTalk(    #7
        "\x07\x05If you can read this, the clowns have won.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_66E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5C2 end

    def Function_5_680(): pass

    label("Function_5_680")

    Return()

    # Function_5_680 end

    def Function_6_681(): pass

    label("Function_6_681")

    OP_EA(0x2, 0xDC, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x364, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_6F2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B27)
    Jump("loc_756")

    label("loc_6F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_756")

    Jump("loc_7AB")

    label("loc_759")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Oh, hey, is there still something in here? ...Nope.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7AB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_681 end

    def Function_7_7B9(): pass

    label("Function_7_7B9")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #11
        "\x07\x05West: Ravennue Mine - 140 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_7B9 end

    SaveToFile()

Try(main)
