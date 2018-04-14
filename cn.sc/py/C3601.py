from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3601   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3601.x',
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

    DeclNpc(
        X                   = -20,
        Z                   = 1000,
        Y                   = -31930,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 18090,
        Z                   = 4400,
        Y                   = 14060,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7861,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 1910,
        Z                   = 4400,
        Y                   = -18170,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7862,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33620,
        Z                   = 400,
        Y                   = 17700,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7863,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 18030,
        TriggerZ            = 4400,
        TriggerY            = 7080,
        TriggerRange        = 1000,
        ActorX              = 18030,
        ActorZ              = 4400,
        ActorY              = 6460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12960,
        TriggerZ            = -3600,
        TriggerY            = 18020,
        TriggerRange        = 1000,
        ActorX              = 12260,
        ActorZ              = -3600,
        ActorY              = 18010,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = -50,
        TriggerY            = -31270,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = -50,
        ActorY              = -31930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6850,
        TriggerZ            = 400,
        TriggerY            = -31890,
        TriggerRange        = 1000,
        ActorX              = 7560,
        ActorZ              = 400,
        ActorY              = -31890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20,
        TriggerZ            = 400,
        TriggerY            = -38890,
        TriggerRange        = 1000,
        ActorX              = -20,
        ActorZ              = 400,
        ActorY              = -39510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6950,
        TriggerZ            = 400,
        TriggerY            = -31950,
        TriggerRange        = 1000,
        ActorX              = -7610,
        ActorZ              = 400,
        ActorY              = -31950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_29B",          # 01, 1
        "Function_2_36A",          # 02, 2
        "Function_3_380",          # 03, 3
        "Function_4_497",          # 04, 4
        "Function_5_5AE",          # 05, 5
        "Function_6_77E",          # 06, 6
        "Function_7_895",          # 07, 7
        "Function_8_9AC",          # 08, 8
        "Function_9_AC3",          # 09, 9
        "Function_10_BBE",         # 0A, 10
        "Function_11_C36",         # 0B, 11
        "Function_12_D31",         # 0C, 12
        "Function_13_DA9",         # 0D, 13
        "Function_14_EA4",         # 0E, 14
        "Function_15_F1C",         # 0F, 15
        "Function_16_1017",        # 10, 16
        "Function_17_108F",        # 11, 17
        "Function_18_1182",        # 12, 18
        "Function_19_1275",        # 13, 19
        "Function_20_12C3",        # 14, 20
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_27E"),
        (101, "loc_285"),
        (102, "loc_28C"),
        (103, "loc_293"),
        (SWITCH_DEFAULT, "loc_29A"),
    )


    label("loc_27E")

    Event(0, 9)
    Jump("loc_29A")

    label("loc_285")

    Event(0, 11)
    Jump("loc_29A")

    label("loc_28C")

    Event(0, 13)
    Jump("loc_29A")

    label("loc_293")

    Event(0, 15)
    Jump("loc_29A")

    label("loc_29A")

    Return()

    # Function_0_266 end

    def Function_1_29B(): pass

    label("Function_1_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_6F(0x0, 0)
    Jump("loc_2B4")

    label("loc_2AD")

    OP_6F(0x0, 60)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_6F(0x1, 0)
    Jump("loc_2CD")

    label("loc_2C6")

    OP_6F(0x1, 60)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF")
    OP_6F(0x2, 0)
    Jump("loc_2E6")

    label("loc_2DF")

    OP_6F(0x2, 60)

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F8")
    OP_6F(0x3, 0)
    Jump("loc_2FF")

    label("loc_2F8")

    OP_6F(0x3, 60)

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311")
    OP_6F(0x4, 0)
    Jump("loc_318")

    label("loc_311")

    OP_6F(0x4, 60)

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A")
    OP_6F(0x5, 0)
    Jump("loc_331")

    label("loc_32A")

    OP_6F(0x5, 60)

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 5)), scpexpr(EXPR_END)), "loc_33D")
    SetChrFlags(0x9, 0x80)

    label("loc_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 6)), scpexpr(EXPR_END)), "loc_349")
    SetChrFlags(0xA, 0x80)

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D6, 7)), scpexpr(EXPR_END)), "loc_355")
    SetChrFlags(0xB, 0x80)

    label("loc_355")

    OP_1B(0x0, 0x0, 0xA)
    OP_1B(0x1, 0x0, 0xC)
    OP_1B(0x2, 0x0, 0xE)
    OP_1B(0x3, 0x0, 0x10)
    Return()

    # Function_1_29B end

    def Function_2_36A(): pass

    label("Function_2_36A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_36A")

    label("loc_37F")

    Return()

    # Function_2_36A end

    def Function_3_380(): pass

    label("Function_3_380")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_458")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_3EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F30)
    Jump("loc_455")

    label("loc_3EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_455")

    Jump("loc_489")

    label("loc_458")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_489")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_380 end

    def Function_4_497(): pass

    label("Function_4_497")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_506")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F31)
    Jump("loc_56C")

    label("loc_506")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFB\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_56C")

    Jump("loc_5A0")

    label("loc_56F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_497 end

    def Function_5_5AE(): pass

    label("Function_5_5AE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_741")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_600():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_600)

    def lambda_61B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_61B)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #6
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x418, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_668"),
        (2, "loc_67A"),
        (1, "loc_68A"),
        (SWITCH_DEFAULT, "loc_68D"),
    )


    label("loc_668")

    OP_A2(0x1F33)
    OP_6F(0x2, 60)
    Sleep(500)
    Jump("loc_68D")

    label("loc_67A")

    OP_6F(0x2, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_68A")

    OP_B4(0x0)
    Return()

    label("loc_68D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x143, 1)"), scpexpr(EXPR_END)), "loc_6DC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\x43\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F32)
    Jump("loc_73E")

    label("loc_6DC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\x43\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x43\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_73E")

    Jump("loc_770")

    label("loc_741")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_770")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5AE end

    def Function_6_77E(): pass

    label("Function_6_77E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_7ED")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F34)
    Jump("loc_853")

    label("loc_7ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x01\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_853")

    Jump("loc_887")

    label("loc_856")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_887")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_77E end

    def Function_7_895(): pass

    label("Function_7_895")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_904")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xFA\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F35)
    Jump("loc_96A")

    label("loc_904")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "宝箱里装有\x1F\xFA\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFA\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_96A")

    Jump("loc_99E")

    label("loc_96D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_99E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_895 end

    def Function_8_9AC(): pass

    label("Function_8_9AC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A84")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_A1B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1F36)
    Jump("loc_A81")

    label("loc_A1B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_A81")

    Jump("loc_AB5")

    label("loc_A84")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AB5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_9AC end

    def Function_9_AC3(): pass

    label("Function_9_AC3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x101, 500, 190, 33780, 180)
    SetChrPos(0x102, -500, 190, 33780, 180)
    SetChrPos(0xF8, 500, 190, 34780, 180)
    SetChrPos(0xF9, -500, 190, 34780, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 17)
    Call(0, 19)
    Fade(500)
    OP_6D(-90, 190, 32189, 0)
    SetChrPos(0x0, -90, 190, 32189, 180)
    SetChrPos(0x1, -90, 190, 32189, 180)
    SetChrPos(0x2, -90, 190, 32189, 180)
    SetChrPos(0x3, -90, 190, 32189, 180)
    EventEnd(0x0)
    Return()

    # Function_9_AC3 end

    def Function_10_BBE(): pass

    label("Function_10_BBE")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 190, 34280, 0)
    SetChrPos(0x101, -500, 190, 34780, 0)
    SetChrPos(0x102, 500, 190, 34780, 0)
    SetChrPos(0xF8, -500, 190, 33780, 0)
    SetChrPos(0xF9, 500, 190, 33780, 0)
    OP_0D()
    Call(0, 17)
    Call(0, 20)
    NewScene("ED6_DT21/C3600   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_10_BBE end

    def Function_11_C36(): pass

    label("Function_11_C36")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x101, 34500, 190, 130, 180)
    SetChrPos(0x102, 33500, 190, 130, 180)
    SetChrPos(0xF8, 34500, 190, 1130, 180)
    SetChrPos(0xF9, 33500, 190, 1130, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(34000, 190, -1740, 0)
    SetChrPos(0x0, 34000, 190, -1740, 180)
    SetChrPos(0x1, 34000, 190, -1740, 180)
    SetChrPos(0x2, 34000, 190, -1740, 180)
    SetChrPos(0x3, 34000, 190, -1740, 180)
    EventEnd(0x0)
    Return()

    # Function_11_C36 end

    def Function_12_D31(): pass

    label("Function_12_D31")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(34000, 190, 630, 0)
    SetChrPos(0x101, 33500, 190, 1130, 0)
    SetChrPos(0x102, 34500, 190, 1130, 0)
    SetChrPos(0xF8, 33500, 190, 130, 0)
    SetChrPos(0xF9, 34500, 190, 130, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_D31 end

    def Function_13_DA9(): pass

    label("Function_13_DA9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 190, 500, 0)
    SetChrPos(0x101, 500, 190, 0, 180)
    SetChrPos(0x102, -500, 190, 0, 180)
    SetChrPos(0xF8, 500, 190, 1000, 180)
    SetChrPos(0xF9, -500, 190, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(130, 190, -1790, 0)
    SetChrPos(0x0, 130, 190, -1790, 180)
    SetChrPos(0x1, 130, 190, -1790, 180)
    SetChrPos(0x2, 130, 190, -1790, 180)
    SetChrPos(0x3, 130, 190, -1790, 180)
    EventEnd(0x0)
    Return()

    # Function_13_DA9 end

    def Function_14_EA4(): pass

    label("Function_14_EA4")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 190, 500, 0)
    SetChrPos(0x101, -500, 190, 1000, 0)
    SetChrPos(0x102, 500, 190, 1000, 0)
    SetChrPos(0xF8, -500, 190, 0, 0)
    SetChrPos(0xF9, 500, 190, 0, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_EA4 end

    def Function_15_F1C(): pass

    label("Function_15_F1C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x101, -33500, 190, 0, 180)
    SetChrPos(0x102, -34500, 190, 0, 180)
    SetChrPos(0xF8, -33500, 190, 1000, 180)
    SetChrPos(0xF9, -34500, 190, 1000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 19)
    Fade(500)
    OP_6D(-33710, 190, -1710, 0)
    SetChrPos(0x0, -33710, 190, -1710, 180)
    SetChrPos(0x1, -33710, 190, -1710, 180)
    SetChrPos(0x2, -33710, 190, -1710, 180)
    SetChrPos(0x3, -33710, 190, -1710, 180)
    EventEnd(0x0)
    Return()

    # Function_15_F1C end

    def Function_16_1017(): pass

    label("Function_16_1017")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-34000, 190, 500, 0)
    SetChrPos(0x101, -34500, 190, 1000, 0)
    SetChrPos(0x102, -33500, 190, 1000, 0)
    SetChrPos(0xF8, -34500, 190, 0, 0)
    SetChrPos(0xF9, -33500, 190, 0, 0)
    OP_0D()
    Call(0, 18)
    Call(0, 20)
    NewScene("ED6_DT21/C3602   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1017 end

    def Function_17_108F(): pass

    label("Function_17_108F")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_17_108F end

    def Function_18_1182(): pass

    label("Function_18_1182")

    LoadEffect(0x0, "map\\\\mp049_22.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_18_1182 end

    def Function_19_1275(): pass

    label("Function_19_1275")


    def lambda_127B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_127B)

    def lambda_128D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_128D)

    def lambda_129F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_129F)

    def lambda_12B1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12B1)
    Sleep(2500)
    Return()

    # Function_19_1275 end

    def Function_20_12C3(): pass

    label("Function_20_12C3")


    def lambda_12C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12C9)

    def lambda_12DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12DB)

    def lambda_12ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12ED)

    def lambda_12FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12FF)
    Sleep(2000)
    Return()

    # Function_20_12C3 end

    SaveToFile()

Try(main)
