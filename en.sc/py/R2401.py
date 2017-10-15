from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_2_399",          # 02, 2
        "Function_3_4BA",          # 03, 3
        "Function_4_689",          # 04, 4
        "Function_5_90F",          # 05, 5
        "Function_6_9E3",          # 06, 6
        "Function_7_EB6",          # 07, 7
        "Function_8_F3C",          # 08, 8
        "Function_9_FC9",          # 09, 9
        "Function_10_10AD",        # 0A, 10
        "Function_11_1132",        # 0B, 11
        "Function_12_11B7",        # 0C, 12
        "Function_13_123C",        # 0D, 13
        "Function_14_12C1",        # 0E, 14
        "Function_15_1448",        # 0F, 15
        "Function_16_14A9",        # 10, 16
        "Function_17_150A",        # 11, 17
        "Function_18_156B",        # 12, 18
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

    OP_E0(0x0, 0x14, 0x28, 0x0, 0x0, 0x14, 0x0, 0x0, 0x0, 0x98, 0x4D, 0x1, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_309")
    Jump("loc_359")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_359")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -2070, 6000, 96100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_359")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_372")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_378")

    label("loc_372")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_378")

    OP_B2(0x0, 0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_398")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x3, 0x80)

    label("loc_398")

    Return()

    # Function_1_2A7 end

    def Function_2_399(): pass

    label("Function_2_399")

    OP_EA(0x2, 0xE8, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C8, 1)"), scpexpr(EXPR_END)), "loc_40A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xC8\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x130F)
    Jump("loc_46E")

    label("loc_40A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xC8\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC8\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_46E")

    Jump("loc_4AC")

    label("loc_471")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Empty as your bottom is dry.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4AC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_399 end

    def Function_3_4BA(): pass

    label("Function_3_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 3)), scpexpr(EXPR_END)), "loc_4C2")
    Return()

    label("loc_4C2")

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
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5B6"),
        (SWITCH_DEFAULT, "loc_5D9"),
    )


    label("loc_5B6")

    Fade(500)
    OP_89(0x0, -3140, -60, 60730, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_5D9")

    Battle(0xEF2, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -3140, -60, 60730, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_612"),
        (1, "loc_615"),
        (SWITCH_DEFAULT, "loc_618"),
    )


    label("loc_612")

    EventEnd(0x0)
    Return()

    label("loc_615")

    OP_B4(0x0)
    Return()

    label("loc_618")

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
        "\x07\x05Exterminated monster!\x02",
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

    # Function_3_4BA end

    def Function_4_689(): pass

    label("Function_4_689")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A0")
    Call(0, 7)
    Call(0, 8)

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D")
    OP_6D(-1330, 20, 82650, 0)
    OP_67(0, 12040, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(45000, 0)
    OP_6E(341, 0)
    SetChrPos(0x101, 280, -30, 13880, 0)
    SetChrPos(0x102, -1200, -10, 13760, 0)
    SetChrPos(0x103, 280, 0, 12600, 0)
    SetChrPos(0xF9, -1140, 20, 12330, 0)

    def lambda_72F():
        OP_6D(-450, 20, 21490, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72F)
    OP_C8(0x200, 0x46, "C_PLAC20._CH", 0x1, 0x3E8)
    OP_DE("Sapphirl Tower")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)

    def lambda_77B():
        OP_8E(0xFE, 0xA, 0x14, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_77B)

    def lambda_796():
        OP_8E(0xFE, 0xFFFFFB3C, 0x14, 0x5398, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_796)

    def lambda_7B1():
        OP_8E(0xFE, 0xFFFFFFCE, 0x14, 0x4EDE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7B1)

    def lambda_7CC():
        OP_8E(0xFE, 0xFFFFFA42, 0x0, 0x4E7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_7CC)
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
    Jump("loc_8FE")

    label("loc_87D")

    OP_6D(790, 50, 13670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 790, 50, 11360, 0)
    SetChrPos(0x1, 790, 50, 11360, 0)
    SetChrPos(0x2, 790, 50, 11360, 0)
    SetChrPos(0x3, 790, 50, 11360, 0)

    label("loc_8FE")

    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_689 end

    def Function_5_90F(): pass

    label("Function_5_90F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_921")
    Return()

    label("loc_921")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Return to the Arseille?\x02",
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
            "[Return]\x01",            # 0
            "[Don't Return]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9E2")

    label("loc_9C2")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_9E2")

    Return()

    # Function_5_90F end

    def Function_6_9E3(): pass

    label("Function_6_9E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F0")
    Return()

    label("loc_9F0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A15")
    Call(0, 7)
    Call(0, 8)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_A15")

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
            "#1015F#2PThe Sapphirl Tower...\x02\x03",

            "Wonder where we'll get\x01",
            "punted off to this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1035F#5PThere's no real way to\x01",
            "know until we go in.\x02\x03",

            "#1042FUnlike the 'normal' towers, the shadow towers\x01",
            "don't seem restricted by conventional spatial\x01",
            "definitions. They could be...large, inside.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2D")

    ChrTalk(    #8
        0x106,
        (
            "#053FLimited only by how crazy the builders\x01",
            "are, huh? Heh, creepy thing to think about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_C2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #9
        0x108,
        (
            "#074FAnd so the only limit on their construction\x01",
            "was their builders. Mmm... Hard to stay\x01",
            "focused, thinking about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_CBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D26")

    ChrTalk(    #10
        0x109,
        (
            "#1068FSo the only restriction is when the ancients\x01",
            "got bored. Thaaaaaat's comforting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_D26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D9E")

    ChrTalk(    #11
        0x105,
        (
            "#045FConstrained only by the will of their builders...\x01",
            "that's a bit nerve-racking to think about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE1")

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE1")

    ChrTalk(    #12
        0x107,
        "#561FAaaa, that's kind of scary to think about!\x02",
    )

    CloseMessageWindow()

    label("loc_DE1")


    ChrTalk(    #13
        0x103,
        (
            "#026FRegardless, we have to go\x01",
            "in one way or another.\x02\x03",

            "#022FCome on. Let's proceed\x01",
            "carefully and deliberately.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E5B():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E5B)

    def lambda_E69():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E69)

    def lambda_E81():
        OP_6B(3200, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E81)

    def lambda_E91():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_E91)

    def lambda_EA1():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EA1)
    OP_A2(0x1E13)
    WaitChrThread(0x0, 0x0)
    EventEnd(0x0)
    Return()

    # Function_6_9E3 end

    def Function_7_EB6(): pass

    label("Function_7_EB6")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F2F"),
        (1, "loc_F35"),
        (SWITCH_DEFAULT, "loc_F3B"),
    )


    label("loc_F2F")

    OP_A2(0x1200)
    Jump("loc_F3B")

    label("loc_F35")

    OP_A2(0x1201)
    Jump("loc_F3B")

    label("loc_F3B")

    Return()

    # Function_7_EB6 end

    def Function_8_F3C(): pass

    label("Function_8_F3C")

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

    # Function_8_F3C end

    def Function_9_FC9(): pass

    label("Function_9_FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10AC")
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

    label("loc_10AC")

    Return()

    # Function_9_FC9 end

    def Function_10_10AD(): pass

    label("Function_10_10AD")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_10F2():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10F2)

    def lambda_110C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_110C)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_10_10AD end

    def Function_11_1132(): pass

    label("Function_11_1132")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1177():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1177)

    def lambda_1191():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1191)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_11_1132 end

    def Function_12_11B7(): pass

    label("Function_12_11B7")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_11FC():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11FC)

    def lambda_1216():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1216)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_11B7 end

    def Function_13_123C(): pass

    label("Function_13_123C")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1281():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1281)

    def lambda_129B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_129B)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_123C end

    def Function_14_12C1(): pass

    label("Function_14_12C1")

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

    # Function_14_12C1 end

    def Function_15_1448(): pass

    label("Function_15_1448")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1453():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1453)

    def lambda_146D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_146D)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_148E():
        OP_8F(0xFE, 0xFFFFFA24, 0xE10, 0x16D3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_148E)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_15_1448 end

    def Function_16_14A9(): pass

    label("Function_16_14A9")

    OP_22(0x99, 0x0, 0x64)

    def lambda_14B4():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14B4)

    def lambda_14CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14CE)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_14EF():
        OP_8F(0xFE, 0xFFFFF63C, 0xE10, 0x16D3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14EF)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_16_14A9 end

    def Function_17_150A(): pass

    label("Function_17_150A")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1515():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1515)

    def lambda_152F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_152F)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_1550():
        OP_8F(0xFE, 0xFFFFFA24, 0xE10, 0x17124, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1550)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_17_150A end

    def Function_18_156B(): pass

    label("Function_18_156B")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1576():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1576)

    def lambda_1590():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1590)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_15B1():
        OP_8F(0xFE, 0xFFFFF63C, 0xE10, 0x17124, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15B1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_18_156B end

    SaveToFile()

Try(main)
