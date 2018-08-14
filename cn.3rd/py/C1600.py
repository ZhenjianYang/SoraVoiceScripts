from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1600   ._SN',
        MapName             = 'Bose',
        Location            = 'C1600.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60125",
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
        '寒冰碎片',                             # 9
        '寒冰至尊',                             # 10
        '洛克',                                 # 11
        '目标用照相机',                         # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
        'ED6_DT07/CH02530 ._CH',             # 0C
        'ED6_DT07/CH00450 ._CH',             # 0D
        'ED6_DT07/CH00460 ._CH',             # 0E
        'ED6_DT07/CH00470 ._CH',             # 0F
        'ED6_DT07/CH00454 ._CH',             # 10
        'ED6_DT07/CH00464 ._CH',             # 11
        'ED6_DT07/CH00474 ._CH',             # 12
        'ED6_DT07/CH00451 ._CH',             # 13
        'ED6_DT07/CH00461 ._CH',             # 14
        'ED6_DT07/CH00471 ._CH',             # 15
        'ED6_DT07/CH00462 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
        'ED6_DT07/CH02530P._CP',             # 0C
        'ED6_DT07/CH00450P._CP',             # 0D
        'ED6_DT07/CH00460P._CP',             # 0E
        'ED6_DT07/CH00470P._CP',             # 0F
        'ED6_DT07/CH00454P._CP',             # 10
        'ED6_DT07/CH00464P._CP',             # 11
        'ED6_DT07/CH00474P._CP',             # 12
        'ED6_DT07/CH00451P._CP',             # 13
        'ED6_DT07/CH00461P._CP',             # 14
        'ED6_DT07/CH00471P._CP',             # 15
        'ED6_DT07/CH00462P._CP',             # 16
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5230,
        Z                   = 4000,
        Y                   = -12590,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28010,
        Z                   = 6000,
        Y                   = -9400,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21830,
        Z                   = 6560,
        Y                   = -1430,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35520,
        Z                   = 16000,
        Y                   = 14970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8390,
        Z                   = 16000,
        Y                   = -3360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25620,
        Z                   = 22000,
        Y                   = 15270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3A8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -11880,
        Y                   = 4000,
        Z                   = -6460,
        Range               = -10050,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0xFFFFC7A2,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = 18300,
        Y                   = 17460,
        Z                   = 8020,
        Range               = 21370,
        Unknown_10          = 0x57BC,
        Unknown_14          = 0x6AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_2CA",          # 00, 0
        "Function_1_313",          # 01, 1
        "Function_2_362",          # 02, 2
        "Function_3_378",          # 03, 3
        "Function_4_5E6",          # 04, 4
        "Function_5_AEC",          # 05, 5
        "Function_6_1260",         # 06, 6
    )


    def Function_0_2CA(): pass

    label("Function_0_2CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E3")
    SetChrFlags(0x19, 0x80)

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5030, 4000, -13130, 270)

    label("loc_306")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")

    label("loc_312")

    Return()

    # Function_0_2CA end

    def Function_1_313(): pass

    label("Function_1_313")

    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    OP_B2(0x0, 0x1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_B2(0x1, 0x0, 0x80)
    OP_B2(0x1, 0x1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 7)), scpexpr(EXPR_END)), "loc_355")
    OP_B2(0x0, 0x1, 0x80)

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F2, 4)), scpexpr(EXPR_END)), "loc_361")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_361")

    Return()

    # Function_1_313 end

    def Function_2_362(): pass

    label("Function_2_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_362")

    label("loc_377")

    Return()

    # Function_2_362 end

    def Function_3_378(): pass

    label("Function_3_378")

    EventBegin(0x0)
    Fade(1500)
    OP_6D(-11540, 4000, -8180, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_3A8():
        OP_6D(-9000, 4000, -10140, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3A8)

    def lambda_3C0():
        OP_6C(330000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3C0)

    def lambda_3D0():
        OP_67(0, 5860, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3D0)

    def lambda_3E8():
        OP_6B(3420, 2500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_3E8)
    OP_11(0xFF, 0xFF, 0xFF, 0x878C, 0xFF78, 0x0)
    SetChrPos(0x111, -11540, 4000, -11370, 124)
    SetChrPos(0x113, -10550, 4000, -9690, 124)
    SetChrPos(0x112, -10570, 4000, -11060, 124)
    WaitChrThread(0x13, 0x0)

    ChrTalk(    #0
        0x113,
        "#1765F#5P哼，又出现了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x112,
        (
            "#1756F#5P这家伙，看上去\x01",
            "好像没有什么大本事的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x111,
        (
            "#1744F#5P别大意，小心遭受惨痛教训哦。\x02\x03",

            "#1742F密切注意对手的举动，然后再出手。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x113, 0x1000)
    SetChrFlags(0x111, 0x1000)
    SetChrFlags(0x112, 0x1000)

    def lambda_515():
        OP_6D(-7000, 3500, -10140, 1000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_515)

    def lambda_52D():
        OP_6B(2920, 1000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_52D)
    SetChrChipByIndex(0x112, 20)
    SetChrSubChip(0x112, 0)

    def lambda_547():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFCE28, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_547)
    Sleep(50)
    SetChrChipByIndex(0x111, 19)
    SetChrSubChip(0x111, 0)

    def lambda_571():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFCCFC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_571)
    Sleep(50)
    SetChrChipByIndex(0x113, 21)
    SetChrSubChip(0x113, 0)

    def lambda_59B():
        OP_8E(0xFE, 0xFFFFE840, 0xFA0, 0xFFFFD0E4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_59B)
    Sleep(450)
    OP_44(0x113, 0xFF)
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x13, 0xFF)
    ClearChrFlags(0x113, 0x1000)
    ClearChrFlags(0x111, 0x1000)
    ClearChrFlags(0x112, 0x1000)
    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 4)
    Return()

    # Function_3_378 end

    def Function_4_5E6(): pass

    label("Function_4_5E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-6440, 4000, -11720, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x8F5C, 0xFF78, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x111, -5050, 4000, -11660, 225)
    SetChrPos(0x113, -4540, 4000, -13610, 315)
    SetChrPos(0x112, -6490, 4000, -13030, 45)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0x112,
        "#1755F#5P哈哈，总算是打倒了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x111,
        (
            "#1749F#11P嗯，虽然有点费劲，\x01",
            "不过按照这种势头前进的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x113,
        (
            "#1764F#6P#1S嘁……\x01",
            "如果有三个我的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_781():

        label("loc_781")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_781")

    QueueWorkItem2(0x112, 2, lambda_781)
    Sleep(100)

    def lambda_797():

        label("loc_797")

        TurnDirection(0xFE, 0x113, 400)
        OP_48()
        Jump("loc_797")

    QueueWorkItem2(0x111, 2, lambda_797)
    Sleep(300)

    ChrTalk(    #6
        0x112,
        "#1753F#5P……嗯？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x111,
        "#1743F#11P……说什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x113,
        (
            "#1762F啊，被听到了啊？\x02\x03",

            "#1763F那就再说一遍。\x02\x03",

            "#1761F如果有三个我的话……\x01",
            "肯定可以轻松战胜这些家伙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x112,
        "#1753F#5P啊？你在说什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x111,
        (
            "#1745F#11P…………………\x02\x03",

            "#1749F……不管怎样，\x01",
            "现在只能是我们这三个人一起行动。\x02\x03",

            "#1742F如果有什么抱怨，\x01",
            "放在心里说就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x113,
        (
            "#1764F#6P哼……\x02\x03",

            "#1763F至少，不要拖后腿嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x113, 90, 500)
    Sleep(100)

    def lambda_978():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x113, 1, lambda_978)
    Sleep(1500)

    ChrTalk(    #12
        0x112,
        "#1752F#5P……怎、怎么了，这家伙？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x111,
        "#1742F#5P…………………\x02",
    )

    CloseMessageWindow()
    OP_44(0x111, 0x2)
    OP_44(0x112, 0x2)

    def lambda_9F2():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_9F2)
    Sleep(100)

    def lambda_A12():
        OP_8E(0xFE, 0x123E, 0xFA0, 0xFFFFCD38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_A12)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x111, 0xFF)
    OP_44(0x112, 0xFF)
    OP_44(0x113, 0xFF)
    OP_6D(2240, 4000, -12100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0xAAB4, 0xFF78, 0x0)
    SetChrPos(0x111, 2240, 4000, -12100, 90)
    SetChrPos(0x112, 2240, 4000, -12100, 90)
    SetChrPos(0x113, 2240, 4000, -12100, 90)
    SetChrSubChip(0x111, 0)
    SetChrSubChip(0x112, 0)
    SetChrSubChip(0x113, 0)
    Sleep(1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F94)
    OP_B2(0x0, 0x0, 0x80)
    EventEnd(0x4)
    Return()

    # Function_4_5E6 end

    def Function_5_AEC(): pass

    label("Function_5_AEC")

    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23480, 22200, 18920, 150)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 27400, 22000, 15240, 315)
    SetChrChipByIndex(0x12, 18)
    SetChrSubChip(0x12, 3)
    LoadEffect(0x0, "Condition\\\\freeze.eff")
    LoadEffect(0x1, "battle\\\\mgaria0.eff")
    LoadEffect(0x2, "battle\\\\mgaria1.eff")
    LoadEffect(0x3, "magic\\\\mg030_0.eff")
    LoadEffect(0x4, "monster\\ms00300.eff")
    PlayEffect(0x0, 0x1, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    OP_6D(19100, 19040, 5460, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x7FBC, 0xFF78, 0x0)
    SetChrPos(0x111, 19330, 18450, 4490, 45)
    SetChrPos(0x112, 18590, 18490, 5380, 45)
    Sleep(1000)
    OP_20(0x7D0)
    OP_8C(0x112, 45, 0)
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #14
        0x112,
        (
            "#1752F#6P喂，迪恩。\x01",
            "在那里的不就是……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x111,
        "#1743F#6P咦……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x111, 45, 0)
    OP_62(0x111, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_21()
    OP_1D(0x29)
    Sleep(500)

    ChrTalk(    #16
        0x111,
        "#1747F#6P嘁，这个笨蛋家伙！\x02",
    )

    CloseMessageWindow()

    def lambda_D1A():
        OP_6D(25960, 22000, 19140, 2500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_D1A)

    def lambda_D32():
        OP_6C(8000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_D32)

    def lambda_D42():
        OP_67(0, 5260, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_D42)

    def lambda_D5A():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_D5A)
    WaitChrThread(0x13, 0x0)
    Sleep(1000)

    ChrTalk(    #17
        0x12,
        (
            "#1767F#12P#40W这个家伙……！\x02\x03",

            "糟糕，动不了了……\x02\x03",

            "#1764F可、可恶……\x01",
            "难道就死在这里了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x112, 19330, 18450, 4490, 45)
    SetChrPos(0x111, 18590, 18490, 5380, 45)

    def lambda_E0C():
        OP_6D(26100, 22000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_E0C)

    def lambda_E24():
        OP_67(0, 4380, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_E24)

    def lambda_E3C():
        OP_8E(0xFE, 0x5F50, 0x5442, 0x2E54, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_E3C)
    Sleep(100)

    def lambda_E5C():
        OP_8F(0xFE, 0x6478, 0x5460, 0x2940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_E5C)
    WaitChrThread(0x111, 0x1)

    def lambda_E7C():

        label("loc_E7C")

        TurnDirection(0xFE, 0x12, 500)
        OP_48()
        Jump("loc_E7C")

    QueueWorkItem2(0x112, 2, lambda_E7C)
    Sleep(300)

    ChrTalk(    #18
        0x111,
        (
            "#1747F#6P洛克！！\x02\x03",

            "#1743F……不好，\x01",
            "好像被冻起来了。\x02\x03",

            "#1742F雷斯，拜托了！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x112, 0x1)
    OP_44(0x112, 0x2)

    ChrTalk(    #19
        0x112,
        "#1756F#6P知道啦！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(100)
    SetChrChipByIndex(0x112, 22)
    SetChrSubChip(0x112, 0)

    def lambda_F2E():
        OP_99(0xFE, 0x0, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x112, 2, lambda_F2E)
    Sleep(400)
    PlayEffect(0x4, 0x2, 0x112, 500, 300, 700, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 700, 0, 0)
    Sleep(1500)

    ChrTalk(    #20
        0x12,
        "#1767F#3S#11P烫烫烫烫烫烫！！#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x1F4)
    CloseMessageWindow()
    OP_82(0x2, 0x2)
    OP_82(0x1, 0x2)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x12,
        "#1762F#11P……可、可以动了。\x02",
    )

    CloseMessageWindow()

    def lambda_1006():
        OP_6D(25520, 22000, 19500, 1500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1006)

    def lambda_101E():
        OP_6B(3640, 1500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_101E)

    def lambda_102E():
        OP_8E(0xFE, 0x66F8, 0x55F0, 0x3F34, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x111, 1, lambda_102E)
    Sleep(100)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)

    def lambda_1058():
        OP_8E(0xFE, 0x6324, 0x55F0, 0x38F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x112, 1, lambda_1058)
    WaitChrThread(0x111, 0x1)
    OP_8C(0x111, 315, 500)
    SetChrChipByIndex(0x111, 13)
    SetChrSubChip(0x111, 0)
    WaitChrThread(0x112, 0x1)
    OP_8C(0x112, 315, 500)
    SetChrChipByIndex(0x112, 14)
    SetChrSubChip(0x112, 0)
    Sleep(300)

    ChrTalk(    #22
        0x111,
        "#1741F#5P哼，真丢人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x112,
        "#1756F#6P来晚了，真是抱歉哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "#1762F#12P是、是你们！？\x02\x03",

            "#1767F你们到底是来干什么的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x112,
        (
            "#1751F#6P干什么……\x01",
            "不是明摆着来帮你的吗? \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x111,
        "#1747F#5P有话一会儿再说，大家一起反击吧！\x02",
    )

    CloseMessageWindow()

    def lambda_11A7():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_11A7)
    Sleep(200)
    Fade(500)
    OP_99(0x12, 0x3, 0x2, 0x1F4)
    Sleep(100)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #27
        0x12,
        "#1766F哼……没办法！\x02",
    )

    CloseMessageWindow()
    OP_59()
    AddParty(0x12, 0xF0, 0xFF)
    SetChrPos(0x113, 27400, 22000, 15240, 315)
    SetChrChipByIndex(0x113, 15)
    SetChrSubChip(0x113, 0)
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x112, 25380, 22000, 14580, 315)
    SetChrChipByIndex(0x112, 14)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x111, 13)
    SetChrSubChip(0x111, 0)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 6)
    Return()

    # Function_5_AEC end

    def Function_6_1260(): pass

    label("Function_6_1260")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    OP_6D(25120, 22000, 18540, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x83A4, 0xFF78, 0x0)
    SetChrPos(0x111, 25020, 22000, 16970, 315)
    SetChrPos(0x113, 25940, 22000, 15420, 315)
    SetChrPos(0x112, 24210, 22000, 15900, 315)
    SetChrChipByIndex(0x111, 65535)
    SetChrSubChip(0x111, 0)
    SetChrChipByIndex(0x112, 65535)
    SetChrSubChip(0x112, 0)
    SetChrChipByIndex(0x113, 65535)
    SetChrSubChip(0x113, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #28
        0x111,
        (
            "#1749F#5P呼，\x01",
            "还好赶上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x112,
        (
            "#1750F#5P真是的，\x01",
            "洛克你也真会乱来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x113,
        (
            "#1767F#12P喂，你们这些家伙！\x01",
            "干嘛要特意追上来呢！？\x02\x03",

            "你们不来的话\x01",
            "我一个人也能……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13E9():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x111, 2, lambda_13E9)
    Sleep(100)
    OP_8C(0x112, 135, 500)
    Sleep(300)

    ChrTalk(    #31
        0x111,
        "#1747F#4S#5P笨蛋家伙！！！#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #32
        0x113,
        "#1762F#12P……什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x111,
        (
            "#1747F#5P你还想死要面子\x01",
            "到什么时候！\x02\x03",

            "你这乱逞强的结果\x01",
            "不就是落得刚才那个样子吗！\x02\x03",

            "你这家伙到底是\x01",
            "真不明白还是装糊涂！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x113,
        "#1767F#12P……你、你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x111,
        (
            "#1745F#5P唉……\x01",
            "说什么也不该轮到我发火。\x02\x03",

            "#1749F……对不起，洛克。\x02\x03",

            "我刚才说让你一个人走，\x01",
            "的确是有些过分了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x113,
        "#1762F#12P………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x111,
        (
            "#1744F#5P刚才虽然说了那样的话……\x02\x03",

            "#1742F但我们以游击士为目标\x01",
            "可不只是因为被你拉来而已。\x02\x03",

            "不管怎么样，\x01",
            "我们通过了地狱般的特训……\x02\x03",

            "自然没有不百分百投入的道理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x112,
        (
            "#1754F#5P没错，洛克。\x02\x03",

            "#1750F我们也是认真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x111,
        (
            "#1749F#5P当然我们也能够理解\x01",
            "你想尽快追赶上\x01",
            "阿加特大哥的焦急心情。\x02\x03",

            "#1740F难得我们\x01",
            "一共有三个人。\x02\x03",

            "有什么事情\x01",
            "互相照顾一下\x01",
            "不是更好吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x113, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x113)
    Sleep(500)

    ChrTalk(    #40
        0x113,
        (
            "#1763F#12P哼……\x02\x03",

            "#1764F……真是的，\x01",
            "竟然落到被你们这么说的地步。\x02\x03",

            "我也不是笨蛋……\x01",
            "自己的实力自己清楚。\x02\x03",

            "#1760F迪恩，正像你说的，\x01",
            "或许是因为我太着急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x111,
        "#1743F#5P洛克……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x113,
        (
            "#1764F#12P居然被那该死的家伙打败……\x01",
            "我算是体会到\x01",
            "自己的能耐有几斤几两了。\x02\x03",

            "#1763F要想突破这里……\x01",
            "还是需要你们的力量才行。\x02\x03",

            "#1760F对不起，迪恩、雷斯……\x02\x03",

            "能让我……\x01",
            "回到你们的行列中吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x111,
        (
            "#1746F#5P哼，笨蛋家伙……\x02\x03",

            "#1741F这还用说，\x01",
            "自然是没问题！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x113,
        "#1761F#12P迪恩……\x02",
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x112,
        (
            "#1751F#5P哈哈哈，你们这两个家伙，\x01",
            "还这么装模作样！\x02\x03",

            "#1756F要不作为重新和好的见证，\x01",
            "在这里拥抱如何啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x113,
        (
            "#1763F#12P你、你胡说什么啊！\x02\x03",

            "#1767F对了，雷斯……\x01",
            "你刚才的那招是认真的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x112,
        "#1753F#5P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x113,
        (
            "#1765F#12P针对冻结状态\x01",
            "使用痊愈之药或活性之药，\x01",
            "那才是常识吧。\x02\x03",

            "#1763F真是的，你难道想杀了我吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #49
        0x112,
        (
            "#1751F#5P哪里哪里……\x01",
            "反正已经解决了，那就一切都好啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x113,
        (
            "#1765F#12P唉……\x02\x03",

            "#1763F哼，\x01",
            "不管怎样，还是脱险了。\x02\x03",

            "#1761F……谢啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x112, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x112,
        (
            "#1753F#5P……洛、洛克？\x02\x03",

            "#1755F你、你不会是……\x01",
            "想和我拥抱吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x113,
        "#1767F#12P哼，你这句话就说一辈子吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x112,
        "#1751F#5P哈哈哈，玩笑玩笑。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x111,
        (
            "#1741F#5P哈哈，\x01",
            "那我们赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x113,
        "#1761F#4P好！\x02",
    )


    ChrTalk(    #56
        0x112,
        "#1756F#3P知道啦！\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_A2(0x2F97)
    OP_B2(0x0, 0x1, 0x80)
    StopSound(0xAAB4, 0xFF78, 0x3E8)
    EventEnd(0x0)
    Return()

    # Function_6_1260 end

    SaveToFile()

Try(main)
