from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0702   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0702.x',
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
        'ED6_DT29/CH12590 ._CH',             # 00
        'ED6_DT29/CH12591 ._CH',             # 01
        'ED6_DT29/CH12600 ._CH',             # 02
        'ED6_DT29/CH12601 ._CH',             # 03
        'ED6_DT29/CH12610 ._CH',             # 04
        'ED6_DT29/CH12611 ._CH',             # 05
        'ED6_DT29/CH12620 ._CH',             # 06
        'ED6_DT29/CH12621 ._CH',             # 07
        'ED6_DT29/CH12630 ._CH',             # 08
        'ED6_DT29/CH12631 ._CH',             # 09
        'ED6_DT29/CH12640 ._CH',             # 0A
        'ED6_DT29/CH12641 ._CH',             # 0B
        'ED6_DT29/CH12651 ._CH',             # 0C
        'ED6_DT29/CH12651 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12590P._CP',             # 00
        'ED6_DT29/CH12591P._CP',             # 01
        'ED6_DT29/CH12600P._CP',             # 02
        'ED6_DT29/CH12601P._CP',             # 03
        'ED6_DT29/CH12610P._CP',             # 04
        'ED6_DT29/CH12611P._CP',             # 05
        'ED6_DT29/CH12620P._CP',             # 06
        'ED6_DT29/CH12621P._CP',             # 07
        'ED6_DT29/CH12630P._CP',             # 08
        'ED6_DT29/CH12631P._CP',             # 09
        'ED6_DT29/CH12640P._CP',             # 0A
        'ED6_DT29/CH12641P._CP',             # 0B
        'ED6_DT29/CH12651P._CP',             # 0C
        'ED6_DT29/CH12651P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 8170,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5920,
        Z                   = 400,
        Y                   = -46200,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8141,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6500,
        Z                   = 400,
        Y                   = -46310,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8142,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -41540,
        Z                   = -3600,
        Y                   = -16470,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8143,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31300,
        Z                   = 400,
        Y                   = -14460,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8144,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 43860,
        Z                   = 400,
        Y                   = -14570,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E9,
        Unknown_18          = 8145,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -5320,
        Z                   = 4000,
        Y                   = 40390,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3E8,
        Unknown_18          = 8146,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 5600,
        Z                   = 4000,
        Y                   = 51500,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3EA,
        Unknown_18          = 8147,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 100,
        TriggerZ            = 7170,
        TriggerY            = -670,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 7170,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 3600,
        TriggerY            = 45490,
        TriggerRange        = 1000,
        ActorX              = 90,
        ActorZ              = 3600,
        ActorY              = 46140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_27B",          # 01, 1
        "Function_2_35F",          # 02, 2
        "Function_3_375",          # 03, 3
        "Function_4_5D0",          # 04, 4
        "Function_5_712",          # 05, 5
        "Function_6_824",          # 06, 6
        "Function_7_8A5",          # 07, 7
        "Function_8_9A5",          # 08, 8
        "Function_9_A28",          # 09, 9
        "Function_10_B31",         # 0A, 10
        "Function_11_BB4",         # 0B, 11
        "Function_12_CC6",         # 0C, 12
        "Function_13_D47",         # 0D, 13
        "Function_14_E26",         # 0E, 14
        "Function_15_F05",         # 0F, 15
        "Function_16_F53",         # 10, 16
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_25E"),
        (101, "loc_265"),
        (102, "loc_26C"),
        (103, "loc_273"),
        (SWITCH_DEFAULT, "loc_27A"),
    )


    label("loc_25E")

    Event(0, 5)
    Jump("loc_27A")

    label("loc_265")

    Event(0, 7)
    Jump("loc_27A")

    label("loc_26C")

    Event(0, 9)
    Jump("loc_27A")

    label("loc_273")

    Event(0, 11)
    Jump("loc_27A")

    label("loc_27A")

    Return()

    # Function_0_246 end

    def Function_1_27B(): pass

    label("Function_1_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D")
    OP_6F(0x0, 0)
    Jump("loc_294")

    label("loc_28D")

    OP_6F(0x0, 60)

    label("loc_294")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6")
    OP_6F(0x1, 0)
    Jump("loc_2AD")

    label("loc_2A6")

    OP_6F(0x1, 60)

    label("loc_2AD")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 5)), scpexpr(EXPR_END)), "loc_2E1")
    SetChrFlags(0x9, 0x80)

    label("loc_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 6)), scpexpr(EXPR_END)), "loc_2ED")
    SetChrFlags(0xA, 0x80)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3F9, 7)), scpexpr(EXPR_END)), "loc_2F9")
    SetChrFlags(0xB, 0x80)

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 0)), scpexpr(EXPR_END)), "loc_305")
    SetChrFlags(0xC, 0x80)

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 1)), scpexpr(EXPR_END)), "loc_311")
    SetChrFlags(0xD, 0x80)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 2)), scpexpr(EXPR_END)), "loc_31D")
    SetChrFlags(0xE, 0x80)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3FA, 3)), scpexpr(EXPR_END)), "loc_329")
    SetChrFlags(0xF, 0x80)

    label("loc_329")

    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0x0, 0x6)
    OP_1B(0x1, 0x0, 0x8)
    OP_1B(0x2, 0x0, 0xA)
    OP_1B(0x3, 0x0, 0xC)
    Return()

    # Function_1_27B end

    def Function_2_35F(): pass

    label("Function_2_35F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_374")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_35F")

    label("loc_374")

    Return()

    # Function_2_35F end

    def Function_3_375(): pass

    label("Function_3_375")

    OP_EA(0x2, 0x0, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_510")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_3CC():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CC)

    def lambda_3E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3E7)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x3F0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_43A"),
        (2, "loc_44C"),
        (1, "loc_45C"),
        (SWITCH_DEFAULT, "loc_45F"),
    )


    label("loc_43A")

    OP_A2(0x1F08)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_45F")

    label("loc_44C")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_45C")

    OP_B4(0x0)
    Return()

    label("loc_45F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x164, 1)"), scpexpr(EXPR_END)), "loc_4AB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x64\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F07)
    Jump("loc_50D")

    label("loc_4AB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x64\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x64\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_50D")

    Jump("loc_5C2")

    label("loc_510")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05You open the chest and see something you didn't\x01",
            "notice the first time around. Without warning, the\x01",
            "chest slams itself shut. You cannot open it again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_375 end

    def Function_4_5D0(): pass

    label("Function_4_5D0")

    OP_EA(0x2, 0x19, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_641")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F09)
    Jump("loc_6A5")

    label("loc_641")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6A5")

    Jump("loc_704")

    label("loc_6A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Which of your party members blocks entrances\x01",
            "the best? AGATE!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_704")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5D0 end

    def Function_5_712(): pass

    label("Function_5_712")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, -80830, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -80330, 0)
    SetChrPos(0x102, 500, 250, -80330, 0)
    SetChrPos(0xF8, -500, 250, -81330, 0)
    SetChrPos(0xF9, 500, 250, -81330, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 13)
    Call(0, 15)
    Fade(500)
    OP_6D(70, -50, -76860, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, 70, -50, -76860, 0)
    SetChrPos(0x1, 70, -50, -76860, 0)
    SetChrPos(0x2, 70, -50, -76860, 0)
    SetChrPos(0x3, 70, -50, -76860, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_5_712 end

    def Function_6_824(): pass

    label("Function_6_824")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, -80830, 0)
    OP_6C(225000, 0)
    SetChrPos(0x101, -500, 250, -81330, 180)
    SetChrPos(0x102, 500, 250, -81330, 180)
    SetChrPos(0xF8, -500, 250, -80330, 180)
    SetChrPos(0xF9, 500, 250, -80330, 180)
    OP_0D()
    Call(0, 13)
    Call(0, 16)
    NewScene("ED6_DT21/C0701   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_824 end

    def Function_7_8A5(): pass

    label("Function_7_8A5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(50, 3850, 80830, 0)
    SetChrPos(0x101, 500, 3850, 80330, 180)
    SetChrPos(0x102, -500, 3850, 80330, 180)
    SetChrPos(0xF8, 500, 3850, 81330, 180)
    SetChrPos(0xF9, -500, 3850, 81330, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 14)
    Call(0, 15)
    Fade(500)
    OP_6D(20, 3870, 78170, 0)
    SetChrPos(0x0, 20, 3870, 78170, 180)
    SetChrPos(0x1, 20, 3870, 78170, 180)
    SetChrPos(0x2, 20, 3870, 78170, 180)
    SetChrPos(0x3, 20, 3870, 78170, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_7_8A5 end

    def Function_8_9A5(): pass

    label("Function_8_9A5")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(50, 3850, 80830, 0)
    SetChrPos(0x101, -500, 3850, 81330, 0)
    SetChrPos(0x102, 500, 3850, 81330, 0)
    SetChrPos(0xF8, -500, 3850, 80330, 0)
    SetChrPos(0xF9, 500, 3850, 80330, 0)
    OP_0D()
    Call(0, 14)
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C0703   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_9A5 end

    def Function_9_A28(): pass

    label("Function_9_A28")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(15500, 4250, 16000, 0)
    SetChrPos(0x101, 16000, 4250, 16500, 90)
    SetChrPos(0x102, 16000, 4250, 15500, 90)
    SetChrPos(0xF8, 15000, 4250, 16500, 90)
    SetChrPos(0xF9, 15000, 4250, 15500, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 14)
    Call(0, 15)
    Fade(500)
    OP_6D(18560, 4300, 16090, 0)
    SetChrPos(0x0, 18560, 4300, 16090, 90)
    SetChrPos(0x1, 18560, 4300, 16090, 90)
    SetChrPos(0x2, 18560, 4300, 16090, 90)
    SetChrPos(0x3, 18560, 4300, 16090, 90)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_9_A28 end

    def Function_10_B31(): pass

    label("Function_10_B31")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(15500, 4250, 16000, 0)
    SetChrPos(0x101, 15000, 4250, 15500, 270)
    SetChrPos(0x102, 15000, 4250, 16500, 270)
    SetChrPos(0xF8, 16000, 4250, 15500, 270)
    SetChrPos(0xF9, 16000, 4250, 16500, 270)
    OP_0D()
    Call(0, 14)
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C0703   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_10_B31 end

    def Function_11_BB4(): pass

    label("Function_11_BB4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-19500, -7350, -16000, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -20000, -7350, -16500, 270)
    SetChrPos(0x102, -20000, -7350, -15500, 270)
    SetChrPos(0xF8, -19000, -7350, -16500, 270)
    SetChrPos(0xF9, -19000, -7350, -15500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 14)
    Call(0, 15)
    Fade(500)
    OP_6D(-22350, -7300, -16129, 0)
    OP_6C(315000, 0)
    SetChrPos(0x0, -22350, -7300, -16129, 270)
    SetChrPos(0x1, -22350, -7300, -16129, 270)
    SetChrPos(0x2, -22350, -7300, -16129, 270)
    SetChrPos(0x3, -22350, -7300, -16129, 270)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_11_BB4 end

    def Function_12_CC6(): pass

    label("Function_12_CC6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-19500, -7350, -16000, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -19000, -7350, -15500, 90)
    SetChrPos(0x102, -19000, -7350, -16500, 90)
    SetChrPos(0xF8, -20000, -7350, -15500, 90)
    SetChrPos(0xF9, -20000, -7350, -16500, 90)
    OP_0D()
    Call(0, 14)
    Call(0, 16)
    NewScene("ED6_DT21/C0703   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_12_CC6 end

    def Function_13_D47(): pass

    label("Function_13_D47")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_13_D47 end

    def Function_14_E26(): pass

    label("Function_14_E26")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_14_E26 end

    def Function_15_F05(): pass

    label("Function_15_F05")


    def lambda_F0B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F0B)

    def lambda_F1D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F1D)

    def lambda_F2F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F2F)

    def lambda_F41():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F41)
    Sleep(2500)
    Return()

    # Function_15_F05 end

    def Function_16_F53(): pass

    label("Function_16_F53")


    def lambda_F59():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F59)

    def lambda_F6B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F6B)

    def lambda_F7D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F7D)

    def lambda_F8F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F8F)
    Sleep(2000)
    Return()

    # Function_16_F53 end

    SaveToFile()

Try(main)
