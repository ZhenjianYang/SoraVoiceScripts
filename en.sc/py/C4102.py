from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4102   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'Erbe Royal Villa',                     # 9
        'Royal Avenue',                         # 10
        '丘陵ビー',                             # 11
        'ワニ',                                 # 12
        'ワニ',                                 # 13
        '沼チュパカブラ',                       # 14
        'プリメーラ',                           # 15
        '丘陵ビー',                             # 16
        'ヘルマーズ',                           # 17
        'ヘルマーズ',                           # 18
        'ウォーバット',                         # 19
        'ダインダイル',                         # 20
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
        'ED6_DT09/CH10780 ._CH',             # 00
        'ED6_DT09/CH10781 ._CH',             # 01
        'ED6_DT09/CH10790 ._CH',             # 02
        'ED6_DT09/CH10791 ._CH',             # 03
        'ED6_DT09/CH10050 ._CH',             # 04
        'ED6_DT09/CH10051 ._CH',             # 05
        'ED6_DT09/CH10800 ._CH',             # 06
        'ED6_DT09/CH10801 ._CH',             # 07
        'ED6_DT09/CH10810 ._CH',             # 08
        'ED6_DT09/CH10811 ._CH',             # 09
        'ED6_DT09/CH10820 ._CH',             # 0A
        'ED6_DT09/CH10821 ._CH',             # 0B
        'ED6_DT09/CH11220 ._CH',             # 0C
        'ED6_DT09/CH11221 ._CH',             # 0D
        'ED6_DT09/CH11230 ._CH',             # 0E
        'ED6_DT09/CH11231 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10780P._CP',             # 00
        'ED6_DT09/CH10781P._CP',             # 01
        'ED6_DT09/CH10790P._CP',             # 02
        'ED6_DT09/CH10791P._CP',             # 03
        'ED6_DT09/CH10050P._CP',             # 04
        'ED6_DT09/CH10051P._CP',             # 05
        'ED6_DT09/CH10800P._CP',             # 06
        'ED6_DT09/CH10801P._CP',             # 07
        'ED6_DT09/CH10810P._CP',             # 08
        'ED6_DT09/CH10811P._CP',             # 09
        'ED6_DT09/CH10820P._CP',             # 0A
        'ED6_DT09/CH10821P._CP',             # 0B
        'ED6_DT09/CH11220P._CP',             # 0C
        'ED6_DT09/CH11221P._CP',             # 0D
        'ED6_DT09/CH11230P._CP',             # 0E
        'ED6_DT09/CH11231P._CP',             # 0F
    )

    DeclNpc(
        X                   = 77370,
        Z                   = 0,
        Y                   = -15080,
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
        X                   = -79490,
        Z                   = 0,
        Y                   = 4930,
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
        X                   = 29090,
        Z                   = 110,
        Y                   = -28620,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 35270,
        Z                   = 0,
        Y                   = -43590,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34970,
        Z                   = 100,
        Y                   = -63310,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4820,
        Z                   = 100,
        Y                   = -79050,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5370,
        Z                   = 120,
        Y                   = -58670,
        Unknown_0C          = 0,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x260,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12310,
        Z                   = 10,
        Y                   = 7720,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x259,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 34490,
        Z                   = 40,
        Y                   = 31600,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21340,
        Z                   = 10,
        Y                   = 64120,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 32640,
        Z                   = 90,
        Y                   = 49450,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6330,
        Z                   = 140,
        Y                   = 2330,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x25C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 480,
        TriggerZ            = 0,
        TriggerY            = -67940,
        TriggerRange        = 1000,
        ActorX              = 1140,
        ActorZ              = 0,
        ActorY              = -67940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13310,
        TriggerZ            = -30,
        TriggerY            = 61150,
        TriggerRange        = 1000,
        ActorX              = 12570,
        ActorZ              = -30,
        ActorY              = 61290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7430,
        TriggerZ            = 30,
        TriggerY            = -17940,
        TriggerRange        = 1000,
        ActorX              = 7020,
        ActorZ              = 30,
        ActorY              = -18340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 24020,
        TriggerZ            = 500,
        TriggerY            = 54480,
        TriggerRange        = 1500,
        ActorX              = 24020,
        ActorZ              = 4000,
        ActorY              = 54480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3540,
        TriggerZ            = 500,
        TriggerY            = -67980,
        TriggerRange        = 1500,
        ActorX              = 3540,
        ActorZ              = 4000,
        ActorY              = -67980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_336",          # 00, 0
        "Function_1_379",          # 01, 1
        "Function_2_423",          # 02, 2
        "Function_3_555",          # 03, 3
        "Function_4_6D8",          # 04, 4
        "Function_5_86B",          # 05, 5
        "Function_6_8BD",          # 06, 6
    )


    def Function_0_336(): pass

    label("Function_0_336")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_378")

    Return()

    # Function_0_336 end

    def Function_1_379(): pass

    label("Function_1_379")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDE8D8, 0x230065)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB")
    OP_6F(0x0, 0)
    Jump("loc_3E2")

    label("loc_3DB")

    OP_6F(0x0, 60)

    label("loc_3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F4")
    OP_6F(0x1, 0)
    Jump("loc_3FB")

    label("loc_3F4")

    OP_6F(0x1, 60)

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40D")
    OP_6F(0x2, 0)
    Jump("loc_414")

    label("loc_40D")

    OP_6F(0x2, 60)

    label("loc_414")

    OP_E0(0x0, 0xF4, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x9C, 0xF6, 0xFE, 0xFF)
    Return()

    # Function_1_379 end

    def Function_2_423(): pass

    label("Function_2_423")

    OP_EA(0x2, 0xFA, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x263, 1)"), scpexpr(EXPR_END)), "loc_494")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x63\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1703)
    Jump("loc_4F8")

    label("loc_494")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x63\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x63\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4F8")

    Jump("loc_547")

    label("loc_4FB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Wear good shoes and you'll never see de feet.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_547")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_423 end

    def Function_3_555(): pass

    label("Function_3_555")

    OP_EA(0x2, 0xFB, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x287, 1)"), scpexpr(EXPR_END)), "loc_5C6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x87\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1705)
    Jump("loc_62A")

    label("loc_5C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x87\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x87\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_62A")

    Jump("loc_6CA")

    label("loc_62D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05The chest unleashes a poison gas trap! \x01",
            "...At least it would if it could. Because you\x01",
            "looted it already, and it hates you now.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6CA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_555 end

    def Function_4_6D8(): pass

    label("Function_4_6D8")

    OP_EA(0x2, 0xFC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_749")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1707)
    Jump("loc_7AD")

    label("loc_749")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_7AD")

    Jump("loc_85D")

    label("loc_7B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You don't find anything this time, but maybe if\x01",
            "you kept on opening and closing this one chest\x01",
            "over and over again... (Don't actually do this)\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_85D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6D8 end

    def Function_5_86B(): pass

    label("Function_5_86B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05There is an old cerulean stone monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_86B end

    def Function_6_8BD(): pass

    label("Function_6_8BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05There is an old vermillion stone monument.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_8BD end

    SaveToFile()

Try(main)
