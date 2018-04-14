from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C1300   ._SN',
        MapName             = 'Bose',
        Location            = 'C1300.x',
        MapIndex            = 52,
        MapDefaultBGM       = "ed60089",
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
        '穆拉',                                 # 9
        '朵洛希',                               # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '空贼船',                               # 18
        '空贼船（影）',                         # 19
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
        'ED6_DT27/CH03570 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH02070 ._CH',             # 02
        'ED6_DT06/CH20063 ._CH',             # 03
        'ED6_DT06/CH20064 ._CH',             # 04
        'ED6_DT27/CH04010 ._CH',             # 05
        'ED6_DT27/CH04011 ._CH',             # 06
        'ED6_DT07/CH00310 ._CH',             # 07
        'ED6_DT07/CH00311 ._CH',             # 08
        'ED6_DT07/CH00290 ._CH',             # 09
        'ED6_DT07/CH00291 ._CH',             # 0A
        'ED6_DT07/CH00300 ._CH',             # 0B
        'ED6_DT07/CH00301 ._CH',             # 0C
        'ED6_DT27/CH04570 ._CH',             # 0D
        'ED6_DT27/CH04571 ._CH',             # 0E
        'ED6_DT27/CH04572 ._CH',             # 0F
        'ED6_DT07/CH00321 ._CH',             # 10
        'ED6_DT06/CH20043 ._CH',             # 11
        'ED6_DT07/CH00326 ._CH',             # 12
        'ED6_DT07/CH00320 ._CH',             # 13
        'ED6_DT27/CH03010 ._CH',             # 14
        'ED6_DT27/CH03011 ._CH',             # 15
        'ED6_DT27/CH03101 ._CH',             # 16
        'ED6_DT27/CH03014 ._CH',             # 17
        'ED6_DT27/CH03761 ._CH',             # 18
        'ED6_DT27/CH03771 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT27/CH03570P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH02070P._CP',             # 02
        'ED6_DT06/CH20063P._CP',             # 03
        'ED6_DT06/CH20064P._CP',             # 04
        'ED6_DT27/CH04010P._CP',             # 05
        'ED6_DT27/CH04011P._CP',             # 06
        'ED6_DT07/CH00310P._CP',             # 07
        'ED6_DT07/CH00311P._CP',             # 08
        'ED6_DT07/CH00290P._CP',             # 09
        'ED6_DT07/CH00291P._CP',             # 0A
        'ED6_DT07/CH00300P._CP',             # 0B
        'ED6_DT07/CH00301P._CP',             # 0C
        'ED6_DT27/CH04570P._CP',             # 0D
        'ED6_DT27/CH04571P._CP',             # 0E
        'ED6_DT27/CH04572P._CP',             # 0F
        'ED6_DT07/CH00321P._CP',             # 10
        'ED6_DT06/CH20043P._CP',             # 11
        'ED6_DT07/CH00326P._CP',             # 12
        'ED6_DT07/CH00320P._CP',             # 13
        'ED6_DT27/CH03010P._CP',             # 14
        'ED6_DT27/CH03011P._CP',             # 15
        'ED6_DT27/CH03101P._CP',             # 16
        'ED6_DT27/CH03014P._CP',             # 17
        'ED6_DT27/CH03761P._CP',             # 18
        'ED6_DT27/CH03771P._CP',             # 19
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -9880,
        TriggerZ            = 4000,
        TriggerY            = -550,
        TriggerRange        = 1500,
        ActorX              = -8980,
        ActorZ              = 5200,
        ActorY              = -340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2FE",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_350",          # 02, 2
        "Function_3_5F8",          # 03, 3
        "Function_4_623",          # 04, 4
        "Function_5_64E",          # 05, 5
        "Function_6_679",          # 06, 6
        "Function_7_6A4",          # 07, 7
        "Function_8_6D4",          # 08, 8
        "Function_9_718",          # 09, 9
        "Function_10_75C",         # 0A, 10
        "Function_11_7A0",         # 0B, 11
        "Function_12_7CC",         # 0C, 12
        "Function_13_81A",         # 0D, 13
        "Function_14_868",         # 0E, 14
        "Function_15_8B6",         # 0F, 15
        "Function_16_904",         # 10, 16
        "Function_17_911",         # 11, 17
        "Function_18_DE7",         # 12, 18
        "Function_19_1684",        # 13, 19
        "Function_20_22BE",        # 14, 20
        "Function_21_238D",        # 15, 21
        "Function_22_246C",        # 16, 22
        "Function_23_24CF",        # 17, 23
        "Function_24_2508",        # 18, 24
        "Function_25_2570",        # 19, 25
        "Function_26_25D8",        # 1A, 26
        "Function_27_2606",        # 1B, 27
        "Function_28_266E",        # 1C, 28
        "Function_29_26A1",        # 1D, 29
        "Function_30_2706",        # 1E, 30
        "Function_31_29F5",        # 1F, 31
        "Function_32_2D05",        # 20, 32
        "Function_33_2D47",        # 21, 33
    )


    def Function_0_2FE(): pass

    label("Function_0_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A")
    Event(0, 2)

    label("loc_30A")

    Return()

    # Function_0_2FE end

    def Function_1_30B(): pass

    label("Function_1_30B")

    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_A1(0x11, 0x0)
    OP_A1(0x12, 0x1)
    SetChrPos(0x11, -2160, 0, -1510, 0)
    SetChrPos(0x12, -2160, 100, -1510, 0)
    OP_8C(0x11, 350, 0)
    OP_8C(0x12, 350, 0)
    Return()

    # Function_1_30B end

    def Function_2_350(): pass

    label("Function_2_350")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-17010, 4000, -16370, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(145000, 0)
    OP_6E(262, 0)
    OP_43(0x129, 0x1, 0x0, 0x3)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0x4)
    Sleep(500)
    OP_43(0x146, 0x1, 0x0, 0x5)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x6)
    WaitChrThread(0x129, 0x1)
    OP_8C(0x129, 0, 400)

    ChrTalk(    #0
        0x129,
        "#192F#2P哦哦……！\x02",
    )

    CloseMessageWindow()

    def lambda_3F8():
        OP_6D(-7610, 4000, -1690, 7000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F8)

    def lambda_410():
        OP_67(0, 5790, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_410)

    def lambda_428():
        OP_6E(255, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_428)

    def lambda_438():
        OP_6B(4660, 7000)
        ExitThread()

    QueueWorkItem(0x129, 3, lambda_438)
    OP_43(0x129, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x12A, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0x146, 0x1, 0x0, 0x9)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0xA)
    WaitChrThread(0x146, 0x1)

    ChrTalk(    #1
        0x129,
        (
            "#191F#6P可爱的『山猫号』……\x01",
            "真是想死你了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x146,
        (
            "#211F看起来\x01",
            "保养得很好呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x12A,
        (
            "#202F#5P嘿嘿，不愧是利贝尔军。\x01",
            "知道该怎么样好好对待飞船。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)
    OP_8C(0x102, 0, 400)
    Sleep(500)

    ChrTalk(    #4
        0x102,
        (
            "#1035F#2P我知道你们很高兴，\x01",
            "不过时间所剩不多了。\x02\x03",

            "#1030F启动钥匙也到手了\x01",
            "能不能赶快准备出发呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12A, 180, 400)

    ChrTalk(    #5
        0x12A,
        "#200F#6P是是，知道啦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x129, 180, 400)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #6
        0x129,
        (
            "#198F#6P真是的……\x01",
            "再让我们沉浸一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x146,
        "#210F#6P那么进去吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1804)
    EventEnd(0x0)
    Return()

    # Function_2_350 end

    def Function_3_5F8(): pass

    label("Function_3_5F8")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0xBB8, 0x0)
    Return()

    # Function_3_5F8 end

    def Function_4_623(): pass

    label("Function_4_623")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE55C, 0xBB8, 0x0)
    Return()

    # Function_4_623 end

    def Function_5_64E(): pass

    label("Function_5_64E")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFE944, 0xBB8, 0x0)
    Return()

    # Function_5_64E end

    def Function_6_679(): pass

    label("Function_6_679")

    SetChrPos(0xFE, -17220, 0, -8680, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFED2C, 0xBB8, 0x0)
    Return()

    # Function_6_679 end

    def Function_7_6A4(): pass

    label("Function_7_6A4")

    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x2DA, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_6A4 end

    def Function_8_6D4(): pass

    label("Function_8_6D4")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD5EE, 0xFA0, 0xFFFFFE20, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_6D4 end

    def Function_9_718(): pass

    label("Function_9_718")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD0E4, 0xFA0, 0x2D0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_9_718 end

    def Function_10_75C(): pass

    label("Function_10_75C")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xBB8, 0x0)
    OP_90(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFD210, 0xFA0, 0xFFFFF9B6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_75C end

    def Function_11_7A0(): pass

    label("Function_11_7A0")

    OP_43(0xA, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xB, 0x0, 0x0, 0xD)
    Sleep(400)
    OP_43(0xC, 0x0, 0x0, 0xE)
    Sleep(300)
    OP_43(0xD, 0x0, 0x0, 0xF)
    Return()

    # Function_11_7A0 end

    def Function_12_7CC(): pass

    label("Function_12_7CC")

    OP_8E(0xFE, 0xFFFFBF78, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD38, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD274, 0xFA0, 0xFFFFE00C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_7CC end

    def Function_13_81A(): pass

    label("Function_13_81A")

    OP_8E(0xFE, 0xFFFFBBAE, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC950, 0x7D0, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD56, 0xFA0, 0xFFFFE0D4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_81A end

    def Function_14_868(): pass

    label("Function_14_868")

    OP_8E(0xFE, 0xFFFFBF78, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD38, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFD35A, 0xFA0, 0xFFFFD990, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_868 end

    def Function_15_8B6(): pass

    label("Function_15_8B6")

    OP_8E(0xFE, 0xFFFFBBA4, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFC950, 0x3E8, 0xFFFFBF28, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFCD56, 0xFA0, 0xFFFFDA76, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_8B6 end

    def Function_16_904(): pass

    label("Function_16_904")

    Call(0, 17)
    Call(0, 18)
    Call(0, 19)
    Return()

    # Function_16_904 end

    def Function_17_911(): pass

    label("Function_17_911")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-10510, 4000, 30, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(3930, 0)
    OP_6C(145000, 0)
    OP_6E(255, 0)
    SetChrPos(0xA, -15480, 4000, -12010, 0)
    SetChrPos(0x102, -11480, 4000, -1700, 90)
    SetChrPos(0x146, -12030, 4000, 580, 90)
    SetChrPos(0x129, -10510, 4000, 720, 90)
    SetChrPos(0x12A, -10510, 4000, -1000, 90)
    OP_0D()

    NpcTalk(    #8
        0xA,
        "声音",
        "#3P……走喽！\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x129, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, -16520, 2000, -11870, 0)
    SetChrPos(0xB, -17490, 2000, -11830, 0)
    SetChrPos(0xC, -16520, 1000, -10800, 0)
    SetChrPos(0xD, -17500, 1000, -10870, 0)
    SetChrChipByIndex(0xA, 16)
    SetChrChipByIndex(0xB, 16)
    SetChrChipByIndex(0xC, 16)
    SetChrChipByIndex(0xD, 16)

    def lambda_AA5():
        OP_6D(-12670, 4000, -11680, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AA5)

    def lambda_ABD():
        OP_67(0, 6070, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_ABD)

    def lambda_AD5():
        OP_6C(147000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_AD5)

    def lambda_AE5():
        OP_6B(2880, 2000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AE5)

    def lambda_AF5():
        OP_6E(322, 2000)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_AF5)
    OP_43(0xD, 0x3, 0x0, 0xB)

    def lambda_B0C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B0C)
    Sleep(100)

    def lambda_B1F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_B1F)
    Sleep(50)

    def lambda_B32():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_B32)
    Sleep(100)

    def lambda_B45():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_B45)
    Sleep(3000)
    OP_6D(-11430, 4000, -4670, 1500)

    ChrTalk(    #9
        0x129,
        "#192F#5P哎哎……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12A,
        "#201F#5P切，被发现了吗！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x0)

    ChrTalk(    #11
        0xB,
        "#4P空贼！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        "#6P什，什么时候……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xD,
        (
            "是这些家伙让队长他们\x01",
            "昏过去的吗！？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    OP_0D()

    ChrTalk(    #14
        0x102,
        "#1032F#5P没办法……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12A, 11)
    SetChrSubChip(0x12A, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x129, 9)
    SetChrSubChip(0x129, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0x146,
        "#214F#6P就让它们乖乖地睡一觉吧！\x02",
    )

    CloseMessageWindow()

    def lambda_C8D():
        OP_6D(-11680, 4000, -4390, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C8D)

    def lambda_CA5():
        OP_6B(2500, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CA5)

    def lambda_CB5():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB5)
    SetChrChipByIndex(0xA, 16)

    def lambda_CD5():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CD5)
    Sleep(50)

    def lambda_CF5():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_CF5)
    SetChrChipByIndex(0xB, 16)

    def lambda_D15():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_D15)
    Sleep(50)
    SetChrFlags(0x146, 0x1000)
    SetChrChipByIndex(0x146, 8)

    def lambda_D3F():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_D3F)
    SetChrChipByIndex(0xC, 16)

    def lambda_D5F():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D5F)
    Sleep(50)

    def lambda_D7F():
        OP_90(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_D7F)
    SetChrChipByIndex(0xD, 16)

    def lambda_D9F():
        OP_90(0xFE, 0x1F4, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D9F)
    Sleep(200)
    OP_44(0x102, 0xFF)
    OP_44(0x146, 0xFF)
    OP_44(0x129, 0xFF)
    OP_44(0x12A, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Battle(0xA6, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_911 end

    def Function_18_DE7(): pass

    label("Function_18_DE7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x146, 65535)
    SetChrChipByIndex(0x129, 65535)
    SetChrChipByIndex(0x12A, 65535)
    OP_8C(0x102, 180, 0)
    OP_8C(0x146, 180, 0)
    OP_8C(0x129, 180, 0)
    OP_8C(0x12A, 180, 0)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    Call(0, 33)
    SetChrPos(0x102, -12270, 4000, -1460, 0)
    SetChrPos(0x146, -12610, 4000, 500, 0)
    SetChrPos(0x129, -11560, 4000, 690, 0)
    SetChrPos(0x12A, -11070, 4000, -1280, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x146, 65535)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x12A, 65535)
    SetChrSubChip(0x12A, 0)
    SetChrChipByIndex(0x129, 65535)
    SetChrSubChip(0x129, 0)
    OP_6D(-11090, 4000, -1010, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(147000, 0)
    OP_6E(322, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x146,
        "#210F#6P哈哈，搞定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#1035F#2P一定很快还会有后援来。\x02\x03",

            "#1030F这里由我来挡住，\x01",
            "拜托你们，准备出发吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F69():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_F69)
    Sleep(50)

    def lambda_F7C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_F7C)
    Sleep(50)
    OP_8C(0x146, 180, 400)

    ChrTalk(    #18
        0x129,
        "#196F#6P哦哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12A,
        "#202F#5P交给我们吧！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_48()
    OP_8C(0x129, 90, 500)

    def lambda_FD1():
        OP_6D(-7230, 4000, -1520, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FD1)
    OP_43(0x129, 0x1, 0x0, 0x14)
    OP_8C(0x12A, 90, 500)
    OP_8C(0x146, 90, 500)
    OP_8C(0x102, 90, 500)
    Sleep(500)
    OP_43(0x12A, 0x1, 0x0, 0x15)
    Sleep(1000)
    OP_6D(-10160, 4000, -1430, 1500)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #20
        0x102,
        (
            "#1034F#2P乔丝特……\x01",
            "你不走吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x146, 180, 400)

    ChrTalk(    #21
        0x146,
        (
            "#210F#6P发动『山猫号』\x01",
            "有哥哥他们在就行了。\x02\x03",

            "我要在这里\x01",
            "支援你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        "#1032F#2P但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x146,
        (
            "#211F#6P嘿嘿……\x02\x03",

            "虽然总是装得很酷，\x01",
            "不过你还是太嫩了点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1034F#2P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x146,
        (
            "#210F#6P就因为\x01",
            "你救了我们……\x02\x03",

            "所以从没想过我们会\x01",
            "抛弃你自己逃走吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1031F#2P……我看人的眼光\x01",
            "还是挺准的。\x02\x03",

            "特别是像你们这样\x01",
            "的老好人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x146,
        "#216F#6P你，你才是老好人吧。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -13110, 4000, -15810, 0)

    NpcTalk(    #28
        0x8,
        "男人的声音",
        (
            "#3P哎呀呀……\x01",
            "还以为是谁在吵闹呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1240():
        OP_8C(0xFE, 192, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1240)
    Sleep(50)

    def lambda_1253():
        OP_8C(0xFE, 192, 500)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1253)
    OP_20(0x7D0)

    def lambda_1266():
        OP_8E(0xFE, 0xFFFFCF22, 0xFA0, 0xFFFFE0C0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1266)
    OP_6D(-11750, 4000, -5000, 2000)

    ChrTalk(    #29
        0x146,
        "#213F#6P哎……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x0)

    ChrTalk(    #30
        0x8,
        (
            "#277F#2P『卡普亚空贼团』……\x01",
            "竟然在这时候出现了吗。\x02\x03",

            "而且没想到连你也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1035F#1P……想起来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x146,
        (
            "#216F#6P这，这里怎么会\x01",
            "有埃雷波尼亚军人！？\x02\x03",

            "是你认识的吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#1030F#1P……见过而已。\x02\x03",

            "大概是在互不侵犯条约之前\x01",
            "来接收飞船的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#270F#2P如你所料。\x02\x03",

            "#272F就算这艘船被夺走，\x01",
            "对我们来说也是无关紧要……\x02\x03",

            "不过既然碰上了，\x01",
            "也不能就这么放过。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_0D()
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 1)
    OP_22(0x1F9, 0x0, 0x64)
    OP_99(0x8, 0x1, 0x6, 0x7D0)
    OP_1D(0x33)
    Sleep(500)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #35
        0x8,
        (
            "#270F#5P让我重新报上名号吧。\x02\x03",

            "我是帝国军第７机甲师团所属──\x01",
            "穆拉·范德尔少校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x146,
        "#212F#8P呜……！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x102,
        (
            "#1032F#6P小心……\x01",
            "看来这不是个容易对付的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#272F#5P应该不及你吧。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #39
        0x8,
        "#271F#5P#3S上吧！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_159D():
        OP_6D(-12230, 4000, -4280, 300)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_159D)

    def lambda_15B5():
        OP_6B(2480, 300)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15B5)
    SetChrChipByIndex(0x8, 14)
    SetChrFlags(0x8, 0x1000)

    def lambda_15CF():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15CF)
    Sleep(10)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x102, 6)

    def lambda_15F9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15F9)
    Sleep(50)
    SetChrFlags(0x146, 0x1000)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 8)

    def lambda_1628():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1628)
    Sleep(100)
    RemoveParty(0x28, 0xFF)
    RemoveParty(0x29, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x146, 0xFF)
    OP_44(0x8, 0xFF)
    Battle(0xA8, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_DE7 end

    def Function_19_1684(): pass

    label("Function_19_1684")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    Call(0, 33)
    AddParty(0x28, 0xFF, 0xFF)
    AddParty(0x29, 0xFF, 0xFF)
    OP_44(0x102, 0x1)
    OP_44(0x146, 0x1)
    OP_44(0x8, 0x1)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x146, 0x1000)
    ClearChrFlags(0x8, 0x1000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x129, 0x80)
    SetChrFlags(0x12A, 0x80)
    Call(0, 33)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x146, 7)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 6)
    SetChrPos(0x102, -12270, 4000, -1460, 180)
    SetChrPos(0x146, -12610, 4000, 500, 180)
    SetChrPos(0x8, -12510, 4000, -8000, 0)
    OP_6D(-12170, 4000, -6200, 0)
    OP_67(0, 3810, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(175000, 0)
    OP_6E(322, 0)
    OP_A3(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1770"),
        (1, "loc_1776"),
        (SWITCH_DEFAULT, "loc_177C"),
    )


    label("loc_1770")

    OP_A2(0x0)
    Jump("loc_177C")

    label("loc_1776")

    OP_A3(0x0)
    Jump("loc_177C")

    label("loc_177C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◆赢了对穆拉的战斗】\x01",      # 0
            "【◆输了对穆拉的战斗】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17E6"),
        (1, "loc_17EC"),
        (SWITCH_DEFAULT, "loc_17F2"),
    )


    label("loc_17E6")

    OP_A2(0x0)
    Jump("loc_17F2")

    label("loc_17EC")

    OP_A3(0x0)
    Jump("loc_17F2")

    label("loc_17F2")

    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1837")

    ChrTalk(    #40
        0x146,
        (
            "#214F#8P呼呼……\x02\x03",

            "为、为什么打不倒！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_185F")

    label("loc_1837")


    ChrTalk(    #41
        0x146,
        (
            "#215F#8P呜……\x02\x03",

            "不行……太强了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185F")


    ChrTalk(    #42
        0x102,
        (
            "#1035F#6P好厉害的高手……\x01",
            "而且姓范德尔吗。\x02\x03",

            "#1031F奥利维尔的真正身份，\x01",
            "我大概已经猜出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#272F#5P如果要这么说的话，\x01",
            "你的真正身份也实在令人吃惊。\x02\x03",

            "#270F『哈梅尔』的遗孤，\x01",
            "约修亚·阿斯特雷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#1034F#6P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x146,
        "#213F#8P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#276F#5P果然是吗……\x02\x03",

            "那个吊儿郎当的家伙，\x01",
            "直觉有时候还挺准的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1038F#6P………………………………\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp056_00.eff")
    PlayEffect(0x0, 0x1, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x117, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x146,
        "#216F#8P约，约修亚！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1038F#6P可以告诉我吗……\x02\x03",

            "为什么你们\x01",
            "会知道那件事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#272F#5P看来这句话让你\x01",
            "认真起来了呢……\x02\x03",

            "#270F那么我也全力迎战吧。\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp057_00.eff")
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x117, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x146, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #51
        0x146,
        "#216F#8P慢，慢着……！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_43(0x12A, 0x0, 0x0, 0x1F)
    Sleep(1000)
    OP_62(0x146, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x146, 65535)
    OP_8C(0x146, 90, 400)

    def lambda_1BC1():
        OP_6D(-7530, 6580, -2230, 8000)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_1BC1)

    def lambda_1BD9():
        OP_67(0, 6340, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1BD9)

    def lambda_1BF1():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x146, 2, lambda_1BF1)

    def lambda_1C01():
        OP_6E(603, 8000)
        ExitThread()

    QueueWorkItem(0x146, 3, lambda_1C01)

    def lambda_1C11():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_1C11)
    WaitChrThread(0x12A, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x0, 160)
    OP_70(0x0, 0x50)
    OP_73(0x0)
    Sleep(200)
    ClearChrFlags(0x12A, 0x80)
    SetChrFlags(0x12A, 0x4)
    SetChrPos(0x12A, -3020, 9000, -1200, 270)
    OP_8F(0x12A, 0xFFFFF434, 0x251C, 0xFFFFFB50, 0x7D0, 0x0)
    OP_82(0x4, 0x2)
    WaitChrThread(0x146, 0x0)
    Sleep(500)

    ChrTalk(    #52
        0x12A,
        (
            "#201F#6P准备完毕了！\x02\x03",

            "你们俩快跳上来！\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    Sleep(300)
    OP_82(0x2, 0x2)
    Sleep(300)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    Sleep(200)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x102, 90, 400)
    OP_8C(0x8, 45, 400)

    ChrTalk(    #53
        0x146,
        "#210F#5P嗯！\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    def lambda_1CFD():
        OP_8F(0x12A, 0xFFFFF434, 0x2328, 0xFFFFFB50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12A, 1, lambda_1CFD)
    Fade(500)
    OP_6D(-10520, 4000, -1950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(1720, 0)
    OP_6C(145000, 0)
    OP_6E(603, 0)
    PlayEffect(0x1, 0x4, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_1D8F():
        OP_8F(0x11, 0xFFFFF63C, 0x1F4, 0x9C4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_1D8F)

    def lambda_1DAA():
        OP_8F(0x12, 0xFFFFF63C, 0x1F4, 0x9C4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_1DAA)
    WaitChrThread(0x12A, 0x1)
    OP_6F(0x0, 80)
    OP_70(0x0, 0xA0)
    OP_23(0x6A)
    OP_22(0xE6, 0x0, 0x64)
    SetChrFlags(0x12A, 0x80)
    OP_48()
    SetChrFlags(0x146, 0x4)
    SetChrBattleFlags(0x146, 0x20)
    OP_8F(0x146, 0xFFFFD562, 0xFA0, 0xFFFFFF1A, 0x1388, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x146, 22)
    SetChrSubChip(0x146, 5)
    OP_96(0x146, 0xFFFFE08E, 0x14D2, 0x28, 0x7D0, 0x1388)
    SetChrChipByIndex(0x146, 65535)
    SetChrSubChip(0x146, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x146, 0x4)
    OP_8E(0x146, 0xFFFFEDA4, 0x17A2, 0xFFFFFD80, 0xFA0, 0x0)
    OP_8C(0x146, 270, 400)

    ChrTalk(    #54
        0x146,
        (
            "#214F#3P喂！\x01",
            "在干什么！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        "#1033F#6P………呜…………\x02",
    )

    CloseMessageWindow()

    def lambda_1E95():
        OP_6D(-10520, 4000, -9000, 4000)
        ExitThread()

    QueueWorkItem(0x12A, 0, lambda_1E95)
    OP_43(0x11, 0x1, 0x0, 0x1E)
    OP_43(0xE, 0x1, 0x0, 0x16)
    OP_43(0xF, 0x1, 0x0, 0x18)
    OP_43(0x10, 0x1, 0x0, 0x19)
    OP_43(0x9, 0x1, 0x0, 0x1B)
    OP_8C(0x146, 180, 400)

    def lambda_1ED7():

        label("loc_1ED7")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1ED7")

    QueueWorkItem2(0x8, 1, lambda_1ED7)
    OP_8E(0x102, 0xFFFFD6F2, 0xFA0, 0xFFFFF830, 0x1388, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrBattleFlags(0x102, 0x20)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x102, 21)
    SetChrSubChip(0x102, 5)

    def lambda_1F15():
        OP_96(0x102, 0xFFFFE2B4, 0x1770, 0xFFFFF830, 0x8FC, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F15)
    WaitChrThread(0x102, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    ClearChrFlags(0x102, 0x4)
    OP_8C(0x102, 180, 600)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 23)
    SetChrSubChip(0x102, 3)
    Sleep(500)
    OP_44(0x12A, 0x0)
    Fade(250)
    OP_6D(-5290, 6330, -19870, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(145000, 0)
    OP_6E(466, 0)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)

    def lambda_1FBC():

        label("loc_1FBC")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1FBC")

    QueueWorkItem2(0xE, 1, lambda_1FBC)

    def lambda_1FCD():

        label("loc_1FCD")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1FCD")

    QueueWorkItem2(0xF, 1, lambda_1FCD)

    def lambda_1FDE():

        label("loc_1FDE")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1FDE")

    QueueWorkItem2(0x10, 1, lambda_1FDE)

    ChrTalk(    #56 op#A op#5
        0xE,
        "#4A#6P什么！？\x05\x02",
    )

    Sleep(400)

    ChrTalk(    #57 op#A op#5
        0xF,
        "#15A#5P别，别想逃！\x05\x02",
    )

    Sleep(1500)
    WaitChrThread(0x9, 0x1)

    def lambda_202A():

        label("loc_202A")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_202A")

    QueueWorkItem2(0x9, 1, lambda_202A)
    OP_43(0xE, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0xF, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x10, 0x2, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x9, 0x2, 0x0, 0x1D)

    ChrTalk(    #58 op#A op#5
        0x9,
        (
            "#25A#153F#4P哇哇～！\x01",
            "最佳镜头～！\x05\x02",
        )
    )

    Sleep(1000)
    WaitChrThread(0x11, 0x1)
    OP_20(0xBB8)
    FadeToDark(2500, 0, -1)
    OP_0D()
    OP_6D(-11550, 6400, -22050, 0)
    OP_67(0, 3700, -10000, 0)
    OP_6B(3970, 0)
    OP_6C(157000, 0)
    OP_6E(262, 0)
    OP_44(0xE, 0x2)
    OP_44(0xF, 0x2)
    OP_44(0x10, 0x2)
    OP_44(0x9, 0x2)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x146, 0x80)
    SetChrFlags(0x129, 0x80)
    SetChrFlags(0x12A, 0x80)
    Sleep(2000)
    OP_1D(0x54)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0xE,
        "可恶！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xF,
        "#5P队长怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        "联络哈肯大门！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 1)
    SetChrChipByIndex(0xF, 1)
    SetChrChipByIndex(0x10, 1)
    SetChrChipByIndex(0x9, 3)

    def lambda_216E():
        OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0xFFFF6DAC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_216E)
    Sleep(100)
    OP_43(0xE, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x10, 0x1, 0x0, 0x1A)
    Sleep(2000)

    def lambda_21A6():
        OP_6D(-14870, 6400, -19960, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_21A6)

    def lambda_21BE():
        OP_67(0, 6180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_21BE)

    def lambda_21D6():
        OP_6B(3550, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_21D6)
    OP_6E(215, 3000)
    SetMapFlags(0x2000000)

    ChrTalk(    #62
        0x9,
        (
            "#154F哎呀呀～……？\x02\x03",

            "刚才那个男孩子\x01",
            "好像在哪里见过的样子～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #63
        0x9,
        (
            "#153F哇哇，怎么回事～！？\x02\x03",

            "#152F要，要和奈尔前辈\x01",
            "商量才行……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1305   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_1684 end

    def Function_20_22BE(): pass

    label("Function_20_22BE")

    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_8C(0xFE, 90, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xFFFFD6FC, 0xFA0, 0x370, 0xFA0, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    OP_96(0xFE, 0xFFFFE0C0, 0x14D2, 0xC8, 0x7D0, 0xFA0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEBB0, 0x1770, 0x46A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEEBC, 0x15AE, 0xFFFFF98E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3C)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFF51A, 0x15AE, 0xFFFFF93E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_22BE end

    def Function_21_238D(): pass

    label("Function_21_238D")

    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_8E(0xFE, 0xFFFFD6D4, 0xFA0, 0xFFFFFCE0, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)
    OP_96(0xFE, 0xFFFFE0C0, 0x14D2, 0xC8, 0x7D0, 0xFA0)
    SetChrChipByIndex(0xFE, 65535)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFEB6A, 0x1770, 0x37A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFEC1E, 0x178E, 0x17C, 0xBB8, 0x0)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFEE94, 0x15AE, 0xFFFFF7FE, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF51A, 0x15AE, 0xFFFFF93E, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Sleep(200)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_23(0x6A)
    OP_22(0xE6, 0x0, 0x64)
    Return()

    # Function_21_238D end

    def Function_22_246C(): pass

    label("Function_22_246C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2493():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2493)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD2A6, 0xFA0, 0xFFFFB136, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_22_246C end

    def Function_23_24CF(): pass

    label("Function_23_24CF")

    OP_8E(0xFE, 0xFFFFD120, 0xFA0, 0xFFFFDCD8, 0xFA0, 0x0)

    label("loc_24E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2507")
    OP_8C(0xFE, 225, 400)
    Sleep(1000)
    OP_8C(0xFE, 325, 400)
    Sleep(1000)
    Jump("loc_24E3")

    label("loc_2507")

    Return()

    # Function_23_24CF end

    def Function_24_2508(): pass

    label("Function_24_2508")

    Sleep(500)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2534():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2534)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFD1C0, 0xFA0, 0xFFFFA808, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_24_2508 end

    def Function_25_2570(): pass

    label("Function_25_2570")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_259C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_259C)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFCC48, 0xFA0, 0xFFFFB096, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_25_2570 end

    def Function_26_25D8(): pass

    label("Function_26_25D8")

    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFBD5C, 0xFA0, 0xFFFFDD82, 0xFA0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_25D8 end

    def Function_27_2606(): pass

    label("Function_27_2606")

    Sleep(1000)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17060, 0, -8830, 0)

    def lambda_2632():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2632)
    OP_8E(0xFE, 0xFFFFBD34, 0xFA0, 0xFFFFBE38, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFCA22, 0xFA0, 0xFFFFA90C, 0x1770, 0x0)
    TurnDirection(0xFE, 0x11, 400)
    Return()

    # Function_27_2606 end

    def Function_28_266E(): pass

    label("Function_28_266E")

    SetChrChipByIndex(0xFE, 18)

    label("loc_2673")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26A0")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(500)
    Jump("loc_2673")

    label("loc_26A0")

    Return()

    # Function_28_266E end

    def Function_29_26A1(): pass

    label("Function_29_26A1")

    LoadEffect(0x0, "map\\\\mp032_00.eff")
    SetChrChipByIndex(0xFE, 4)

    label("loc_26BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2705")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_26BA")

    label("loc_2705")

    Return()

    # Function_29_26A1 end

    def Function_30_2706(): pass

    label("Function_30_2706")


    def lambda_270C():
        OP_8F(0xFE, 0xFFFFF63C, 0x1F4, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_270C)

    def lambda_2727():
        OP_8F(0xFE, 0xFFFFF63C, 0x1F4, 0xFFFFF63C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2727)
    Sleep(500)

    def lambda_2747():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2747)

    def lambda_2762():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2762)
    Sleep(500)
    OP_6F(0x0, 200)
    OP_70(0x0, 0xF0)

    def lambda_2790():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2790)

    def lambda_27AB():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_27AB)
    Sleep(500)

    def lambda_27CB():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_27CB)

    def lambda_27E6():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_27E6)
    Sleep(500)

    def lambda_2806():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2806)

    def lambda_2821():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2821)
    Sleep(500)

    def lambda_2841():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2841)

    def lambda_285C():
        OP_8F(0xFE, 0x280, 0x1F4, 0xFFFEEC9C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_285C)
    Sleep(500)

    def lambda_287C():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_287C)

    def lambda_2897():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2897)
    Sleep(500)

    def lambda_28B7():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_28B7)

    def lambda_28D2():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_28D2)
    Sleep(500)

    def lambda_28F2():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_28F2)

    def lambda_290D():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_290D)
    Sleep(500)

    def lambda_292D():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_292D)

    def lambda_2948():
        OP_8F(0xFE, 0x280, 0x3E8, 0xFFFEEC9C, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2948)
    Sleep(500)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    OP_24(0x77, 0x5A)
    OP_24(0x79, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x79, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x79, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x79, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x79, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x79, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x79, 0x1E)
    Sleep(100)
    OP_24(0x77, 0x14)
    OP_24(0x79, 0x14)
    Sleep(100)
    OP_24(0x77, 0xA)
    OP_24(0x79, 0xA)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x79)
    OP_82(0x4, 0x0)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    Return()

    # Function_30_2706 end

    def Function_31_29F5(): pass

    label("Function_31_29F5")

    PlayEffect(0x1, 0x4, 0x12, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_24(0x79, 0x46)
    Sleep(500)
    OP_24(0x79, 0x50)
    Sleep(500)
    OP_24(0x79, 0x5A)
    Sleep(500)
    OP_24(0x79, 0x64)
    Sleep(500)
    SetChrFlags(0x11, 0x4)
    OP_22(0x77, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x0, 160)
    OP_70(0x0, 0xC8)

    def lambda_2A76():
        OP_8F(0x11, 0xFFFFFBDC, 0x3E8, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_2A76)

    def lambda_2A91():
        OP_8F(0x12, 0xFFFFFBDC, 0x0, 0x0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_2A91)
    WaitChrThread(0x129, 0x1)
    WaitChrThread(0x129, 0x2)
    Sleep(300)

    def lambda_2ABB():
        OP_8C(0xFE, 315, 5)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2ABB)

    def lambda_2AC9():
        OP_8C(0xFE, 315, 5)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2AC9)
    Sleep(400)

    def lambda_2ADC():
        OP_8C(0xFE, 270, 8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2ADC)

    def lambda_2AEA():
        OP_8C(0xFE, 270, 8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2AEA)
    Sleep(400)

    def lambda_2AFD():
        OP_8C(0xFE, 270, 10)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2AFD)

    def lambda_2B0B():
        OP_8C(0xFE, 270, 10)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B0B)
    Sleep(400)

    def lambda_2B1E():
        OP_8C(0xFE, 225, 13)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2B1E)

    def lambda_2B2C():
        OP_8C(0xFE, 225, 13)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B2C)
    Sleep(400)

    def lambda_2B3F():
        OP_8C(0xFE, 225, 15)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2B3F)

    def lambda_2B4D():
        OP_8C(0xFE, 225, 15)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B4D)
    Sleep(400)

    def lambda_2B60():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2B60)

    def lambda_2B6E():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B6E)
    Sleep(400)

    def lambda_2B81():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2B81)

    def lambda_2B8F():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2B8F)
    Sleep(400)

    def lambda_2BA2():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2BA2)

    def lambda_2BB0():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2BB0)
    Sleep(400)

    def lambda_2BC3():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2BC3)

    def lambda_2BD1():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2BD1)
    Sleep(400)

    def lambda_2BE4():
        OP_8C(0xFE, 180, 28)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2BE4)

    def lambda_2BF2():
        OP_8C(0xFE, 180, 28)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2BF2)
    Sleep(3000)

    def lambda_2C05():
        OP_8F(0x11, 0xFFFFF63C, 0x0, 0x9C4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 1, lambda_2C05)

    def lambda_2C20():
        OP_8F(0x12, 0xFFFFF63C, 0x0, 0x9C4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x129, 2, lambda_2C20)

    def lambda_2C3B():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2C3B)

    def lambda_2C49():
        OP_8C(0xFE, 180, 25)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2C49)
    Sleep(400)

    def lambda_2C5C():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2C5C)

    def lambda_2C6A():
        OP_8C(0xFE, 180, 23)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2C6A)
    Sleep(400)

    def lambda_2C7D():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2C7D)

    def lambda_2C8B():
        OP_8C(0xFE, 180, 18)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2C8B)
    Sleep(400)

    def lambda_2C9E():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2C9E)

    def lambda_2CAC():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2CAC)
    Sleep(400)

    def lambda_2CBF():
        OP_8C(0xFE, 180, 8)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_2CBF)

    def lambda_2CCD():
        OP_8C(0xFE, 180, 8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2CCD)
    Sleep(400)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x129, 0x1)
    WaitChrThread(0x129, 0x2)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(500)
    Return()

    # Function_31_29F5 end

    def Function_32_2D05(): pass

    label("Function_32_2D05")

    SetChrChipByIndex(0x8, 0)
    OP_8E(0xFE, 0xFFFFCAA4, 0xFA0, 0xFFFFC180, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBE4C, 0xFA0, 0xFFFFBDE8, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFBDB6, 0x0, 0xFFFFDC38, 0xBB8, 0x0)
    Return()

    # Function_32_2D05 end

    def Function_33_2D47(): pass

    label("Function_33_2D47")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0xB, 17)
    SetChrChipByIndex(0xC, 17)
    SetChrChipByIndex(0xD, 17)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrPos(0xA, -11960, 4000, 4040, 315)
    SetChrPos(0xB, -12210, 4000, 6160, 90)
    SetChrPos(0xC, -13650, 4000, 6030, 180)
    SetChrPos(0xD, -13510, 4000, 3710, 45)
    Return()

    # Function_33_2D47 end

    SaveToFile()

Try(main)
