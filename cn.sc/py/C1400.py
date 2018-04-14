from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1400   ._SN',
        MapName             = 'Bose',
        Location            = 'C1400.x',
        MapIndex            = 60,
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
        '',                                     # 9
        '维姆拉',                               # 10
        '基库',                                 # 11
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
        'ED6_DT09/CH11170 ._CH',             # 00
        'ED6_DT09/CH11171 ._CH',             # 01
        'ED6_DT09/CH11180 ._CH',             # 02
        'ED6_DT09/CH11181 ._CH',             # 03
        'ED6_DT09/CH11190 ._CH',             # 04
        'ED6_DT09/CH11191 ._CH',             # 05
        'ED6_DT09/CH10170 ._CH',             # 06
        'ED6_DT09/CH10171 ._CH',             # 07
        'ED6_DT09/CH10840 ._CH',             # 08
        'ED6_DT09/CH10841 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT07/CH01680 ._CH',             # 0B
        'ED6_DT07/CH02320 ._CH',             # 0C
        'ED6_DT26/CH20238 ._CH',             # 0D
        'ED6_DT06/CH20051 ._CH',             # 0E
        'ED6_DT26/CH20254 ._CH',             # 0F
        'ED6_DT07/CH01660 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH11170P._CP',             # 00
        'ED6_DT09/CH11171P._CP',             # 01
        'ED6_DT09/CH11180P._CP',             # 02
        'ED6_DT09/CH11181P._CP',             # 03
        'ED6_DT09/CH11190P._CP',             # 04
        'ED6_DT09/CH11191P._CP',             # 05
        'ED6_DT09/CH10170P._CP',             # 06
        'ED6_DT09/CH10171P._CP',             # 07
        'ED6_DT09/CH10840P._CP',             # 08
        'ED6_DT09/CH10841P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT07/CH01680P._CP',             # 0B
        'ED6_DT07/CH02320P._CP',             # 0C
        'ED6_DT26/CH20238P._CP',             # 0D
        'ED6_DT06/CH20051P._CP',             # 0E
        'ED6_DT26/CH20254P._CP',             # 0F
        'ED6_DT07/CH01660P._CP',             # 10
    )

    DeclNpc(
        X                   = -42410,
        Z                   = 4019,
        Y                   = 103940,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -68750,
        Z                   = 50,
        Y                   = 92910,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -112800,
        Z                   = -50,
        Y                   = 104070,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86000,
        Z                   = 2020,
        Y                   = 104050,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -91980,
        Z                   = 2080,
        Y                   = 122080,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78470,
        Z                   = 4059,
        Y                   = 133110,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -61710,
        Z                   = 4050,
        Y                   = 112490,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46460,
        Z                   = 4080,
        Y                   = 83320,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xB8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -42410,
        Y                   = 3500,
        Z                   = 103940,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -43500,
        Y                   = 3500,
        Z                   = 104740,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -67400,
        Y                   = 3000,
        Z                   = 184200,
        Range               = -60300,
        Unknown_10          = 0x1770,
        Unknown_14          = 0x2D2A8,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )


    DeclActor(
        TriggerX            = -78820,
        TriggerZ            = 90,
        TriggerY            = 98230,
        TriggerRange        = 1000,
        ActorX              = -78790,
        ActorZ              = 1590,
        ActorY              = 97650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -85490,
        TriggerZ            = -30,
        TriggerY            = 115790,
        TriggerRange        = 1000,
        ActorX              = -85380,
        ActorZ              = 1200,
        ActorY              = 115700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_344",          # 01, 1
        "Function_2_3DA",          # 02, 2
        "Function_3_3F0",          # 03, 3
        "Function_4_407",          # 04, 4
        "Function_5_4AC",          # 05, 5
        "Function_6_5C3",          # 06, 6
        "Function_7_8CB",          # 07, 7
        "Function_8_1314",         # 08, 8
        "Function_9_1564",         # 09, 9
        "Function_10_18BC",        # 0A, 10
        "Function_11_2516",        # 0B, 11
        "Function_12_2615",        # 0C, 12
        "Function_13_269F",        # 0D, 13
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_305")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_END)), "loc_322")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -42100, 4000, 104960, 135)

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_END)), "loc_32E")
    SetChrFlags(0x9, 0x80)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_343")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_343")

    Return()

    # Function_0_2FE end

    def Function_1_344(): pass

    label("Function_1_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356")
    OP_6F(0x2, 0)
    Jump("loc_35D")

    label("loc_356")

    OP_6F(0x2, 60)

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    OP_6F(0x6, 0)
    Jump("loc_376")

    label("loc_36F")

    OP_6F(0x6, 60)

    label("loc_376")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x4)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B7")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_END)), "loc_3C8")
    OP_72(0x1, 0x4)
    OP_71(0x3, 0x4)

    label("loc_3C8")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_344 end

    def Function_2_3DA(): pass

    label("Function_2_3DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3DA")

    label("loc_3EF")

    Return()

    # Function_2_3DA end

    def Function_3_3F0(): pass

    label("Function_3_3F0")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x9,
        "◆没有台词\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_3F0 end

    def Function_4_407(): pass

    label("Function_4_407")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_480")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    AddSepith(0x1, 0xC8)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x00得到了\x07\x02#57I水之耀晶片×２００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B14)
    Jump("loc_49A")

    label("loc_480")


    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_49A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_407 end

    def Function_5_4AC(): pass

    label("Function_5_4AC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_584")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2D9, 1)"), scpexpr(EXPR_END)), "loc_51B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xD9\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B15)
    Jump("loc_581")

    label("loc_51B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xD9\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD9\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_581")

    Jump("loc_5B5")

    label("loc_584")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5B5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_4AC end

    def Function_6_5C3(): pass

    label("Function_6_5C3")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62C"),
        (1, "loc_860"),
        (SWITCH_DEFAULT, "loc_8C8"),
    )


    label("loc_62C")

    Battle(0xBB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_64D"),
        (2, "loc_7E0"),
        (1, "loc_858"),
        (SWITCH_DEFAULT, "loc_85D"),
    )


    label("loc_64D")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F4")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【◇已经消灭了古罗尼山路和琥珀之塔的通缉魔兽】\x01",      # 0
            "【◇什么也没有变更】\x01",                                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6DF"),
        (SWITCH_DEFAULT, "loc_6F4"),
    )


    label("loc_6DF")

    OP_A2(0x1A0E)
    OP_A2(0x1A0F)
    OP_28(0xB1, 0x1, 0x1)
    OP_28(0xB3, 0x1, 0x1)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_706")
    Call(0, 7)
    Jump("loc_7DD")

    label("loc_706")

    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40990, 3930, 102060, 315)
    SetChrPos(0x1, -40990, 3930, 102060, 315)
    SetChrPos(0x2, -40990, 3930, 102060, 315)
    SetChrPos(0x3, -40990, 3930, 102060, 315)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05消灭了迷雾峡谷的通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x80)
    OP_28(0x93, 0x1, 0x100)
    OP_28(0x93, 0x1, 0x200)
    Sleep(400)

    label("loc_7DD")

    Jump("loc_85D")

    label("loc_7E0")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40390, 3880, 100330, 315)
    SetChrPos(0x1, -40390, 3880, 100330, 315)
    SetChrPos(0x2, -40390, 3880, 100330, 315)
    SetChrPos(0x3, -40390, 3880, 100330, 315)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_85D")

    label("loc_858")

    OP_B4(0x0)
    Jump("loc_85D")

    label("loc_85D")

    Jump("loc_8C8")

    label("loc_860")

    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x0, -40390, 3880, 100330, 315)
    SetChrPos(0x1, -40390, 3880, 100330, 315)
    SetChrPos(0x2, -40390, 3880, 100330, 315)
    SetChrPos(0x3, -40390, 3880, 100330, 315)
    OP_69(0x0, 0x0)
    OP_0D()
    Jump("loc_8C8")

    label("loc_8C8")

    EventEnd(0x0)
    Return()

    # Function_6_5C3 end

    def Function_7_8CB(): pass

    label("Function_7_8CB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DE")
    Call(0, 11)

    label("loc_8DE")

    OP_6D(-42350, 4059, 103640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(359000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -41720, 3990, 104460, 225)
    SetChrPos(0x106, -43170, 4059, 104220, 135)
    SetChrPos(0xF8, -41440, 4030, 102690, 315)
    SetChrPos(0xF9, -42900, 4070, 102590, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #8
        0x101,
        (
            "#1007F哈～总算是解决了啊。\x02\x03",

            "#1002F不过……\x01",
            "这些魔兽的样子似乎很奇怪啊？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x18\x07\x05是哪里和平时不同了呢？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【魔兽变强了】\x01",        # 0
            "【魔兽变胆怯了】\x01",      # 1
            "【魔兽非常兴奋】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A6C"),
        (1, "loc_C45"),
        (2, "loc_DFA"),
        (SWITCH_DEFAULT, "loc_FAF"),
    )


    label("loc_A6C")

    OP_2B(0x93, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AE1")

    ChrTalk(    #10
        0x108,
        (
            "#072F那也没错……\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3C")

    label("loc_AE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B57")

    ChrTalk(    #11
        0x103,
        (
            "#022F那也说的没错……\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3C")

    label("loc_B57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCF")

    ChrTalk(    #12
        0x104,
        (
            "#032F嗯，那也说的不错，\x01",
            "不过更明显的是它们的性情变了哦。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3C")

    label("loc_BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3C")

    ChrTalk(    #13
        0x105,
        (
            "#043F那样说也对，\x01",
            "不过更明显的是它们的性情变了。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3C")

    OP_28(0x93, 0x1, 0x400)
    Jump("loc_FAF")

    label("loc_C45")

    OP_2B(0x93, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB6")

    ChrTalk(    #14
        0x108,
        (
            "#072F啊啊～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D20")

    ChrTalk(    #15
        0x103,
        (
            "#022F哎～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_D20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D8A")

    ChrTalk(    #16
        0x104,
        (
            "#032F嗯，不管什么样的魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF1")

    label("loc_D8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF1")

    ChrTalk(    #17
        0x105,
        (
            "#042F是啊，不管什么样的魔兽\x01",
            "也都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF1")

    OP_28(0x93, 0x1, 0x1000)
    Jump("loc_FAF")

    label("loc_DFA")

    OP_2B(0x93, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E6B")

    ChrTalk(    #18
        0x108,
        (
            "#072F啊啊～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA6")

    label("loc_E6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED5")

    ChrTalk(    #19
        0x103,
        (
            "#022F哎～不管什么样的魔兽\x01",
            "都变得很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA6")

    label("loc_ED5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3F")

    ChrTalk(    #20
        0x104,
        (
            "#032F嗯，不管什么样的魔兽\x01",
            "都好像很奇怪啊。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA6")

    label("loc_F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FA6")

    ChrTalk(    #21
        0x105,
        (
            "#042F是啊，不管什么样的魔兽\x01",
            "也都很奇怪呢。\x02\x03",

            "变得异常地凶暴，\x01",
            "陷入了某种恐慌之中……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FA6")

    OP_28(0x93, 0x1, 0x800)
    Jump("loc_FAF")

    label("loc_FAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF7")

    ChrTalk(    #22
        0x107,
        (
            "#065F我、我也\x01",
            "有那种感觉。\x02\x03",

            "#561F好、好可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CC")

    label("loc_FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_103E")

    ChrTalk(    #23
        0x105,
        (
            "#043F我也……\x01",
            "有那种感觉啊。\x02\x03",

            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CC")

    label("loc_103E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(    #24
        0x104,
        (
            "#032F我也有\x01",
            "同样的感觉呢。\x02\x03",

            "嗯，到底是为什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10CC")

    label("loc_1085")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10CC")

    ChrTalk(    #25
        0x103,
        (
            "#026F我也有同感啊。\x02\x03",

            "#522F嗯……\x01",
            "究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CC")


    ChrTalk(    #26
        0x106,
        "#057F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F嗯？　怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#555F啊，没什么……\x02\x03",

            "或许这是\x01",
            "某种前兆也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1020F前兆……\x01",
            "难道是『结社』！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x106,
        (
            "#552F这就不得而知了……\x01",
            "不过以前也发生过类似的状况。\x02\x03",

            "魔兽突然就变得\x01",
            "仓惶不安…\x02\x03",

            "之后……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004F？？？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #32
        0x107,
        "#063F阿加特哥哥……？\x02",
    )

    CloseMessageWindow()

    label("loc_1218")


    ChrTalk(    #33
        0x106,
        (
            "#053F算了，目前就这样吧。\x02\x03",

            "#057F不管怎么说，动物的直觉\x01",
            "有时候比人还要更加敏锐。\x02\x03",

            "我们也必须准备应付\x01",
            "随时可能出现的特殊情况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1002F嗯……明白了。\x02\x03",

            "那么…\x01",
            "我们暂时先返回协会吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        "#050F啊啊～就这样办吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A10)
    OP_28(0xB2, 0x1, 0x1)
    OP_28(0x93, 0x2, 0x80)
    OP_28(0x93, 0x1, 0x100)
    OP_28(0x93, 0x1, 0x200)
    OP_28(0x93, 0x1, 0x2000)
    Return()

    # Function_7_8CB end

    def Function_8_1314(): pass

    label("Function_8_1314")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_132B")
    Call(0, 12)
    Call(0, 13)

    label("loc_132B")

    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(-69550, -70, 106980, 0)
    OP_67(0, 13560, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(9000, 0)
    OP_6E(342, 0)
    SetChrPos(0x101, -43050, 40, 15070, 0)
    SetChrPos(0x106, -44190, -50, 15060, 0)
    SetChrPos(0x107, -44150, -20, 13590, 0)
    SetChrPos(0xF9, -43040, 50, 13500, 0)

    def lambda_13D5():
        OP_6D(-44930, -70, 26000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13D5)

    def lambda_13ED():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13ED)
    OP_C8(0x200, 0x46, "C_PLAC13._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(5000)

    def lambda_1421():
        OP_8E(0xFE, 0xFFFF58BC, 0x50, 0x602C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1421)
    Sleep(200)

    def lambda_1441():
        OP_8E(0xFE, 0xFFFF53E4, 0x46, 0x5FFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1441)

    def lambda_145C():
        OP_8E(0xFE, 0xFFFF5510, 0xFFFFFFA6, 0x5AAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_145C)
    Sleep(200)

    def lambda_147C():
        OP_8E(0xFE, 0xFFFF59CA, 0x14, 0x5B2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_147C)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Fade(1000)
    OP_6D(-43060, 0, 25330, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x2)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1006F#2P那么……\x02\x03",

            "先去峡谷东侧的\x01",
            "山中小屋吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        "#050F#5P啊，快去吧。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_A2(0x1A25)
    EventEnd(0x0)
    Return()

    # Function_8_1314 end

    def Function_9_1564(): pass

    label("Function_9_1564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1571")
    Return()

    label("loc_1571")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1588")
    Call(0, 12)
    Call(0, 13)

    label("loc_1588")

    Fade(1000)
    OP_6D(-41580, 3920, 104490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(27000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -41200, 4019, 103610, 315)
    SetChrPos(0x106, -42230, 4090, 103100, 315)
    SetChrPos(0x107, -41860, 4010, 101920, 315)
    SetChrPos(0xF9, -40840, 3940, 102310, 315)

    def lambda_1614():

        label("loc_1614")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1614")

    QueueWorkItem2(0x101, 1, lambda_1614)

    def lambda_1625():

        label("loc_1625")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1625")

    QueueWorkItem2(0x106, 1, lambda_1625)

    def lambda_1636():

        label("loc_1636")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1636")

    QueueWorkItem2(0x107, 1, lambda_1636)

    def lambda_1647():

        label("loc_1647")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_1647")

    QueueWorkItem2(0xF9, 1, lambda_1647)
    OP_8C(0x9, 180, 0)
    OP_4A(0x9, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0x9,
        (
            "#5P……你们\x01",
            "总算是来到这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        "#052F大叔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1011F是不是…渡过\x01",
            "那座桥的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "#5P嗯，一直向前走\x01",
            "就可以看到一座巨大的岩山。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#5P那里面是中空的，\x01",
            "你们只要一直往内部前进\x01",
            "就可以爬到最上层了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#5P龙应该就栖息在那里。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1006F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#051F谢谢你了，大叔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "#5P那么……\x01",
            "我这就要回小屋去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "#5P对了，岩山的空洞中应该\x01",
            "有很多危险的魔兽在游荡着，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#5P如果觉得危险的话\x01",
            "最好还是马上回头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        "#5P我的小屋随时可以供你们休息。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1018F嗯，谢谢您了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x106,
        "#051F我们会小心的。\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFF568C, 0x1018, 0x19172, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF7036, 0xF6E, 0x17016, 0x7D0, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)
    Sleep(1000)
    OP_A2(0x1A27)
    OP_28(0x96, 0x1, 0x100)
    OP_28(0x96, 0x1, 0x200)
    EventEnd(0x0)
    Return()

    # Function_9_1564 end

    def Function_10_18BC(): pass

    label("Function_10_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18C9")
    Return()

    label("loc_18C9")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18E0")
    Call(0, 12)
    Call(0, 13)

    label("loc_18E0")

    Fade(1000)
    OP_6D(-63540, 4100, 187850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(34000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -64340, 4050, 187170, 0)
    SetChrPos(0x106, -63060, 4019, 187180, 0)
    SetChrPos(0x107, -62880, 4000, 186090, 0)
    SetChrPos(0xF9, -64400, 4090, 185850, 0)
    OP_0D()

    ChrTalk(    #52
        0x101,
        "#1002F这里就是巨龙栖息的岩山……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x107,
        "#062F呜啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        (
            "#051F嘿，看来要拿出\x01",
            "全部的干劲了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A1F")

    ChrTalk(    #55
        0x103,
        (
            "#023F#6P先等一下。\x02\x03",

            "#020F现在先和『埃尔赛尤』\x01",
            "进行联络比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B37")

    label("loc_1A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A7C")

    ChrTalk(    #56
        0x105,
        (
            "#044F#6P啊，请等一下。\x02\x03",

            "#040F现在还是先和『埃尔赛尤』\x01",
            "联络一下比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B37")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ADD")

    ChrTalk(    #57
        0x104,
        (
            "#035F#6P喂，等一下。\x02\x03",

            "#030F我想现在还是先和『埃尔赛尤』\x01",
            "进行联络比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B37")

    label("loc_1ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B37")

    ChrTalk(    #58
        0x108,
        (
            "#073F#6P啊，等一下。\x02\x03",

            "#070F现在还是先和『埃尔赛尤』\x01",
            "联络一下比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B37")

    TurnDirection(0x101, 0xF9, 400)

    ChrTalk(    #59
        0x101,
        "#1006F#5P嗯，说的也对。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3F")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #60
        "\x07\x05艾丝蒂尔把当前的情况记录了下来。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_1BB5():

        label("loc_1BB5")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1BB5")

    QueueWorkItem2(0x106, 1, lambda_1BB5)

    def lambda_1BC6():

        label("loc_1BC6")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1BC6")

    QueueWorkItem2(0x107, 1, lambda_1BC6)

    def lambda_1BD7():

        label("loc_1BD7")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1BD7")

    QueueWorkItem2(0xF9, 1, lambda_1BD7)

    def lambda_1BE8():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BE8)

    def lambda_1C00():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C00)
    OP_8E(0x101, 0xFFFEFE80, 0xFDB, 0x2D9BA, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_1C3D():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C3D)

    def lambda_1C4B():
        OP_8C(0xF9, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1C4B)
    Sleep(300)

    ChrTalk(    #61
        0x101,
        "#1005F#5P#3S基库！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_22(0x197, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-68540, 5590, 186890, 1500)
    SetChrPos(0xA, -78030, 10000, 185300, 0)
    SetChrChipByIndex(0xA, 12)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    OP_43(0xA, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x1)
    Sleep(500)

    def lambda_1CC7():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1CC7)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_1CE4():
        OP_8E(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1CE4)
    Sleep(2400)
    SetChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 15)
    OP_8C(0xA, 180, 100)
    OP_8F(0xA, 0xFFFEFDD6, 0x1068, 0x2DA8C, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    OP_8C(0x101, 225, 0)
    SetChrChipByIndex(0x101, 13)
    SetChrSubChip(0x101, 5)
    OP_0D()
    Sleep(300)

    ChrTalk(    #62
        0xA,
        "#311F#6P啾啾⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1016F#5P啊哈哈，你果然\x01",
            "一叫就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x107,
        "#061F基库，谢谢啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        (
            "#551F呼～这只鸟还是\x01",
            "那样让人感到不可思议。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        "\x07\x05艾丝蒂尔把纸条绑在了基库的脚上。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #67
        0x101,
        (
            "#1006F#5P那么，基库。\x02\x03",

            "可以拜托你跟『埃尔赛尤』\x01",
            "取得联络吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "#310F#6P啾！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0xA, -66090, 4200, 187020, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)

    def lambda_1E9F():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E9F)
    OP_8F(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x7D0, 0x0)
    OP_8C(0xA, 270, 100)
    SetChrChipByIndex(0xA, 12)

    def lambda_1ECD():
        OP_6D(-68540, 5590, 186890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1ECD)

    def lambda_1EE5():
        OP_8E(0xA, 0xFFFECD84, 0x2710, 0x2D3D4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_1EE5)
    Sleep(100)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x80)

    def lambda_1F19():
        OP_6D(-63540, 4100, 187850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F19)
    Sleep(1000)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x2)
    Jump("loc_232F")

    label("loc_1F3F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        "\x07\x05科洛丝把当前的情况记录了下来。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_1F89():

        label("loc_1F89")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1F89")

    QueueWorkItem2(0x101, 1, lambda_1F89)

    def lambda_1F9A():

        label("loc_1F9A")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1F9A")

    QueueWorkItem2(0x106, 1, lambda_1F9A)

    def lambda_1FAB():

        label("loc_1FAB")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1FAB")

    QueueWorkItem2(0x107, 1, lambda_1FAB)

    def lambda_1FBC():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FBC)

    def lambda_1FD4():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FD4)
    OP_8E(0x105, 0xFFFEFE80, 0xFDB, 0x2D9BA, 0x7D0, 0x0)

    def lambda_2000():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2000)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x1)
    OP_44(0x106, 0x1)
    OP_44(0x107, 0x1)

    def lambda_201F():
        OP_8C(0x107, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_201F)

    def lambda_202D():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_202D)
    Sleep(300)

    ChrTalk(    #70
        0x105,
        "#042F#5P#3S基库，过来！\x02",
    )

    CloseMessageWindow()
    OP_22(0x197, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-68540, 5590, 186890, 1500)
    SetChrPos(0xA, -78030, 10000, 185300, 0)
    SetChrChipByIndex(0xA, 12)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    OP_43(0xA, 0x0, 0x0, 0x2)
    ClearChrFlags(0xA, 0x1)
    Sleep(500)

    def lambda_20A9():
        OP_6D(-65560, 4059, 187340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20A9)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_20C6():
        OP_8E(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_20C6)
    Sleep(2400)
    SetChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    SetChrChipByIndex(0xA, 15)

    def lambda_20F5():
        OP_8C(0xA, 180, 100)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_20F5)

    def lambda_2103():
        OP_8C(0x105, 225, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2103)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 14)
    SetChrSubChip(0x105, 2)
    WaitChrThread(0xA, 0x3)
    OP_8F(0xA, 0xFFFEFDD6, 0x1068, 0x2DA8C, 0x3E8, 0x0)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x105, 14)
    SetChrSubChip(0x105, 0)
    OP_0D()

    ChrTalk(    #71
        0xA,
        "#311F#6P啾啾⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        "#048F#5P呵呵，辛苦你啦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1001F谢谢了，基库！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x106,
        (
            "#551F呼～这只鸟还是\x01",
            "那样让人感到不可思议。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #75
        "\x07\x05科洛丝把纸条绑在了基库的脚上。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #76
        0x105,
        (
            "#042F#5P那么，基库。\x02\x03",

            "和『埃尔赛尤』的联络\x01",
            "一切就拜托你了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "#310F#6P啾！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0x105, 65535)
    ClearChrFlags(0x105, 0x20)
    SetChrPos(0xA, -66090, 4200, 187020, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 15)

    def lambda_2292():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2292)
    OP_8F(0xA, 0xFFFEFC64, 0x1770, 0x2DBA4, 0x7D0, 0x0)
    OP_8C(0xA, 270, 100)
    SetChrChipByIndex(0xA, 12)

    def lambda_22C0():
        OP_6D(-68540, 5590, 186890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22C0)

    def lambda_22D8():
        OP_8E(0xA, 0xFFFECD84, 0x2710, 0x2D3D4, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_22D8)
    Sleep(100)
    ClearChrFlags(0xA, 0x1)
    WaitChrThread(0xA, 0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x80)

    def lambda_230C():
        OP_6D(-63540, 4100, 187850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_230C)
    Sleep(1000)
    OP_8C(0x105, 90, 400)
    WaitChrThread(0x101, 0x2)

    label("loc_232F")

    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_236D")

    ChrTalk(    #78
        0x105,
        (
            "#047F那么……\x01",
            "大家已经准备好了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_236D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A2")

    ChrTalk(    #79
        0x103,
        (
            "#026F那么……\x01",
            "已经准备好了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_23A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23DD")

    ChrTalk(    #80
        0x104,
        (
            "#035F那么……\x01",
            "想必大家已经准备好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2415")

    label("loc_23DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2415")

    ChrTalk(    #81
        0x108,
        (
            "#074F那么……\x01",
            "想必大家已经准备好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2415")


    ChrTalk(    #82
        0x101,
        (
            "#1002F#5P嗯……\x01",
            "打起精神来，继续前进吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        "#062F#2P嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#054F#2P噢噢！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-63660, 4000, 183220, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -63660, 4000, 183220, 0)
    SetChrPos(0x1, -63660, 4000, 183220, 0)
    SetChrPos(0x2, -63660, 4000, 183220, 0)
    SetChrPos(0x3, -63660, 4000, 183220, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x1A28)
    OP_28(0x96, 0x1, 0x400)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_18BC end

    def Function_11_2516(): pass

    label("Function_11_2516")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25CD"),
        (1, "loc_25D3"),
        (SWITCH_DEFAULT, "loc_25D9"),
    )


    label("loc_25CD")

    OP_A2(0x1200)
    Jump("loc_25D9")

    label("loc_25D3")

    OP_A2(0x1201)
    Jump("loc_25D9")

    label("loc_25D9")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_2516 end

    def Function_12_2615(): pass

    label("Function_12_2615")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2692"),
        (1, "loc_2698"),
        (SWITCH_DEFAULT, "loc_269E"),
    )


    label("loc_2692")

    OP_A2(0x1200)
    Jump("loc_269E")

    label("loc_2698")

    OP_A2(0x1201)
    Jump("loc_269E")

    label("loc_269E")

    Return()

    # Function_12_2615 end

    def Function_13_269F(): pass

    label("Function_13_269F")

    ClearMapFlags(0x1)
    OP_6D(97010, 0, 95840, 0)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_13_269F end

    SaveToFile()

Try(main)
