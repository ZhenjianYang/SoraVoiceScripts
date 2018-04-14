from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2401   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2401.x',
        MapIndex            = 103,
        MapDefaultBGM       = "ed60029",
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
            'ED6_DT21/SUB000  ._SN',
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
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT09/CH10520 ._CH',             # 02
        'ED6_DT09/CH10521 ._CH',             # 03
        'ED6_DT09/CH10340 ._CH',             # 04
        'ED6_DT09/CH10341 ._CH',             # 05
        'ED6_DT09/CH11040 ._CH',             # 06
        'ED6_DT09/CH11041 ._CH',             # 07
        'ED6_DT09/CH11070 ._CH',             # 08
        'ED6_DT09/CH11071 ._CH',             # 09
        'ED6_DT09/CH11080 ._CH',             # 0A
        'ED6_DT09/CH11081 ._CH',             # 0B
        'ED6_DT29/CH13010 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT09/CH10520P._CP',             # 02
        'ED6_DT09/CH10521P._CP',             # 03
        'ED6_DT09/CH10340P._CP',             # 04
        'ED6_DT09/CH10341P._CP',             # 05
        'ED6_DT09/CH11040P._CP',             # 06
        'ED6_DT09/CH11041P._CP',             # 07
        'ED6_DT09/CH11070P._CP',             # 08
        'ED6_DT09/CH11071P._CP',             # 09
        'ED6_DT09/CH11080P._CP',             # 0A
        'ED6_DT09/CH11081P._CP',             # 0B
        'ED6_DT29/CH13010P._CP',             # 0C
    )

    DeclNpc(
        X                   = -3580,
        Z                   = -30,
        Y                   = 67370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -12120,
        Z                   = 240,
        Y                   = 43840,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 6530,
        Z                   = 270,
        Y                   = 30240,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -6700,
        Y                   = -2000,
        Z                   = 8900,
        Range               = 8200,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x26AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -21190,
        Y                   = -3010,
        Z                   = 80310,
        Range               = 20100,
        Unknown_10          = 0xBC2,
        Unknown_14          = 0x148F2,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -5300,
        Y                   = 3000,
        Z                   = 95360,
        Range               = 1100,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x178F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = -3580,
        Y                   = -500,
        Z                   = 67370,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 10960,
        TriggerZ            = -50,
        TriggerY            = 86080,
        TriggerRange        = 1000,
        ActorX              = 11490,
        ActorZ              = 1000,
        ActorY              = 86480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20E",          # 00, 0
        "Function_1_2A7",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_49D",          # 03, 3
        "Function_4_658",          # 04, 4
        "Function_5_8CE",          # 05, 5
        "Function_6_99D",          # 06, 6
        "Function_7_CA4",          # 07, 7
        "Function_8_D2B",          # 08, 8
        "Function_9_DB8",          # 09, 9
        "Function_10_E9C",         # 0A, 10
        "Function_11_F21",         # 0B, 11
        "Function_12_FA6",         # 0C, 12
        "Function_13_102B",        # 0D, 13
        "Function_14_10B0",        # 0E, 14
        "Function_15_1237",        # 0F, 15
        "Function_16_1298",        # 10, 16
        "Function_17_12F9",        # 11, 17
        "Function_18_135A",        # 12, 18
    )


    def Function_0_20E(): pass

    label("Function_0_20E")

    OP_A3(0x1350)
    OP_A3(0x1351)
    OP_A3(0x1352)
    OP_A3(0x1353)
    OP_A3(0x1354)
    OP_A3(0x1355)
    OP_A3(0x1356)
    OP_A3(0x1357)
    OP_A3(0x1358)
    OP_A3(0x1359)
    OP_A3(0x1E99)
    OP_A3(0x1E9A)
    OP_A3(0x1E9B)
    OP_A3(0x1E9C)
    OP_A3(0x1E9D)
    OP_A3(0x1E9E)
    OP_A3(0x1E9F)
    OP_A3(0x1EA0)
    OP_A3(0x1EA1)
    OP_A3(0x1EA2)
    OP_A3(0x1EA3)
    OP_A3(0x1EA4)
    OP_A3(0x1EA5)
    OP_A3(0x1EA6)
    OP_A3(0x1EA7)
    OP_A3(0x1EA8)
    OP_A3(0x1EA9)
    OP_A3(0x1EAA)
    OP_A3(0x1EAB)
    OP_A3(0x1EAC)
    OP_A3(0x1EAD)
    OP_A3(0x1EAE)
    OP_A3(0x1EAF)
    OP_A3(0x1EB0)
    OP_A3(0x1EB1)
    OP_A3(0x1EB2)
    OP_A3(0x1EB3)
    OP_A3(0x1EB4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_296")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_2A6")

    label("loc_296")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    Event(0, 14)

    label("loc_2A6")

    Return()

    # Function_0_20E end

    def Function_1_2A7(): pass

    label("Function_1_2A7")

    OP_16(0x2, 0xFA0, 0xFFFE0430, 0xFFFECB68, 0x230024)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D3")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5")
    OP_6F(0x0, 0)
    Jump("loc_2EC")

    label("loc_2E5")

    OP_6F(0x0, 60)

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FB")
    Jump("loc_34B")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_34B")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -2070, 6000, 96100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_34B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_364")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_36A")

    label("loc_364")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_36A")

    OP_B2(0x0, 0x3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x3, 0x80)

    label("loc_385")

    Return()

    # Function_1_2A7 end

    def Function_2_386(): pass

    label("Function_2_386")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C8, 1)"), scpexpr(EXPR_END)), "loc_3F5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xC8\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x130F)
    Jump("loc_45B")

    label("loc_3F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xC8\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xC8\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_45B")

    Jump("loc_48F")

    label("loc_45E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_48F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_386 end

    def Function_3_49D(): pass

    label("Function_3_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 3)), scpexpr(EXPR_END)), "loc_4A5")
    Return()

    label("loc_4A5")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #3
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
        (1, "loc_58A"),
        (SWITCH_DEFAULT, "loc_5AD"),
    )


    label("loc_58A")

    Fade(500)
    OP_89(0x0, -3140, -60, 60730, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_5AD")

    Battle(0xEF2, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -3140, -60, 60730, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_5E6"),
        (1, "loc_5E9"),
        (SWITCH_DEFAULT, "loc_5EC"),
    )


    label("loc_5E6")

    EventEnd(0x0)
    Return()

    label("loc_5E9")

    OP_B4(0x0)
    Return()

    label("loc_5EC")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x3, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20FB)
    OP_28(0xBA, 0x4, 0x10)
    OP_28(0xBA, 0x4, 0x2)
    OP_28(0xBA, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_49D end

    def Function_4_658(): pass

    label("Function_4_658")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66F")
    Call(0, 7)
    Call(0, 8)

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")
    OP_6D(-1330, 20, 82650, 0)
    OP_67(0, 12040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(341, 0)
    SetChrPos(0x101, 280, -30, 13880, 0)
    SetChrPos(0x102, -1200, -10, 13760, 0)
    SetChrPos(0x103, 280, 0, 12600, 0)
    SetChrPos(0xF9, -1140, 20, 12330, 0)

    def lambda_6FE():
        OP_6D(-450, 20, 21490, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FE)
    OP_C8(0x200, 0x46, "C_PLAC20._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)

    def lambda_73A():
        OP_8E(0xFE, 0xA, 0x14, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_73A)

    def lambda_755():
        OP_8E(0xFE, 0xFFFFFB3C, 0x14, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_755)

    def lambda_770():
        OP_8E(0xFE, 0xFFFFFFCE, 0x14, 0x4EDE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_770)

    def lambda_78B():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0x4E7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_78B)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(790, 50, 13670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetChrPos(0x0, 790, 50, 11360, 0)
    SetChrPos(0x1, 790, 50, 11360, 0)
    SetChrPos(0x2, 790, 50, 11360, 0)
    SetChrPos(0x3, 790, 50, 11360, 0)
    OP_A2(0x1E12)
    Jump("loc_8BD")

    label("loc_83C")

    OP_6D(790, 50, 13670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 790, 50, 11360, 0)
    SetChrPos(0x1, 790, 50, 11360, 0)
    SetChrPos(0x2, 790, 50, 11360, 0)
    SetChrPos(0x3, 790, 50, 11360, 0)

    label("loc_8BD")

    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_658 end

    def Function_5_8CE(): pass

    label("Function_5_8CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E0")
    Return()

    label("loc_8E0")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05要回『埃尔赛尤』吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【回船上】\x01",      # 0
            "【不回去】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97C")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_99C")

    label("loc_97C")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_99C")

    Return()

    # Function_5_8CE end

    def Function_6_99D(): pass

    label("Function_6_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AA")
    Return()

    label("loc_9AA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CF")
    Call(0, 7)
    Call(0, 8)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_9CF")

    Fade(1000)
    OP_6D(-1000, 2600, 88570, 0)
    OP_67(0, 3330, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(9000, 0)
    OP_6E(437, 0)
    SetChrPos(0x101, -1150, 400, 83690, 0)
    SetChrPos(0x102, -2640, 400, 83590, 0)
    SetChrPos(0x103, -1030, 20, 81750, 0)
    SetChrPos(0xF9, -2430, 20, 81800, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#1015F#2P『绀碧』之塔……\x02\x03",

            "这次会被传送到\x01",
            "什么样的地方去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1035F#5P不进去的话\x01",
            "是没有办法知道的。\x02\x03",

            "#1042F和『表塔』不同，\x01",
            "由于不受空间上的约制，\x01",
            "因此内部构造似乎很不一样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B44")

    ChrTalk(    #8
        0x106,
        (
            "#053F哦……\x01",
            "真令人不放心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFC")

    label("loc_B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B75")

    ChrTalk(    #9
        0x108,
        (
            "#074F嗯……\x01",
            "真令人不安心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BFC")

    label("loc_B75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA6")

    ChrTalk(    #10
        0x109,
        "#1068F唉～真令人不放心呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFC")

    label("loc_BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(    #11
        0x105,
        "#045F有点紧张呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BFC")

    label("loc_BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFC")

    ChrTalk(    #12
        0x107,
        (
            "#561F呜……\x01",
            "心脏跳得好快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFC")


    ChrTalk(    #13
        0x103,
        (
            "#026F总之……\x01",
            "只有进去看看了。\x02\x03",

            "#022F小心谨慎、一步一步地前进哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C49():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C49)

    def lambda_C57():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C57)

    def lambda_C6F():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_C6F)

    def lambda_C7F():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_C7F)

    def lambda_C8F():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C8F)
    OP_A2(0x1E13)
    WaitChrThread(0x0, 0x0)
    EventEnd(0x0)
    Return()

    # Function_6_99D end

    def Function_7_CA4(): pass

    label("Function_7_CA4")

    FadeToDark(0, 0, -1)
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
        (0, "loc_D1E"),
        (1, "loc_D24"),
        (SWITCH_DEFAULT, "loc_D2A"),
    )


    label("loc_D1E")

    OP_A2(0x1200)
    Jump("loc_D2A")

    label("loc_D24")

    OP_A2(0x1201)
    Jump("loc_D2A")

    label("loc_D2A")

    Return()

    # Function_7_CA4 end

    def Function_8_D2B(): pass

    label("Function_8_D2B")

    FadeToDark(0, 0, -1)
    OP_6D(-48940, 490, -13310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_8_D2B end

    def Function_9_DB8(): pass

    label("Function_9_DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E9B")
    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-2080, 5220, 94860, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(14000, 0)
    OP_6E(376, 0)
    SetChrPos(0x101, -2500, 4000, 94500, 0)
    SetChrPos(0x102, -1500, 4000, 94500, 0)
    SetChrPos(0xF8, -2500, 4000, 93500, 0)
    SetChrPos(0xF9, -1500, 4000, 93500, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E9B")

    Return()

    # Function_9_DB8 end

    def Function_10_E9C(): pass

    label("Function_10_E9C")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_EE1():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE1)

    def lambda_EFB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EFB)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_10_E9C end

    def Function_11_F21(): pass

    label("Function_11_F21")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_F66():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F66)

    def lambda_F80():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F80)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_11_F21 end

    def Function_12_FA6(): pass

    label("Function_12_FA6")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_FEB():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FEB)

    def lambda_1005():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1005)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_FA6 end

    def Function_13_102B(): pass

    label("Function_13_102B")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1070():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1070)

    def lambda_108A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_108A)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_102B end

    def Function_14_10B0(): pass

    label("Function_14_10B0")

    EventBegin(0x0)
    OP_6D(-2080, 5220, 94860, 0)
    OP_67(0, 4690, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(14000, 0)
    OP_6E(376, 0)
    SetChrPos(0x101, -1500, 4000, 96300, 180)
    SetChrPos(0x102, -2500, 4000, 96300, 180)
    SetChrPos(0xF8, -1500, 4000, 96300, 180)
    SetChrPos(0xF9, -2500, 4000, 96300, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0x10)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x11)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x12)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(-2150, 4000, 93840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2150, 4000, 93840, 180)
    SetChrPos(0x1, -2150, 4000, 93840, 180)
    SetChrPos(0x2, -2150, 4000, 93840, 180)
    SetChrPos(0x3, -2150, 4000, 93840, 180)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_14_10B0 end

    def Function_15_1237(): pass

    label("Function_15_1237")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1242():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1242)

    def lambda_125C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_125C)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_127D():
        OP_8F(0xFE, 0xFFFFFA24, 0xE10, 0x16D3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_127D)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_15_1237 end

    def Function_16_1298(): pass

    label("Function_16_1298")

    OP_22(0x99, 0x0, 0x64)

    def lambda_12A3():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12A3)

    def lambda_12BD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12BD)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_12DE():
        OP_8F(0xFE, 0xFFFFF63C, 0xE10, 0x16D3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12DE)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_16_1298 end

    def Function_17_12F9(): pass

    label("Function_17_12F9")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1304():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1304)

    def lambda_131E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_131E)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_133F():
        OP_8F(0xFE, 0xFFFFFA24, 0xE10, 0x17124, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_133F)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_17_12F9 end

    def Function_18_135A(): pass

    label("Function_18_135A")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1365():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1365)

    def lambda_137F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_137F)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_13A0():
        OP_8F(0xFE, 0xFFFFF63C, 0xE10, 0x17124, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13A0)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_18_135A end

    SaveToFile()

Try(main)
