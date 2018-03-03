from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5506   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5506.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
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


    AddCharChip(
        'ED6_DT29/CH14740 ._CH',             # 00
        'ED6_DT29/CH14741 ._CH',             # 01
        'ED6_DT29/CH14540 ._CH',             # 02
        'ED6_DT29/CH14541 ._CH',             # 03
        'ED6_DT29/CH15110 ._CH',             # 04
        'ED6_DT29/CH15111 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14740P._CP',             # 00
        'ED6_DT29/CH14741P._CP',             # 01
        'ED6_DT29/CH14540P._CP',             # 02
        'ED6_DT29/CH14541P._CP',             # 03
        'ED6_DT29/CH15110P._CP',             # 04
        'ED6_DT29/CH15111P._CP',             # 05
    )

    DeclMonster(
        X                   = 37660,
        Z                   = 0,
        Y                   = 37770,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x197,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 50140,
        Z                   = 0,
        Y                   = 5540,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15580,
        Z                   = 0,
        Y                   = -2310,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 46400,
        TriggerZ            = 0,
        TriggerY            = 38540,
        TriggerRange        = 1000,
        ActorX              = 46400,
        ActorZ              = 1000,
        ActorY              = 38540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 42470,
        TriggerZ            = 0,
        TriggerY            = -15200,
        TriggerRange        = 1000,
        ActorX              = 42470,
        ActorZ              = 1000,
        ActorY              = -15200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 46200,
        TriggerZ            = 0,
        TriggerY            = 36480,
        TriggerRange        = 1000,
        ActorX              = 46200,
        ActorZ              = 1000,
        ActorY              = 36480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_19B",          # 01, 1
        "Function_2_1F9",          # 02, 2
        "Function_3_355",          # 03, 3
        "Function_4_49A",          # 04, 4
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Return()

    # Function_0_19A end

    def Function_1_19B(): pass

    label("Function_1_19B")

    OP_16(0x2, 0xFA0, 0xFFFE61F0, 0xFFFDFC60, 0x2300A3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF")
    OP_6F(0x0, 0)
    Jump("loc_1C6")

    label("loc_1BF")

    OP_6F(0x0, 60)

    label("loc_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8")
    OP_6F(0x1, 0)
    Jump("loc_1DF")

    label("loc_1D8")

    OP_6F(0x1, 60)

    label("loc_1DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F1")
    OP_6F(0x2, 0)
    Jump("loc_1F8")

    label("loc_1F1")

    OP_6F(0x2, 60)

    label("loc_1F8")

    Return()

    # Function_1_19B end

    def Function_2_1F9(): pass

    label("Function_2_1F9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_267")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A8)
    Jump("loc_2CF")

    label("loc_267")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFB\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFB\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2CF")

    Jump("loc_347")

    label("loc_2D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You know, I'm worth a hell lot more sepith than that lousy trinket you just\x01",
            "took!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x7D, 0x0)

    label("loc_347")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1F9 end

    def Function_3_355(): pass

    label("Function_3_355")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4A3, 1)"), scpexpr(EXPR_END)), "loc_3C3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA3\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29A9)
    Jump("loc_42B")

    label("loc_3C3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA3\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA3\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_42B")

    Jump("loc_48C")

    label("loc_42E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05You found a plank of wood, but it seems to be nailed down.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x7E, 0x0)

    label("loc_48C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_355 end

    def Function_4_49A(): pass

    label("Function_4_49A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x535, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_579")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x1E9, 1)

    AnonymousTalk(    #6
        "\x07\x05Received \x1F\xE9\x01\x07\x05.\x02",
    )

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_567")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x43)"), scpexpr(EXPR_END)), "loc_508")
    Jump("loc_567")

    label("loc_508")

    CloseMessageWindow()

    AnonymousTalk(    #7
        "Found a scrap of paper with a recipe written on it.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #8
        "\x07\x05Learned the recipe for \x1F\xE9\x01\x07\x05.\x02",
    )


    label("loc_567")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x29AA)
    Jump("loc_5E5")

    label("loc_579")


    AnonymousTalk(    #9
        (
            "\x07\x05The aromatic hickory lining of this chest permeated the Sludgy Cookies\x01",
            "with a mouth-watering flavor.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5E5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x7F, 0x0)
    Return()

    # Function_4_49A end

    SaveToFile()

Try(main)
