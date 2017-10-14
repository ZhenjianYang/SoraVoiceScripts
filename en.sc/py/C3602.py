from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3602   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3602.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH12660 ._CH',             # 00
        'ED6_DT29/CH12661 ._CH',             # 01
        'ED6_DT29/CH12670 ._CH',             # 02
        'ED6_DT29/CH12671 ._CH',             # 03
        'ED6_DT29/CH12680 ._CH',             # 04
        'ED6_DT29/CH12681 ._CH',             # 05
        'ED6_DT29/CH12690 ._CH',             # 06
        'ED6_DT29/CH12691 ._CH',             # 07
        'ED6_DT29/CH12700 ._CH',             # 08
        'ED6_DT29/CH12701 ._CH',             # 09
        'ED6_DT29/CH12710 ._CH',             # 0A
        'ED6_DT29/CH12711 ._CH',             # 0B
        'ED6_DT29/CH12720 ._CH',             # 0C
        'ED6_DT29/CH12721 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12660P._CP',             # 00
        'ED6_DT29/CH12661P._CP',             # 01
        'ED6_DT29/CH12670P._CP',             # 02
        'ED6_DT29/CH12671P._CP',             # 03
        'ED6_DT29/CH12680P._CP',             # 04
        'ED6_DT29/CH12681P._CP',             # 05
        'ED6_DT29/CH12690P._CP',             # 06
        'ED6_DT29/CH12691P._CP',             # 07
        'ED6_DT29/CH12700P._CP',             # 08
        'ED6_DT29/CH12701P._CP',             # 09
        'ED6_DT29/CH12710P._CP',             # 0A
        'ED6_DT29/CH12711P._CP',             # 0B
        'ED6_DT29/CH12720P._CP',             # 0C
        'ED6_DT29/CH12721P._CP',             # 0D
    )

    DeclMonster(
        X                   = 16890,
        Z                   = -3600,
        Y                   = -90,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7864,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30,
        Z                   = -3600,
        Y                   = 17250,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7865,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20800,
        Z                   = -3600,
        Y                   = 20800,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7866,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13110,
        Z                   = -3600,
        Y                   = -13270,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7867,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 60,
        Z                   = -450,
        Y                   = 61800,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x415,
        Unknown_18          = 7868,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24710,
        Z                   = -7600,
        Y                   = -24730,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7869,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24890,
        Z                   = -7600,
        Y                   = 24770,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7870,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24900,
        Z                   = -7600,
        Y                   = 24950,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7871,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24090,
        Z                   = -3600,
        Y                   = -300,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7872,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 300,
        Z                   = -3600,
        Y                   = -23660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7873,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 50,
        TriggerZ            = 0,
        TriggerY            = 72970,
        TriggerRange        = 1000,
        ActorX              = -40,
        ActorZ              = 0,
        ActorY              = 73590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6880,
        TriggerZ            = 0,
        TriggerY            = 66010,
        TriggerRange        = 1000,
        ActorX              = -7540,
        ActorZ              = 0,
        ActorY              = 66010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6880,
        TriggerZ            = 0,
        TriggerY            = 66010,
        TriggerRange        = 1000,
        ActorX              = 7580,
        ActorZ              = 0,
        ActorY              = 66010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22970,
        TriggerZ            = -3600,
        TriggerY            = 7630,
        TriggerRange        = 1000,
        ActorX              = -22840,
        ActorZ              = -3600,
        ActorY              = 8250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -16670,
        TriggerZ            = -3600,
        TriggerY            = -50,
        TriggerRange        = 1000,
        ActorX              = -15970,
        ActorZ              = -3600,
        ActorY              = 20,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -3600,
        TriggerY            = -16640,
        TriggerRange        = 1000,
        ActorX              = 10,
        ActorZ              = -3600,
        ActorY              = -15930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7680,
        TriggerZ            = -3600,
        TriggerY            = -22920,
        TriggerRange        = 1000,
        ActorX              = 8300,
        ActorZ              = -3600,
        ActorY              = -22720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45890,
        TriggerZ            = -8000,
        TriggerY            = -47410,
        TriggerRange        = 1000,
        ActorX              = 45890,
        ActorZ              = -8000,
        ActorY              = -47410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 45890,
        TriggerZ            = -8000,
        TriggerY            = 46040,
        TriggerRange        = 1000,
        ActorX              = 45890,
        ActorZ              = -8000,
        ActorY              = 46040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47420,
        TriggerZ            = -8000,
        TriggerY            = -47410,
        TriggerRange        = 1000,
        ActorX              = -47420,
        ActorZ              = -8000,
        ActorY              = -47410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47200,
        TriggerZ            = -7850,
        TriggerY            = 46160,
        TriggerRange        = 1000,
        ActorX              = -47200,
        ActorZ              = -7850,
        ActorY              = 46160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BE",          # 00, 0
        "Function_1_3F3",          # 01, 1
        "Function_2_55B",          # 02, 2
        "Function_3_6E9",          # 03, 3
        "Function_4_829",          # 04, 4
        "Function_5_974",          # 05, 5
        "Function_6_ABE",          # 06, 6
        "Function_7_BE8",          # 07, 7
        "Function_8_D11",          # 08, 8
        "Function_9_EA7",          # 09, 9
        "Function_10_1398",        # 0A, 10
        "Function_11_1B7E",        # 0B, 11
        "Function_12_2414",        # 0C, 12
        "Function_13_2B82",        # 0D, 13
        "Function_14_322D",        # 0E, 14
        "Function_15_332D",        # 0F, 15
        "Function_16_33A5",        # 10, 16
        "Function_17_34A5",        # 11, 17
        "Function_18_351D",        # 12, 18
        "Function_19_362F",        # 13, 19
        "Function_20_36B0",        # 14, 20
        "Function_21_37C2",        # 15, 21
        "Function_22_3843",        # 16, 22
        "Function_23_3922",        # 17, 23
        "Function_24_3A01",        # 18, 24
        "Function_25_3A4F",        # 19, 25
    )


    def Function_0_3BE(): pass

    label("Function_0_3BE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3D6"),
        (101, "loc_3DD"),
        (102, "loc_3E4"),
        (103, "loc_3EB"),
        (SWITCH_DEFAULT, "loc_3F2"),
    )


    label("loc_3D6")

    Event(0, 14)
    Jump("loc_3F2")

    label("loc_3DD")

    Event(0, 16)
    Jump("loc_3F2")

    label("loc_3E4")

    Event(0, 18)
    Jump("loc_3F2")

    label("loc_3EB")

    Event(0, 20)
    Jump("loc_3F2")

    label("loc_3F2")

    Return()

    # Function_0_3BE end

    def Function_1_3F3(): pass

    label("Function_1_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405")
    OP_6F(0x24, 0)
    Jump("loc_40C")

    label("loc_405")

    OP_6F(0x24, 60)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E")
    OP_6F(0x25, 0)
    Jump("loc_425")

    label("loc_41E")

    OP_6F(0x25, 60)

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437")
    OP_6F(0x26, 0)
    Jump("loc_43E")

    label("loc_437")

    OP_6F(0x26, 60)

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450")
    OP_6F(0x27, 0)
    Jump("loc_457")

    label("loc_450")

    OP_6F(0x27, 60)

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_469")
    OP_6F(0x28, 0)
    Jump("loc_470")

    label("loc_469")

    OP_6F(0x28, 60)

    label("loc_470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482")
    OP_6F(0x29, 0)
    Jump("loc_489")

    label("loc_482")

    OP_6F(0x29, 60)

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    OP_6F(0x2A, 0)
    Jump("loc_4A2")

    label("loc_49B")

    OP_6F(0x2A, 60)

    label("loc_4A2")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 0)), scpexpr(EXPR_END)), "loc_4D6")
    SetChrFlags(0x8, 0x80)

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 1)), scpexpr(EXPR_END)), "loc_4E2")
    SetChrFlags(0x9, 0x80)

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 2)), scpexpr(EXPR_END)), "loc_4EE")
    SetChrFlags(0xA, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 3)), scpexpr(EXPR_END)), "loc_4FA")
    SetChrFlags(0xB, 0x80)

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 4)), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0xC, 0x80)

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 5)), scpexpr(EXPR_END)), "loc_512")
    SetChrFlags(0xD, 0x80)

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 6)), scpexpr(EXPR_END)), "loc_51E")
    SetChrFlags(0xE, 0x80)

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D7, 7)), scpexpr(EXPR_END)), "loc_52A")
    SetChrFlags(0xF, 0x80)

    label("loc_52A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 0)), scpexpr(EXPR_END)), "loc_536")
    SetChrFlags(0x10, 0x80)

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 1)), scpexpr(EXPR_END)), "loc_542")
    SetChrFlags(0x11, 0x80)

    label("loc_542")

    Call(0, 9)
    OP_1B(0x0, 0x0, 0xF)
    OP_1B(0x1, 0x0, 0x11)
    OP_1B(0x2, 0x0, 0x13)
    OP_1B(0x3, 0x0, 0x15)
    Return()

    # Function_1_3F3 end

    def Function_2_55B(): pass

    label("Function_2_55B")

    OP_EA(0x2, 0xE2, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x24, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_5CC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F40)
    Jump("loc_630")

    label("loc_5CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x24, 60)
    OP_70(0x24, 0x0)

    label("loc_630")

    Jump("loc_6DB")

    label("loc_633")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Did you know that this treasure chest is an\x01",
            "S-rank bracer? Yes, treasure chests have their\x01",
            "own Bracer Guild. And this chest is legendary.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6DB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_55B end

    def Function_3_6E9(): pass

    label("Function_3_6E9")

    OP_EA(0x2, 0xE3, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x25, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xE3, 1)"), scpexpr(EXPR_END)), "loc_75A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xE3\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F42)
    Jump("loc_7BE")

    label("loc_75A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xE3\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE3\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x25, 60)
    OP_70(0x25, 0x0)

    label("loc_7BE")

    Jump("loc_81B")

    label("loc_7C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05This chest is empty. Not even half-empty,\x01",
            "just plain empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_81B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_6E9 end

    def Function_4_829(): pass

    label("Function_4_829")

    OP_EA(0x2, 0xE4, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_901")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x26, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xF0, 1)"), scpexpr(EXPR_END)), "loc_89A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF0\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F44)
    Jump("loc_8FE")

    label("loc_89A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF0\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF0\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x26, 60)
    OP_70(0x26, 0x0)

    label("loc_8FE")

    Jump("loc_966")

    label("loc_901")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05There's nothing in the chest, but the air\x01",
            "inside is strangely...humid.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_966")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_829 end

    def Function_5_974(): pass

    label("Function_5_974")

    OP_EA(0x2, 0xE5, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x27, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_9E5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F46)
    Jump("loc_A49")

    label("loc_9E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x27, 60)
    OP_70(0x27, 0x0)

    label("loc_A49")

    Jump("loc_AB0")

    label("loc_A4C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05When you stare too long into the chest, the chest\x01",
            "stares back at you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_974 end

    def Function_6_ABE(): pass

    label("Function_6_ABE")

    OP_EA(0x2, 0xE6, 0x0, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B86")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x28, 0x1E)
    OP_73(0x28)
    OP_6F(0x28, 30)
    AddSepith(0x2, 0x12C)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #12
        (
            "Found\x01",
            "#2C#58IFire Sepith x300\x01",
            "#62ITime Sepith x100\x01",
            "#60ISpace Sepith x100\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1F47)
    Jump("loc_BD6")

    label("loc_B86")


    AnonymousTalk(    #13
        (
            "\x07\x05The chest is angry at being robbed.\x01",
            "It demands you build it a shrubbery!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_BD6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_ABE end

    def Function_7_BE8(): pass

    label("Function_7_BE8")

    OP_EA(0x2, 0xE7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x29, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_C59")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F48)
    Jump("loc_CBD")

    label("loc_C59")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x29, 60)
    OP_70(0x29, 0x0)

    label("loc_CBD")

    Jump("loc_D03")

    label("loc_CC0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05This chest is as empty as your soul.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D03")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_BE8 end

    def Function_8_D11(): pass

    label("Function_8_D11")

    OP_EA(0x2, 0xE8, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2A, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_D82")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F49)
    Jump("loc_DE6")

    label("loc_D82")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2A, 60)
    OP_70(0x2A, 0x0)

    label("loc_DE6")

    Jump("loc_E99")

    label("loc_DE9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05As you crack the lid of the chest, you hear a\x01",
            "sound like the collective wailing of editors. You\x01",
            "let the lid drop, sealing the sound away forever.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E99")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_D11 end

    def Function_9_EA7(): pass

    label("Function_9_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_END)), "loc_F39")
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_6F(0xA, 360)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    Jump("loc_FC1")

    label("loc_F39")

    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_72(0x11, 0x20)
    OP_72(0xA, 0x8)
    OP_72(0xB, 0x8)
    OP_72(0xC, 0x8)
    OP_72(0xD, 0x8)
    OP_72(0xE, 0x8)
    OP_72(0xF, 0x8)
    OP_72(0x10, 0x8)
    OP_72(0x11, 0x8)
    OP_6F(0xA, 0)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_END)), "loc_1075")
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    Jump("loc_111F")

    label("loc_1075")

    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x5, 0x8)
    OP_72(0x6, 0x8)
    OP_72(0x7, 0x8)
    OP_72(0x8, 0x8)
    OP_72(0x9, 0x8)
    OP_6F(0x0, 0)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_END)), "loc_11B1")
    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_6F(0x12, 360)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    Jump("loc_1239")

    label("loc_11B1")

    OP_72(0x12, 0x20)
    OP_72(0x13, 0x20)
    OP_72(0x14, 0x20)
    OP_72(0x15, 0x20)
    OP_72(0x16, 0x20)
    OP_72(0x17, 0x20)
    OP_72(0x18, 0x20)
    OP_72(0x19, 0x20)
    OP_72(0x12, 0x8)
    OP_72(0x13, 0x8)
    OP_72(0x14, 0x8)
    OP_72(0x15, 0x8)
    OP_72(0x16, 0x8)
    OP_72(0x17, 0x8)
    OP_72(0x18, 0x8)
    OP_72(0x19, 0x8)
    OP_6F(0x12, 0)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)

    label("loc_1239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_END)), "loc_12ED")
    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x22, 0x20)
    OP_72(0x23, 0x20)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_72(0x22, 0x8)
    OP_72(0x23, 0x8)
    OP_6F(0x1A, 360)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)
    Jump("loc_1397")

    label("loc_12ED")

    OP_72(0x1A, 0x20)
    OP_72(0x1B, 0x20)
    OP_72(0x1C, 0x20)
    OP_72(0x1D, 0x20)
    OP_72(0x1E, 0x20)
    OP_72(0x1F, 0x20)
    OP_72(0x20, 0x20)
    OP_72(0x21, 0x20)
    OP_72(0x22, 0x20)
    OP_72(0x23, 0x20)
    OP_72(0x1A, 0x8)
    OP_72(0x1B, 0x8)
    OP_72(0x1C, 0x8)
    OP_72(0x1D, 0x8)
    OP_72(0x1E, 0x8)
    OP_72(0x1F, 0x8)
    OP_72(0x20, 0x8)
    OP_72(0x21, 0x8)
    OP_72(0x22, 0x8)
    OP_72(0x23, 0x8)
    OP_6F(0x1A, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)

    label("loc_1397")

    Return()

    # Function_9_EA7 end

    def Function_10_1398(): pass

    label("Function_10_1398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_185B")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0xA, 0x78)
    OP_70(0xA, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0xE, 0x64)
    OP_B0(0xF, 0x64)
    OP_B0(0x10, 0x64)
    OP_B0(0x11, 0x64)
    OP_70(0xE, 0xF0)
    Sleep(100)
    OP_70(0xF, 0xF0)
    Sleep(100)
    OP_70(0x10, 0xF0)
    Sleep(100)
    OP_70(0x11, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0xB, 0x64)
    OP_B0(0xC, 0x64)
    OP_B0(0xD, 0x64)
    OP_70(0xB, 0x168)
    OP_70(0xC, 0x168)
    OP_70(0xD, 0x168)
    OP_73(0xB)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #20
        (
            "\x07\x05#1S[Lakeside Underground Facility 1/4]\x01",
            "In or■■■ to m■ke the Seal Mec■■■■■m into a\x01",
            "■eal■■y, w■ needed b■■h ■■■■ous am■■nts ■■ energy\x01",
            "and mas■■■■ facil■■■■s. We, to ■■■■■■ the ■■■■,\x01",
            "■irs■ th■■■■ of using ■■e Aureole ■■lf.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x05#1SThe Aur■■le ■■spond■ to ■■■■■■ 's wishes ■■d gives\x01",
            "its boon--in ■■■er words, ■■ 'w■sh■■g' w■ thought\x01",
            "that ■■■■■ps we could ■ull the n■■■ed ■mo■■t of\x01",
            "e■■■gy ■■■■ ■■■ Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #22
        (
            "\x07\x05#1S... However, ■■■■ ■■■ not c■■e to ■■■■. Shortly\x01",
            "■fter ■h■ Aureole ■■■■ed auto■■■, it ■ur■■d to\x01",
            "simply ■■■■■■■■ b■st■■ing its ■■fts ■■■■dless\x01",
            "of ■■■ w■■h■s o■ the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #23
        "\x07\x00Received #1025i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x401, 1)
    OP_A2(0x1E0E)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0xA, 360)
    OP_6F(0xB, 0)
    OP_6F(0xC, 0)
    OP_6F(0xD, 0)
    OP_6F(0xE, 0)
    OP_6F(0xF, 0)
    OP_6F(0x10, 0)
    OP_6F(0x11, 0)
    OP_6D(44390, -7800, -49020, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 44390, -7800, -49020, 45)
    SetChrPos(0x1, 44390, -7800, -49020, 45)
    SetChrPos(0x2, 44390, -7800, -49020, 45)
    SetChrPos(0x3, 44390, -7800, -49020, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_1B7A")

    label("loc_185B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #24
        (
            "\x07\x05#1S[Lakeside Underground Facility 1/4]\x01",
            "In or■■■ to m■ke the Seal Mec■■■■■m into a\x01",
            "■eal■■y, w■ needed b■■h ■■■■ous am■■nts ■■ energy\x01",
            "and mas■■■■ facil■■■■s. We, to ■■■■■■ the ■■■■,\x01",
            "■irs■ th■■■■ of using ■■e Aureole ■■lf.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #25
        (
            "\x07\x05#1SThe Aur■■le ■■spond■ to ■■■■■■ 's wishes ■■d gives\x01",
            "its boon--in ■■■er words, ■■ 'w■sh■■g' w■ thought\x01",
            "that ■■■■■ps we could ■ull the n■■■ed ■mo■■t of\x01",
            "e■■■gy ■■■■ ■■■ Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #26
        (
            "\x07\x05#1S... However, ■■■■ ■■■ not c■■e to ■■■■. Shortly\x01",
            "■fter ■h■ Aureole ■■■■ed auto■■■, it ■ur■■d to\x01",
            "simply ■■■■■■■■ b■st■■ing its ■■fts ■■■■dless\x01",
            "of ■■■ w■■h■s o■ the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1B7A")

    TalkEnd(0xFF)
    Return()

    # Function_10_1398 end

    def Function_11_1B7E(): pass

    label("Function_11_1B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B0")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x0, 0x78)
    OP_70(0x0, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x4, 0x64)
    OP_B0(0x5, 0x64)
    OP_B0(0x6, 0x64)
    OP_B0(0x7, 0x64)
    OP_B0(0x8, 0x64)
    OP_B0(0x9, 0x64)
    OP_70(0x4, 0xF0)
    Sleep(100)
    OP_70(0x5, 0xF0)
    Sleep(100)
    OP_70(0x6, 0xF0)
    Sleep(100)
    OP_70(0x7, 0xF0)
    Sleep(100)
    OP_70(0x8, 0xF0)
    Sleep(100)
    OP_70(0x9, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1, 0x64)
    OP_B0(0x2, 0x64)
    OP_B0(0x3, 0x64)
    OP_70(0x1, 0x168)
    OP_70(0x2, 0x168)
    OP_70(0x3, 0x168)
    OP_73(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #27
        (
            "\x07\x05#1S[Lakeside Underground Facility 2/4]\x01",
            "We could ■ot ■■■ the ■■■er of th■ ■■■eo■■. Casting\x01",
            "our ■■■ b■■ond the ■■■■, we soug■■ ■■■er the\x01",
            "■■■■■■ sl■■■ing in the ■■■t■■■ ■■■ns that rest\x01",
            "deep be■■■■h the ■■■th, and requested to ■■■■■\x01",
            "■■■■■■res in t■■■■ ■o■■tions. However, ■■ we■■\x01",
            "■■■■■■■ under th■ ■a■c■ of the ■■■eole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #28
        (
            "\x07\x05#1S■■ seems ■■■ ■u■■■■■ had come ■o the ■on■■■sion\x01",
            "that its ■■■■■ prior■■■ was the con■■■■■■ ■■\x01",
            "the city, ■■d theref■re the elimination of ■■■\x01",
            "■■■■■■■ ob■■ac■es to ■■■at. So, to d■■■■■ the\x01",
            "Aureole, ■■ proc■■■ed with the ■■■st■■■tion of\x01",
            "these ■■■l■ings under the ■■■■■ o■ mo■■tor■■■\x01",
            "the s■■■■■■ veins.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Received #1026i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x402, 1)
    OP_A2(0x1E0F)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 360)
    OP_6F(0x1, 0)
    OP_6F(0x2, 0)
    OP_6F(0x3, 0)
    OP_6F(0x4, 0)
    OP_6F(0x5, 0)
    OP_6F(0x6, 0)
    OP_6F(0x7, 0)
    OP_6F(0x8, 0)
    OP_6F(0x9, 0)
    OP_6D(44260, -7800, 44300, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 44260, -7800, 44300, 45)
    SetChrPos(0x1, 44260, -7800, 44300, 45)
    SetChrPos(0x2, 44260, -7800, 44300, 45)
    SetChrPos(0x3, 44260, -7800, 44300, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_2410")

    label("loc_20B0")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #30
        (
            "\x07\x05#1S[Lakeside Underground Facility 2/4]\x01",
            "We could ■ot ■■■ the ■■■er of th■ ■■■eo■■. Casting\x01",
            "our ■■■ b■■ond the ■■■■, we soug■■ ■■■er the\x01",
            "■■■■■■ sl■■■ing in the ■■■t■■■ ■■■ns that rest\x01",
            "deep be■■■■h the ■■■th, and requested to ■■■■■\x01",
            "■■■■■■res in t■■■■ ■o■■tions. However, ■■ we■■\x01",
            "■■■■■■■ under th■ ■a■c■ of the ■■■eole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05#1S■■ seems ■■■ ■u■■■■■ had come ■o the ■on■■■sion\x01",
            "that its ■■■■■ prior■■■ was the con■■■■■■ ■■\x01",
            "the city, ■■d theref■re the elimination of ■■■\x01",
            "■■■■■■■ ob■■ac■es to ■■■at. So, to d■■■■■ the\x01",
            "Aureole, ■■ proc■■■ed with the ■■■st■■■tion of\x01",
            "these ■■■l■ings under the ■■■■■ o■ mo■■tor■■■\x01",
            "the s■■■■■■ veins.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2410")

    TalkEnd(0xFF)
    Return()

    # Function_11_1B7E end

    def Function_12_2414(): pass

    label("Function_12_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289B")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x12, 0x78)
    OP_70(0x12, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x16, 0x64)
    OP_B0(0x17, 0x64)
    OP_B0(0x18, 0x64)
    OP_B0(0x19, 0x64)
    OP_70(0x16, 0xF0)
    Sleep(100)
    OP_70(0x17, 0xF0)
    Sleep(100)
    OP_70(0x18, 0xF0)
    Sleep(100)
    OP_70(0x19, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x13, 0x64)
    OP_B0(0x14, 0x64)
    OP_B0(0x15, 0x64)
    OP_70(0x13, 0x168)
    OP_70(0x14, 0x168)
    OP_70(0x15, 0x168)
    OP_73(0x13)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #32
        (
            "\x07\x05#1S[Lakeside Underground Facility 3/4]\x01",
            "The ■■■■ty was ■■■■ roughly ■00 arge b■■■a■■\x01",
            "■he ■■■th on the ea■■■r■ side of ■■■■■■ ■■ke.\x01",
            "A■■■■ing ■■ our ■■■■ti■■tions, this ■as ■■e\x01",
            "loc■■ion wher■ the ■■■■■■■ ■■■■s g■th■■ed mo■■\x01",
            "■ffi■■■■ly. ■■■ l■nd beneath the ■■■■ was a\x01",
            "sp■■■■■ing pri■■■ f■■■■t. As i■ was ■■to■■■ed by\x01",
            "human ■■■■■■, the ■on■■ru■■■on had ■ittl■\x01",
            "effect ■■ it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #33
        (
            "\x07\x05#1S■■, while av■■■ing the ■■■■■■ion ■f the ■■■■■■■e,\x01",
            "co■■ected a■■ the ■■■h■■logy we had, an■ ■■■ried\x01",
            "to com■■■■■ the u■■■■■■r■■nd facilit■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #34
        "\x07\x00Received #1027i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x403, 1)
    OP_A2(0x1E10)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x12, 360)
    OP_6F(0x13, 0)
    OP_6F(0x14, 0)
    OP_6F(0x15, 0)
    OP_6F(0x16, 0)
    OP_6F(0x17, 0)
    OP_6F(0x18, 0)
    OP_6F(0x19, 0)
    OP_6D(-49000, -7800, -49110, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -49000, -7800, -49110, 45)
    SetChrPos(0x1, -49000, -7800, -49110, 45)
    SetChrPos(0x2, -49000, -7800, -49110, 45)
    SetChrPos(0x3, -49000, -7800, -49110, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_2B7E")

    label("loc_289B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #35
        (
            "\x07\x05#1S[Lakeside Underground Facility 3/4]\x01",
            "The ■■■■ty was ■■■■ roughly ■00 arge b■■■a■■\x01",
            "■he ■■■th on the ea■■■r■ side of ■■■■■■ ■■ke.\x01",
            "A■■■■ing ■■ our ■■■■ti■■tions, this ■as ■■e\x01",
            "loc■■ion wher■ the ■■■■■■■ ■■■■s g■th■■ed mo■■\x01",
            "■ffi■■■■ly. ■■■ l■nd beneath the ■■■■ was a\x01",
            "sp■■■■■ing pri■■■ f■■■■t. As i■ was ■■to■■■ed by\x01",
            "human ■■■■■■, the ■on■■ru■■■on had ■ittl■\x01",
            "effect ■■ it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #36
        (
            "\x07\x05#1S■■, while av■■■ing the ■■■■■■ion ■f the ■■■■■■■e,\x01",
            "co■■ected a■■ the ■■■h■■logy we had, an■ ■■■ried\x01",
            "to com■■■■■ the u■■■■■■r■■nd facilit■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B7E")

    TalkEnd(0xFF)
    Return()

    # Function_12_2414 end

    def Function_13_2B82(): pass

    label("Function_13_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC2")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    OP_B0(0x1A, 0x78)
    OP_70(0x1A, 0x168)
    Sleep(2500)
    OP_22(0x9D, 0x0, 0x64)
    OP_B0(0x1E, 0x64)
    OP_B0(0x1F, 0x64)
    OP_B0(0x20, 0x64)
    OP_B0(0x21, 0x64)
    OP_B0(0x22, 0x64)
    OP_B0(0x23, 0x64)
    OP_70(0x1E, 0xF0)
    Sleep(100)
    OP_70(0x1F, 0xF0)
    Sleep(100)
    OP_70(0x20, 0xF0)
    Sleep(100)
    OP_70(0x21, 0xF0)
    Sleep(100)
    OP_70(0x22, 0xF0)
    Sleep(100)
    OP_70(0x23, 0xF0)
    Sleep(100)
    OP_22(0xB9, 0x0, 0x64)
    OP_B0(0x1B, 0x64)
    OP_B0(0x1C, 0x64)
    OP_B0(0x1D, 0x64)
    OP_70(0x1B, 0x168)
    OP_70(0x1C, 0x168)
    OP_70(0x1D, 0x168)
    OP_73(0x1B)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #37
        (
            "\x07\x05#1S[Lakeside Underground Facility 4/4]\x01",
            "Wh■■■ the c■■■■r■■tion of ■he under■■■■■ ■■■ility\x01",
            "was ■■der■■y, ■■ ■■■■■ ad■■■io■■l ■■ruc■ur■■\x01",
            "■■ ■■■ fr■■ges of the surface. The A■■■■■ur■,\x01",
            "whose ■■■er wa■■ points eve■ toward■ ■■■ Aureole,\x01",
            "■nd the four ■■vi■■ ■■■■■ that ■■rround the\x01",
            "Aur■■■e.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #38
        (
            "\x07\x05#1S■■■■ syste■ of str■■■■■es po■■e■■ed a ■■■t■cal\x01",
            "ro■e ■■ the pla■ and ■■re a■ vital ■■ ■■■ S■■l\x01",
            "■■chan■■■ as the ■■■■■ground ■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #39
        "\x07\x00Received #1028i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x404, 1)
    OP_A2(0x1E1A)
    Sleep(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x1A, 360)
    OP_6F(0x1B, 0)
    OP_6F(0x1B, 0)
    OP_6F(0x1C, 0)
    OP_6F(0x1D, 0)
    OP_6F(0x1E, 0)
    OP_6F(0x1F, 0)
    OP_6F(0x20, 0)
    OP_6F(0x21, 0)
    OP_6F(0x22, 0)
    OP_6F(0x23, 0)
    OP_6D(-49080, -7800, 44450, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -49080, -7800, 44450, 45)
    SetChrPos(0x1, -49080, -7800, 44450, 45)
    SetChrPos(0x2, -49080, -7800, 44450, 45)
    SetChrPos(0x3, -49080, -7800, 44450, 45)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Jump("loc_3229")

    label("loc_2FC2")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    AnonymousTalk(    #40
        (
            "\x07\x05#1S[Lakeside Underground Facility 4/4]\x01",
            "Wh■■■ the c■■■■r■■tion of ■he under■■■■■ ■■■ility\x01",
            "was ■■der■■y, ■■ ■■■■■ ad■■■io■■l ■■ruc■ur■■\x01",
            "■■ ■■■ fr■■ges of the surface. The A■■■■■ur■,\x01",
            "whose ■■■er wa■■ points eve■ toward■ ■■■ Aureole,\x01",
            "■nd the four ■■vi■■ ■■■■■ that ■■rround the\x01",
            "Aur■■■e.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        (
            "\x07\x05#1S■■■■ syste■ of str■■■■■es po■■e■■ed a ■■■t■cal\x01",
            "ro■e ■■ the pla■ and ■■re a■ vital ■■ ■■■ S■■l\x01",
            "■■chan■■■ as the ■■■■■ground ■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3229")

    TalkEnd(0xFF)
    Return()

    # Function_13_2B82 end

    def Function_14_322D(): pass

    label("Function_14_322D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x101, 66000, -210, -500, 270)
    SetChrPos(0x102, 66000, -210, 500, 270)
    SetChrPos(0xF8, 67000, -210, -500, 270)
    SetChrPos(0xF9, 67000, -210, 500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(64530, -210, -40, 0)
    SetChrPos(0x0, 64530, -210, -40, 270)
    SetChrPos(0x1, 64530, -210, -40, 270)
    SetChrPos(0x2, 64530, -210, -40, 270)
    SetChrPos(0x3, 64530, -210, -40, 270)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_14_322D end

    def Function_15_332D(): pass

    label("Function_15_332D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(66500, -210, 0, 0)
    SetChrPos(0x101, 67000, -210, 500, 90)
    SetChrPos(0x102, 67000, -210, -500, 90)
    SetChrPos(0xF8, 66000, -210, 500, 90)
    SetChrPos(0xF9, 66000, -210, -500, 90)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_15_332D end

    def Function_16_33A5(): pass

    label("Function_16_33A5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x101, 500, -7360, 0, 180)
    SetChrPos(0x102, -500, -7360, 0, 180)
    SetChrPos(0xF8, 500, -7360, 1000, 180)
    SetChrPos(0xF9, -500, -7360, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(30, -7360, -1280, 0)
    SetChrPos(0x0, 30, -7360, -1280, 180)
    SetChrPos(0x1, 30, -7360, -1280, 180)
    SetChrPos(0x2, 30, -7360, -1280, 180)
    SetChrPos(0x3, 30, -7360, -1280, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_16_33A5 end

    def Function_17_34A5(): pass

    label("Function_17_34A5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -7360, 500, 0)
    SetChrPos(0x101, -500, -7360, 1000, 0)
    SetChrPos(0x102, 500, -7360, 1000, 0)
    SetChrPos(0xF8, -500, -7360, 0, 0)
    SetChrPos(0xF9, 500, -7360, 0, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_34A5 end

    def Function_18_351D(): pass

    label("Function_18_351D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -66000, -210, 500, 90)
    SetChrPos(0x102, -66000, -210, -500, 90)
    SetChrPos(0xF8, -67000, -210, 500, 90)
    SetChrPos(0xF9, -67000, -210, -500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 22)
    Call(0, 24)
    Fade(500)
    OP_6D(-64580, -210, 80, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -64580, -210, 80, 90)
    SetChrPos(0x1, -64580, -210, 80, 90)
    SetChrPos(0x2, -64580, -210, 80, 90)
    SetChrPos(0x3, -64580, -210, 80, 90)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_18_351D end

    def Function_19_362F(): pass

    label("Function_19_362F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-66500, -210, 0, 0)
    OP_6C(315000, 0)
    SetChrPos(0x101, -67000, -210, -500, 270)
    SetChrPos(0x102, -67000, -210, 500, 270)
    SetChrPos(0xF8, -66000, -210, -500, 270)
    SetChrPos(0xF9, -66000, -210, 500, 270)
    OP_0D()
    Call(0, 22)
    Call(0, 25)
    NewScene("ED6_DT21/C3601   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_19_362F end

    def Function_20_36B0(): pass

    label("Function_20_36B0")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, -210, -66000, 0)
    SetChrPos(0x102, 500, -210, -66000, 0)
    SetChrPos(0xF8, -500, -210, -67000, 0)
    SetChrPos(0xF9, 500, -210, -67000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 23)
    Call(0, 24)
    Fade(500)
    OP_6D(60, -210, -64319, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, 60, -210, -64319, 0)
    SetChrPos(0x1, 60, -210, -64319, 0)
    SetChrPos(0x2, 60, -210, -64319, 0)
    SetChrPos(0x3, 60, -210, -64319, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_20_36B0 end

    def Function_21_37C2(): pass

    label("Function_21_37C2")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -210, -66500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, -210, -67000, 180)
    SetChrPos(0x102, -500, -210, -67000, 180)
    SetChrPos(0xF8, 500, -210, -66000, 180)
    SetChrPos(0xF9, -500, -210, -66000, 180)
    OP_0D()
    Call(0, 23)
    Call(0, 25)
    NewScene("ED6_DT21/C3603   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_37C2 end

    def Function_22_3843(): pass

    label("Function_22_3843")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_22_3843 end

    def Function_23_3922(): pass

    label("Function_23_3922")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_23_3922 end

    def Function_24_3A01(): pass

    label("Function_24_3A01")


    def lambda_3A07():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3A07)

    def lambda_3A19():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3A19)

    def lambda_3A2B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3A2B)

    def lambda_3A3D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3A3D)
    Sleep(2500)
    Return()

    # Function_24_3A01 end

    def Function_25_3A4F(): pass

    label("Function_25_3A4F")


    def lambda_3A55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3A55)

    def lambda_3A67():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3A67)

    def lambda_3A79():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3A79)

    def lambda_3A8B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3A8B)
    Sleep(2000)
    Return()

    # Function_25_3A4F end

    SaveToFile()

Try(main)
