from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '卡西乌斯',                             # 9
        '尤莉亚上尉',                           # 10
        '卫兵',                                 # 11
        '卫兵',                                 # 12
        '卫兵',                                 # 13
        '卫兵',                                 # 14
        '卫兵',                                 # 15
        '卫兵',                                 # 16
        '王国军军官',                           # 17
        '卫兵',                                 # 18
        '卫兵',                                 # 19
        '卫兵',                                 # 20
        '卫兵',                                 # 21
        '卫兵',                                 # 22
        '理查德',                               # 23
        '目标用照相机',                         # 24
        '',                                     # 25
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT27/CH03580 ._CH',             # 02
        'ED6_DT27/CH04580 ._CH',             # 03
        'ED6_DT27/CH04581 ._CH',             # 04
        'ED6_DT27/CH04584 ._CH',             # 05
        'ED6_DT07/CH00420 ._CH',             # 06
        'ED6_DT07/CH00421 ._CH',             # 07
        'ED6_DT07/CH00424 ._CH',             # 08
        'ED6_DT07/CH01600 ._CH',             # 09
        'ED6_DT07/CH00322 ._CH',             # 0A
        'ED6_DT07/CH00326 ._CH',             # 0B
        'ED6_DT07/CH02030 ._CH',             # 0C
        'ED6_DT07/CH00270 ._CH',             # 0D
        'ED6_DT07/CH00271 ._CH',             # 0E
        'ED6_DT07/CH00274 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT27/CH03580P._CP',             # 02
        'ED6_DT27/CH04580P._CP',             # 03
        'ED6_DT27/CH04581P._CP',             # 04
        'ED6_DT27/CH04584P._CP',             # 05
        'ED6_DT07/CH00420P._CP',             # 06
        'ED6_DT07/CH00421P._CP',             # 07
        'ED6_DT07/CH00424P._CP',             # 08
        'ED6_DT07/CH01600P._CP',             # 09
        'ED6_DT07/CH00322P._CP',             # 0A
        'ED6_DT07/CH00326P._CP',             # 0B
        'ED6_DT07/CH02030P._CP',             # 0C
        'ED6_DT07/CH00270P._CP',             # 0D
        'ED6_DT07/CH00271P._CP',             # 0E
        'ED6_DT07/CH00274P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 580,
        Z                   = 0,
        Y                   = 35150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2560,
        Z                   = 0,
        Y                   = 35260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16590,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 14750,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12780,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10840,
        Z                   = 0,
        Y                   = 29000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18730,
        Z                   = 0,
        Y                   = 27570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16470,
        Z                   = 0,
        Y                   = 29800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13160,
        Z                   = 0,
        Y                   = 29250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16250,
        Z                   = 0,
        Y                   = 27060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -13260,
        Z                   = 0,
        Y                   = 26740,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15120,
        Z                   = 0,
        Y                   = 31950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_349",          # 01, 1
        "Function_2_353",          # 02, 2
        "Function_3_3DB",          # 03, 3
        "Function_4_45C",          # 04, 4
        "Function_5_4D8",          # 05, 5
        "Function_6_4ED",          # 06, 6
        "Function_7_12D9",         # 07, 7
        "Function_8_2730",         # 08, 8
        "Function_9_2D99",         # 09, 9
        "Function_10_2DC1",        # 0A, 10
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_348")

    Return()

    # Function_0_32A end

    def Function_1_349(): pass

    label("Function_1_349")

    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_349 end

    def Function_2_353(): pass

    label("Function_2_353")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    Sleep(300)
    Jump("loc_3D7")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    Sleep(400)
    Jump("loc_3D7")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B0")
    Sleep(500)
    Jump("loc_3D7")

    label("loc_3B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    Sleep(700)
    Jump("loc_3D7")

    label("loc_3C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    Sleep(800)

    label("loc_3D7")

    Jump("Function_2_353")

    label("loc_3DA")

    Return()

    # Function_2_353 end

    def Function_3_3DB(): pass

    label("Function_3_3DB")

    LoadEffect(0x0, "battle\\\\btgun00.eff")

    label("loc_3F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 600, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x1F7)
    OP_22(0x1F7, 0x0, 0xA)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(800)
    Jump("loc_3F1")

    label("loc_45B")

    Return()

    # Function_3_3DB end

    def Function_4_45C(): pass

    label("Function_4_45C")

    LoadEffect(0x0, "battle\\\\btgun00.eff")

    label("loc_472")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D7")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 600, 900, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x1F7)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(800)
    Jump("loc_472")

    label("loc_4D7")

    Return()

    # Function_4_45C end

    def Function_5_4D8(): pass

    label("Function_5_4D8")

    OP_8E(0xFE, 0x4F10, 0x0, 0x7BAC, 0x7D0, 0x0)
    Return()

    # Function_5_4D8 end

    def Function_6_4ED(): pass

    label("Function_6_4ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, -1040, 500, 37340, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -1040, 500, 37340, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(15970, 0, 31320, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(315000, 0)
    OP_6E(300, 0)

    def lambda_59F():
        OP_6D(-3140, 0, 32590, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_59F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2820, 0, 36480, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(310, 0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x9)
    OP_73(0x1)
    Sleep(300)

    def lambda_675():
        OP_6D(-2820, 0, 31860, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_675)

    def lambda_68D():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x66BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_68D)
    Sleep(1500)

    def lambda_6AD():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x8110, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_6AD)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #0
        0x10A,
        (
            "#813F#11P（说要让我到外面来……\x01",
            "　到底打算干什么呢。）\x02\x03",

            "（而且，卡西乌斯先生……\x01",
            "　好像正在招呼着什么人……）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #1
        0x10,
        (
            "#1120F#12P哦，来了啊。\x02\x03",

            "已经准备好了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7D6():
        OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x6F54, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_7D6)
    ClearChrFlags(0x1E, 0x80)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1E, -8820, 0, 24400, 90)

    NpcTalk(    #2
        0x1E,
        "男人的声音",
        "#2P嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x1E,
        "男人的声音",
        (
            "#2P不过，没有想到\x01",
            "能再一次穿上这身军装……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x1E,
        "男人的声音",
        "#2P真是的，准将您也真喜欢恶作剧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#1121F#12P哈哈，不要这么说。\x02\x03",

            "#1120F要是穿平时的衣服的话，\x01",
            "战斗起来就不方便了吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x0)
    SetChrPos(0x1E, -10820, 0, 27400, 90)
    OP_9F(0x1E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_44(0x1F, 0x0)

    def lambda_940():
        OP_6D(-12220, 0, 27400, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_940)

    def lambda_958():
        OP_6C(270000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_958)

    def lambda_968():
        OP_6B(2680, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_968)

    def lambda_978():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_978)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    OP_6F(0x1, 0)

    ChrTalk(    #6
        0x10A,
        "#1317F#5P#3S理、理查德上校！？#2S\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()

    def lambda_9D7():
        OP_6D(-4059, 0, 27400, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_9D7)

    def lambda_9EF():
        OP_67(0, 4460, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_9EF)

    def lambda_A07():
        OP_6B(2780, 3500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_A07)

    def lambda_A17():
        OP_8E(0xFE, 0xFFFFF04D, 0x0, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_A17)
    Sleep(2500)

    def lambda_A37():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_A37)

    def lambda_A45():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_A45)
    WaitChrThread(0x1E, 0x0)
    Sleep(300)
    OP_8C(0x1E, 45, 400)
    Sleep(500)

    ChrTalk(    #7
        0x1E,
        (
            "#115F#5P虽然穿成这个样子\x01",
            "说这句话有些奇怪……\x02\x03",

            "#110F不过，我已经不是上校了。\x01",
            "游击士小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#1316F#12P对、对不起。\x02\x03",

            "#818F理、理查德……先生？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1E,
        (
            "#110F#5P嗯，我记得\x01",
            "你就是正游击士亚妮拉丝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10A,
        "#814F#12P您、您知道我的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1E,
        (
            "#119F#5P我也算是曾经的\x01",
            "情报部司令啊。\x02\x03",

            "#111F国内游击士的情况\x01",
            "基本上都有所掌握。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        (
            "#819F#12P原、原来如此……\x02\x03",

            "#1317F但、但是，为什么您会在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1120F#6P实际上理查德就是\x01",
            "在你之前我要会面的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10A,
        "#814F#12P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1E,
        (
            "#119F#5P其实，这次我准备\x01",
            "在民间成立一个调查公司。\x02\x03",

            "由于工作的关系，\x01",
            "今后多少也会和王国军有所交往……\x02\x03",

            "#110F这次就是为了\x01",
            "先打下招呼而来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10A,
        (
            "#1310F#12P咦……\x01",
            "是这样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x10A,
        (
            "#814F#12P难、难道……\x02\x03",

            "刚才说的\x01",
            "『代替者』……\x02",
        )
    )

    Jump("loc_DB9")

    label("loc_DB9")

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)
    Sleep(300)

    ChrTalk(    #18
        0x10,
        (
            "#1125F#5P啊啊，没错。\x02\x03",

            "#1120F接下来，就让理查德\x01",
            "和你比试比试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #19
        0x10A,
        (
            "#1317F#12P等、等一下！\x01",
            "突然说这种话也太……\x02\x03",

            "#1316F而且，\x01",
            "对手居然还是理查德上校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1122F#5P刚才那问题的答案……\x02\x03",

            "你不想知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        "#1317F#12P#3S！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1125F#5P对剑有所疑问\x01",
            "就只有用剑来回答。\x02\x03",

            "#1120F不用拘泥于胜负，\x01",
            "尽全力攻过来便是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        "#813F#12P………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #24
        0x10A,
        (
            "#812F#12P……我明白了。\x01",
            "既然卡西乌斯先生这么说……！\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)

    def lambda_1013():
        OP_96(0xFE, 0x794, 0x0, 0x6B08, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1013)

    def lambda_1031():
        OP_6D(-2210, 0, 28870, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1031)

    def lambda_1049():
        OP_6C(315000, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1049)

    def lambda_1059():
        OP_6B(2780, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1059)
    OP_8C(0x10A, 270, 0)
    OP_8C(0x1E, 90, 0)
    WaitChrThread(0x10A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x10A,
        (
            "#815F#12P就算献丑，\x01",
            "我也会尽我所能\x01",
            "挑战试试看的！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_10F4():
        OP_8F(0xFE, 0xFFFFFBF0, 0x0, 0x5FB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_10F4)
    Sleep(500)

    ChrTalk(    #26
        0x1E,
        (
            "#115F#5P呵，你的剑法传承自\x01",
            "作为『剑圣』剑术之原点的那位高人…………\x02\x03",

            "#112F我可要好好地见识一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 13)
    SetChrSubChip(0x1E, 0)
    Sleep(500)
    OP_1D(0x2B)
    Sleep(500)

    ChrTalk(    #27
        0x1E,
        "#114F#5P#3S……上了！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x10A,
        "#815F#3S#12P是！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_1228():
        OP_6B(2300, 200)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1228)

    def lambda_1238():
        OP_91(0xFE, 0xFFFFF060, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1238)
    SetChrChipByIndex(0x1E, 14)

    def lambda_1258():
        OP_91(0xFE, 0xFA0, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_1258)
    WaitChrThread(0x1F, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x1E, 0x0)
    OP_41(0x9, 0x0, 0xFF)
    OP_31(0x9, 0x10, 0x5A)
    OP_31(0x9, 0x5, 0xC8)
    OP_31(0x9, 0xFE, 0x0)
    OP_35(0x9, 0xFFFF)
    OP_34(0x9, 0xFFFF)
    OP_35(0x9, 0x0)
    OP_BB(0x9, 0x6, 0x110)
    OP_37(0x9, 0x7F, 0x0)
    OP_37(0x9, 0x7F, 0x2)
    OP_41(0x9, 0x3E8, 0xFF)
    OP_34(0x9, 0x82)
    OP_34(0x9, 0x83)
    OP_34(0x9, 0x33)
    OP_34(0x9, 0xB)
    OP_34(0x9, 0x47)
    OP_3E(0x207, 2)
    Battle(0x39C, 0x300003, 0x0, 0x0, 0xFF)
    Call(0, 7)
    Return()

    # Function_6_4ED end

    def Function_7_12D9(): pass

    label("Function_7_12D9")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x9, 0xFC, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x1E, 0x0)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3270, 0, 20110, 270)
    OP_6D(2090, 0, 20150, 0)
    OP_67(0, 4620, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(90000, 0)
    OP_6E(300, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13AF"),
        (1, "loc_13BC"),
        (SWITCH_DEFAULT, "loc_13C9"),
    )


    label("loc_13AF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C9")

    label("loc_13BC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13C9")

    label("loc_13C9")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13E3"),
        (1, "loc_153E"),
        (SWITCH_DEFAULT, "loc_168D"),
    )


    label("loc_13E3")

    SetChrPos(0x10A, -1210, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x800)
    SetChrPos(0x1E, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x1E, 15)
    SetChrSubChip(0x1E, 3)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10A,
        (
            "#1316F#5P呼、呼……\x02\x03",

            "#1314F……成、成功了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x1E,
        (
            "#119F#12P哎呀哎呀……\x01",
            "我也还差得很远呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1125F#5P好，到此为止。\x02\x03",

            "#1122F你们俩都把剑收起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x1E, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 12)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_168D")

    label("loc_153E")

    SetChrPos(0x10A, -1210, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 8)
    SetChrSubChip(0x10A, 3)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x800)
    SetChrPos(0x1E, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x1E, 13)
    SetChrSubChip(0x1E, 0)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x10A,
        (
            "#1312F#6P痛、痛痛……\x02\x03",

            "#813F……被、被打败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1E,
        "#110F#11P唔……真令人吃惊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "#1125F#5P好，到此为止。\x02\x03",

            "#1122F你们俩都把剑收起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1E, 12)
    SetChrSubChip(0x1E, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_168D")

    label("loc_168D")

    OP_1D(0xF)

    def lambda_1695():
        OP_6D(720, 0, 18750, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1695)

    def lambda_16AD():
        OP_67(0, 4620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_16AD)

    def lambda_16C5():
        OP_6B(2960, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_16C5)

    def lambda_16D5():
        OP_6C(135000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_16D5)

    def lambda_16E5():
        OP_6E(300, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16E5)
    OP_8E(0x10, 0x4D8, 0x0, 0x4C9A, 0x5DC, 0x0)
    WaitChrThread(0x1F, 0x0)
    Sleep(300)
    TurnDirection(0x10, 0x10A, 400)
    Sleep(500)

    ChrTalk(    #35
        0x10,
        (
            "#1120F#5P亚妮拉丝……\x02\x03",

            "理查德的剑，\x01",
            "在你眼中看来怎样？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10A, 0x10, 500)

    ChrTalk(    #36
        0x10A,
        (
            "#812F#6P啊，是……\x02\x03",

            "#817F八叶一刀流——第五型『残月』……\x02\x03",

            "#816F虽然加入了些许调整，\x01",
            "不过还是以拔刀术为基础的招式吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #37
        0x10A,
        (
            "#813F#6P不对，应该不是\x01",
            "这种表面化的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#1120F#5P唔，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        (
            "#817F#6P刚才战斗时我发觉到……\x02\x03",

            "理查德先生好像\x01",
            "在配合我的步调挥剑……\x02\x03",

            "对，\x01",
            "正是在我发动攻击\x01",
            "那个瞬间的步调……\x02\x03",

            "#813F怎么说呢，\x01",
            "理查德先生的刀法\x01",
            "充满『包容』的姿势……\x02\x03",

            "#816F这个姿势\x01",
            "和『型』完全吻合，\x01",
            "很自然就使出了强力的『剑』。\x02",
        )
    )

    Jump("loc_19A4")

    label("loc_19A4")

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "#1124F#5P哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x1E,
        "#110F#11P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10A,
        (
            "#813F#6P但是，为什么理查德先生\x01",
            "要执着于『包容』呢……\x02\x03",

            "当然，\x01",
            "我觉得是为了保护什么……\x02",
        )
    )

    Jump("loc_1A4F")

    label("loc_1A4F")

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #43
        0x1E,
        "#119F#11P……亚妮拉丝。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A)
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10A, 0x1E, 500)

    ChrTalk(    #44
        0x10A,
        "#1317F#6P是、是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x1E,
        (
            "#115F#11P我挥剑的理由只有一个。\x02\x03",

            "#110F那就是――\x01",
            "守护这个国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#814F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x1E,
        (
            "#119F#11P无论是谁，\x01",
            "都必定有各自想要守护的东西。\x02\x03",

            "那或许是家人和恋人\x01",
            "这种具体的存在……\x02\x03",

            "又或者是信念和理念\x01",
            "这种无形的东西。\x02\x03",

            "#110F而对于如何去守护的\x01",
            "『理念』也因人而异。\x02\x03",

            "而我的『理念』形式与\x01",
            "你所指出的『包容』之剑\x01",
            "恰巧一致。\x02\x03",

            "#495F哈哈，虽然由我这个\x01",
            "将国家逼入绝境的大罪人\x01",
            "说出这样的话来好像很奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10A,
        "#813F#6P那、那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#1128F#5P……理查德。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1E,
        (
            "#119F#11P准将……\x01",
            "请不必多说。\x02\x03",

            "就算得到陛下赦免，\x01",
            "我的罪孽却还未偿还。\x02\x03",

            "#110F然而，就像您一样，\x01",
            "我无法舍弃报国之心。\x02\x03",

            "正因此，\x01",
            "我更坚定了离开军队的决心。\x02",
        )
    )

    Jump("loc_1DA8")

    label("loc_1DA8")

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#1317F#6P咦………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1E,
        (
            "#115F#11P亚妮拉丝……\x02\x03",

            "我认为，\x01",
            "在『理念』面前，\x01",
            "立场也不过是一种手段。\x02\x03",

            "#111F……而这种说法，\x01",
            "对于武器\x01",
            "或许也同样适用。\x02",
        )
    )

    Jump("loc_1E71")

    label("loc_1E71")

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        "#814F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1125F#5P重要的是，\x01",
            "将何种『理念』寄托其上――\x02\x03",

            "我抛弃剑而选择棒术，\x01",
            "也不过是因为\x01",
            "『理念』的形式有所改变。\x02\x03",

            "#1120F因此，亚妮拉丝……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 300)
    Sleep(400)

    ChrTalk(    #55
        0x10A,
        (
            "#817F#6P我也将自己的『理念』\x01",
            "寄托于自己的剑就好……\x02\x03",

            "#1314F……是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#1121F#5P哦，被抢先了。\x02\x03",

            "#1120F不愧是云老师的孙女啊。\x01",
            "真是机灵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10A,
        (
            "#819F#6P嘿嘿，\x01",
            "不过倒是忘的也快。\x02\x03",

            "#1314F但是，卡西乌斯先生的心情……\x01",
            "我觉得终于能够明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1125F#5P是吗……\x02\x03",

            "#1120F呵呵，那就好。\x02\x03",

            "麻烦你，也替我\x01",
            "转达给云老师行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10A,
        (
            "#816F#6P是，包在我身上！\x02\x03",

            "爷爷一定\x01",
            "也能明白的。\x02",
        )
    )

    Jump("loc_210C")

    label("loc_210C")

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_211A"),
        (SWITCH_DEFAULT, "loc_25CC"),
    )


    label("loc_211A")


    ChrTalk(    #60
        0x10,
        (
            "#1125F#5P唔，对了……\x02\x03",

            "#1128F……理查德，那个没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x1E,
        (
            "#119F#11P呵呵……那当然。\x02\x03",

            "#111F……而且，\x01",
            "我已经继承了您的剑之道。\x02\x03",

            "这个东西，\x01",
            "让她拿着再合适不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        "#814F#6P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1121F#5P……就是这样。\x02\x03",

            "#1120F亚妮拉丝，能收下这个吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_2259():
        OP_6D(260, 0, 19210, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2259)
    OP_8F(0x10, 0xFFFFFF10, 0x0, 0x5280, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x07\x00得到了\x1F\x90\x05\x07\x00。\x02",
    )

    Jump("loc_22B5")

    label("loc_22B5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_A2(0x2FA6)
    OP_8F(0x10, 0x15E, 0x0, 0x4F74, 0x5DC, 0x0)

    ChrTalk(    #65
        0x10A,
        "#1317F#6P这、这是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#1125F#5P这曾经是我的爱刀。\x02\x03",

            "#1120F我想，让选择剑之道的人\x01",
            "拿着它会更好一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10A,
        (
            "#1317F#6P请、请等一下！\x02\x03",

            "这我不能接受。\x02\x03",

            "#813F这是……那个……\x01",
            "理查德先生才应该……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x1E,
        (
            "#115F#11P……重要的\x01",
            "并不是表面可见的形式。\x02\x03",

            "#110F这个刚才\x01",
            "你应该也领悟到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10A,
        (
            "#819F#6P但、但是，\x01",
            "那个和这个是两回事吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x1E,
        (
            "#119F#11P亚妮拉丝……\x01",
            "你不必想得太深。\x02\x03",

            "#110F就像刚才你自己说的，\x01",
            "你只需将自己的『理念』\x01",
            "寄托于这把刀上即可。\x02\x03",

            "就这么简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        (
            "#812F#6P我自己的『理念』……\x02\x03",

            "#813F……………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #72
        0x10A,
        (
            "#817F#6P……我明白了。\x02\x03",

            "#816F非常感谢，\x01",
            "那么我就收下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25CC")

    label("loc_25CC")


    ChrTalk(    #73
        0x1E,
        (
            "#119F#11P你的剑法\x01",
            "也让我受益匪浅。\x02\x03",

            "#110F如果有机会，\x01",
            "就再切磋切磋吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 180, 400)
    Sleep(300)

    ChrTalk(    #74
        0x10A,
        "#1314F#6P是，彼此彼此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        "#1121F#5P呵呵，要不断进步啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 400)
    Sleep(300)

    ChrTalk(    #76
        0x10A,
        (
            "#811F#6P是！\x02\x03",

            "#1310F不肖弟子亚妮拉丝·艾尔菲德――\x01",
            "今后将全身心投入，\x01",
            "向剑之道迈进！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26FA():
        OP_6B(3460, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_26FA)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_12D9 end

    def Function_8_2730(): pass

    label("Function_8_2730")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, -1040, 500, 37340, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(15970, 0, 31320, 0)
    OP_67(0, 6330, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(315000, 0)
    OP_6E(300, 0)

    def lambda_27CC():
        OP_6D(-3140, 0, 32590, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_27CC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-2060, 500, 36480, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(314000, 0)
    OP_6E(310, 0)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -220, 0, 20640, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1630, 0, 20720, 90)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x9)
    OP_73(0x1)
    Sleep(300)

    def lambda_288D():
        OP_8E(0xFE, 0xFFFFFCEA, 0x1F4, 0x8962, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_288D)
    WaitChrThread(0x10A, 0x0)
    Sleep(300)

    ChrTalk(    #77
        0x10A,
        "#810F#2P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_28CB():
        OP_6D(-2110, 0, 22520, 2500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_28CB)

    def lambda_28E3():
        OP_6B(2800, 2500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_28E3)
    WaitChrThread(0x10, 0x0)

    def lambda_28F8():
        OP_8E(0xFE, 0xFFFFFA4C, 0x0, 0x58F2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_28F8)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    Sleep(300)
    OP_8C(0x11, 0, 400)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #78
        0x10,
        (
            "#1120F哦，来啦。\x02\x03",

            "已经准备好了么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        (
            "#810F#2P是，时间正好……\x02\x03",

            "那个，为什么\x01",
            "尤莉亚小姐会在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x11,
        (
            "#170F哈哈，好久不见。\x02\x03",

            "这边有演习，\x01",
            "我刚刚回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "#1120F嗯，机会难得。\x01",
            "就工作到最后吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #82
        0x10,
        "#1120F#4P就这样，拜托了哦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #83
        0x11,
        "#170F#5P……明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #84
        0x11,
        "#170F那么就来场比试吧。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x10A,
        (
            "#810F#2P咦，比试……\x02\x03",

            "难、难道跟我？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 400)

    ChrTalk(    #86
        0x10,
        (
            "#1120F喂喂……\x02\x03",

            "除了你以外\x01",
            "哪里还有别人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        "#810F#2P但、但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "#1120F刚才那问题的答案……\x02\x03",

            "你不想知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10A,
        "#810F#2P！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "#1120F对剑有所疑问\x01",
            "就只有用剑来回答。\x02\x03",

            "不用拘泥于胜负，\x01",
            "尽全力攻过来便是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#810F#2P我、我明白了……\x02\x03",

            "那我就上了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    OP_0D()
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2BF0():
        OP_96(0xFE, 0xFFFFFAC4, 0x0, 0x6126, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2BF0)
    WaitChrThread(0x10A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    ChrTalk(    #92
        0x11,
        (
            "#170F呵，高人所传授的剑法……\x02\x03",

            "就让我好好见识一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    OP_0D()
    OP_43(0x10, 0x0, 0x0, 0x9)

    def lambda_2C74():
        OP_6D(-2700, 0, 22770, 1500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2C74)

    def lambda_2C8C():
        OP_67(0, 4940, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C8C)

    def lambda_2CA4():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2CA4)

    def lambda_2CB4():
        OP_6E(309, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2CB4)
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2CCE():
        OP_96(0xFE, 0xFFFFF902, 0x0, 0x49D4, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2CCE)
    WaitChrThread(0x11, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #93
        0x11,
        "#170F……上了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10A,
        "#810F#2P是！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2D35():
        OP_6B(2300, 200)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2D35)

    def lambda_2D45():
        OP_91(0xFE, 0xFFFFFED4, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2D45)
    SetChrChipByIndex(0x11, 4)

    def lambda_2D65():
        OP_91(0xFE, 0x12C, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2D65)
    WaitChrThread(0x10, 0x0)
    OP_44(0x10A, 0x0)
    OP_44(0x11, 0x0)
    Battle(0x39C, 0x300003, 0x0, 0x0, 0xFF)
    Call(0, 10)
    Return()

    # Function_8_2730 end

    def Function_9_2D99(): pass

    label("Function_9_2D99")

    OP_8C(0x10, 270, 400)

    def lambda_2DA6():
        OP_8F(0xFE, 0xA82, 0x0, 0x5604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DA6)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_9_2D99 end

    def Function_10_2DC1(): pass

    label("Function_10_2DC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10A, 0x0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3270, 0, 20110, 270)
    OP_6D(-170, 0, 21210, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2E84"),
        (1, "loc_2E91"),
        (SWITCH_DEFAULT, "loc_2E9E"),
    )


    label("loc_2E84")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E9E")

    label("loc_2E91")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E9E")

    label("loc_2E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDD")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇胜了】\x01",      # 0
            "【◇输了】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)

    label("loc_2EDD")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EF7"),
        (1, "loc_2FFC"),
        (SWITCH_DEFAULT, "loc_3101"),
    )


    label("loc_2EF7")

    SetChrPos(0x10A, -1250, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 6)
    SetChrSubChip(0x10A, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 3)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #95
        0x10A,
        (
            "#810F呼、呼……\x02\x03",

            "……成、成功了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        (
            "#170F呜……！？\x02\x03",

            "失败了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "#1120F好，到此为止。\x02\x03",

            "你们俩都把剑收起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x11, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3101")

    label("loc_2FFC")

    SetChrPos(0x10A, -1250, 0, 22350, 180)
    SetChrChipByIndex(0x10A, 8)
    SetChrSubChip(0x10A, 3)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -1210, 0, 17900, 0)
    SetChrChipByIndex(0x11, 3)
    SetChrSubChip(0x11, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #98
        0x10A,
        (
            "#810F痛、痛痛……\x02\x03",

            "……被、被打败了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x11,
        (
            "#170F呼……\x02\x03",

            "获胜了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#1120F好，到此为止。\x02\x03",

            "你们俩都把剑收起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_99(0x10A, 0x3, 0x0, 0x3E8)
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x10A, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    Jump("loc_3101")

    label("loc_3101")


    def lambda_3107():
        OP_6D(2090, 0, 20150, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3107)

    def lambda_311F():
        OP_67(0, 4620, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_311F)

    def lambda_3137():
        OP_6B(2960, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3137)

    def lambda_3147():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_3147)

    def lambda_3157():
        OP_6E(300, 1500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_3157)
    OP_8C(0x10A, 135, 400)
    Sleep(300)
    OP_8C(0x11, 45, 400)
    Sleep(300)
    WaitChrThread(0x10, 0x0)
    Sleep(300)

    ChrTalk(    #101
        0x10,
        (
            "#1120F亚妮拉丝……\x02\x03",

            "我尤莉亚的剑，\x01",
            "在你眼中看来怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10A,
        (
            "#810F#6P虽、虽然非常锐利，\x01",
            "但是，并不只是攻击……\x02\x03",

            "感觉像是为了防备敌人的攻击\x01",
            "而挥剑似的……\x02\x03",

            "好像有些不可思议的\x01",
            "太刀剑法呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #103
        0x11,
        (
            "#170F原来如此……\x01",
            "你是这样看的吗。\x02\x03",

            "事实或许就是这样。\x02\x03",

            "我的剑，是为了守护\x01",
            "女王陛下和王太女而存在的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10A,
        (
            "#810F#6P……啊…………\x02\x03",

            "这、这么说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "#1120F武器不过是手段――\x02\x03",

            "重要的是，要将\x01",
            "何种思想寄托其上。\x02\x03",

            "我舍弃剑，\x01",
            "不过是因为这种思想\x01",
            "的形式有所改变。\x02\x03",

            "因此，亚妮拉丝……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10A,
        (
            "#810F#6P我也将我自己的思想\x01",
            "寄托于自己的剑就好……\x02\x03",

            "……是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "#1120F哦，被抢先了。\x02\x03",

            "不愧是爷爷的孙女啊。\x01",
            "真是机灵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10A,
        (
            "#810F#6P哎嘿嘿，不过\x01",
            "忘的也快倒是。\x02\x03",

            "但是，卡西乌斯先生的心情……\x01",
            "我感觉终于明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "#1120F是吗……\x02\x03",

            "麻烦你，也替我\x01",
            "转达给爷爷行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10A,
        (
            "#810F#6P是！　我明白了。\x02\x03",

            "爷爷一定\x01",
            "也能明白的。\x02",
        )
    )

    Jump("loc_34BC")

    label("loc_34BC")

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34CA"),
        (SWITCH_DEFAULT, "loc_3617"),
    )


    label("loc_34CA")


    ChrTalk(    #111
        0x10,
        (
            "#1120F唔，是了……\x02\x03",

            "虽然不算是礼物\x01",
            "不过把这个带走吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_3510():
        OP_6D(1650, 0, 21380, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3510)
    OP_8C(0x10, 315, 0)
    OP_8F(0x10, 0xFFFFFF9C, 0x0, 0x54F6, 0x7D0, 0x0)
    WaitChrThread(0x10, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #112
        "\x1F\x90\x05\x07\x00得到了。\x02",
    )

    Jump("loc_3578")

    label("loc_3578")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_8F(0x10, 0x3DE, 0x0, 0x5154, 0x7D0, 0x0)

    ChrTalk(    #113
        0x10,
        (
            "#1120F#2P曾经是我的爱刀。\x02\x03",

            "让选择剑之道的人\x01",
            "拿着它更好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10A,
        (
            "#810F#6P哇啊……！！\x02\x03",

            "非、非常感谢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3617")

    label("loc_3617")


    ChrTalk(    #115
        0x11,
        (
            "#170F你的太刀剑法\x01",
            "让我受益匪浅。\x02\x03",

            "若有机会\x01",
            "再切磋切磋吧。\x02",
        )
    )

    Jump("loc_3661")

    label("loc_3661")

    CloseMessageWindow()
    OP_8C(0x10A, 180, 400)
    Sleep(300)

    ChrTalk(    #116
        0x10A,
        "#810F#5P哎嘿嘿，彼此彼此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        "#1120F#2P今后也要不断进步啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10A, 135, 400)
    Sleep(300)

    ChrTalk(    #118
        0x10A,
        (
            "#810F#6P是！\x02\x03",

            "不肖弟子亚妮拉丝·艾尔菲德，\x01",
            "今后将全身心投入不懈努力！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2DC1 end

    SaveToFile()

Try(main)
