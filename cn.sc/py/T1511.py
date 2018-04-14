from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1511   ._SN',
        MapName             = 'Bose',
        Location            = 'T1511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '雪拉扎德',                             # 9
        '阿加特',                               # 10
        '奥利维尔',                             # 11
        '科洛丝',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '凯文神父',                             # 15
        '索菲娜',                               # 16
        '器皿',                                 # 17
        '器皿',                                 # 18
        '器皿',                                 # 19
        '器皿',                                 # 20
        '器皿',                                 # 21
        '器皿',                                 # 22
        '器皿',                                 # 23
        '器皿',                                 # 24
        '酒杯',                                 # 25
        '酒杯',                                 # 26
        '酒杯',                                 # 27
        '酒杯',                                 # 28
        '酒杯',                                 # 29
        '酒杯',                                 # 30
        '酒杯',                                 # 31
        '酒杯',                                 # 32
        '克鲁茨',                               # 33
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
        'ED6_DT07/CH00023 ._CH',             # 00
        'ED6_DT07/CH00053 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT07/CH00043 ._CH',             # 03
        'ED6_DT07/CH00063 ._CH',             # 04
        'ED6_DT07/CH00073 ._CH',             # 05
        'ED6_DT27/CH03083 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH00020 ._CH',             # 08
        'ED6_DT07/CH00050 ._CH',             # 09
        'ED6_DT07/CH00030 ._CH',             # 0A
        'ED6_DT07/CH00040 ._CH',             # 0B
        'ED6_DT07/CH00060 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT27/CH03080 ._CH',             # 0E
        'ED6_DT27/CH03003 ._CH',             # 0F
        'ED6_DT06/CH20020 ._CH',             # 10
        'ED6_DT06/CH20021 ._CH',             # 11
        'ED6_DT26/CH20403 ._CH',             # 12
        'ED6_DT26/CH20373 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH00023P._CP',             # 00
        'ED6_DT07/CH00053P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT07/CH00043P._CP',             # 03
        'ED6_DT07/CH00063P._CP',             # 04
        'ED6_DT07/CH00073P._CP',             # 05
        'ED6_DT27/CH03083P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH00020P._CP',             # 08
        'ED6_DT07/CH00050P._CP',             # 09
        'ED6_DT07/CH00030P._CP',             # 0A
        'ED6_DT07/CH00040P._CP',             # 0B
        'ED6_DT07/CH00060P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT27/CH03080P._CP',             # 0E
        'ED6_DT27/CH03003P._CP',             # 0F
        'ED6_DT06/CH20020P._CP',             # 10
        'ED6_DT06/CH20021P._CP',             # 11
        'ED6_DT26/CH20403P._CP',             # 12
        'ED6_DT26/CH20373P._CP',             # 13
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 524304,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 262161,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327697,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 262161,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_46A",          # 00, 0
        "Function_1_49C",          # 01, 1
        "Function_2_49D",          # 02, 2
        "Function_3_1C7F",         # 03, 3
        "Function_4_3AC1",         # 04, 4
        "Function_5_3B4B",         # 05, 5
    )


    def Function_0_46A(): pass

    label("Function_0_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_484")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_49B")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_49B")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_49B")

    Return()

    # Function_0_46A end

    def Function_1_49C(): pass

    label("Function_1_49C")

    Return()

    # Function_1_49C end

    def Function_2_49D(): pass

    label("Function_2_49D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B0")
    Call(0, 4)

    label("loc_4B0")

    SetChrFlags(0x101, 0x4)
    SetChrPos(0xE, 15900, 250, 11150, 180)
    SetChrPos(0x101, 17150, 200, 9830, 270)
    SetChrPos(0xB, 14800, 200, 9950, 90)
    SetChrPos(0xC, 17300, 200, 8480, 270)
    SetChrPos(0x8, 14840, 200, 8410, 90)
    SetChrPos(0x9, 17340, 200, 6860, 270)
    SetChrPos(0xA, 14850, 200, 6940, 90)
    SetChrPos(0xD, 15940, 200, 5490, 0)
    SetChrChipByIndex(0x101, 15)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xE, 6)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x9, 2)
    SetChrSubChip(0xC, 2)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xA, 1)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x10, 15970, 800, 10210, 0)
    SetChrPos(0x11, 16440, 800, 9370, 0)
    SetChrPos(0x12, 15700, 800, 9540, 0)
    SetChrPos(0x13, 16440, 800, 8109, 0)
    SetChrPos(0x14, 15700, 800, 8390, 0)
    SetChrPos(0x15, 16440, 800, 6900, 0)
    SetChrPos(0x16, 15700, 800, 7140, 0)
    SetChrPos(0x17, 15900, 800, 6260, 0)
    SetChrPos(0x18, 15430, 800, 10100, 0)
    SetChrPos(0x19, 16190, 800, 9880, 0)
    SetChrPos(0x1A, 15550, 800, 7940, 0)
    SetChrPos(0x1B, 15690, 800, 9110, 0)
    SetChrPos(0x1C, 16260, 800, 8610, 0)
    SetChrPos(0x1D, 16400, 800, 7350, 0)
    SetChrPos(0x1E, 15580, 800, 6670, 0)
    SetChrPos(0x1F, 16300, 800, 6360, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(16750, 200, 8800, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(17040, 0, 9760, 0)
    OP_67(0, 6990, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x1D, 0x4)
    OP_72(0x1E, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0xE,
        (
            "#1065F#5P──原来如此。\x01",
            "看来的确是件相当棘手的事情。\x02\x03",

            "真没想到传说中的古代龙\x01",
            "竟然栖息在利贝尔。\x02\x03",

            "#1067F而且向人们警告了关于『辉之环』的事\x01",
            "又不知道飞去了哪里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1007F#2P嗯，事情发生的太多\x01",
            "感觉脑子都处理不过来了。\x02\x03",

            "#1015F而且不明白龙为什么\x01",
            "对『辉之环』的事闭口不提。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xE,
        (
            "#1060F#5P其实，教会的圣典里\x01",
            "有这样的记载……\x02\x03",

            "#1065F『授予至宝的女神，遣下圣兽\x01",
            "见证人之子的未来。』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "#043F#6P『至宝』和『圣兽』……\x02\x03",

            "看样子跟『辉之环』\x01",
            "和『龙』的关系很相似呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#035F#6P而且『见证』这文字\x01",
            "说不定是最为关键的。\x02\x03",

            "#030F看来龙的职责只能守望着大地，\x01",
            "而不能插手进来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "#053F#2P呼，原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xE,
        (
            "#1060F#5P无论如何，现在看来\x01",
            "『辉之环』很可能是存在的。\x02\x03",

            "结合我的种种调查\x01",
            "可以做出各种推测……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1002F#2P凯文先生正在调查\x01",
            "『四轮之塔』的事情吧。\x02\x03",

            "知道些什么了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xE,
        (
            "#1065F#5P算是吧。\x02\x03",

            "#1063F关于４座塔顶上\x01",
            "有不明用途的古代装置……\x02\x03",

            "你知道吗？它现在正在运作，\x01",
            "并且还发出光亮。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇确认过装置还在运作】\x01",        # 0
            "【◇没确认过装置还在运作】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B98"),
        (1, "loc_BA7"),
        (SWITCH_DEFAULT, "loc_BB6"),
    )


    label("loc_B98")

    OP_29(0x66, 0x1, 0x1000)
    OP_29(0x66, 0x1, 0x2000)
    Jump("loc_BB6")

    label("loc_BA7")

    OP_28(0x66, 0x2, 0x1000)
    OP_28(0x66, 0x2, 0x2000)
    Jump("loc_BB6")

    label("loc_BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x1000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C13")

    ChrTalk(    #9
        0x101,
        (
            "#1015F#2P嗯，我们也\x01",
            "亲眼确认过……\x02\x03",

            "这和『辉之环』\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C82")

    label("loc_C13")


    ChrTalk(    #10
        0x101,
        (
            "#1004F#2P这么说来，在琥珀之塔\x01",
            "剿灭魔兽的时候的确看到在发光呢。\x02\x03",

            "#1015F但是，这和『辉之环』\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C82")


    ChrTalk(    #11
        0xE,
        (
            "#1063F#5P尤莉亚上尉\x01",
            "告诉过我……\x02\x03",

            "城里的『封印区域』最深处，\x01",
            "巨大的机械化怪物出现之前\x01",
            "曾经发生过奇怪的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1004F#2P啊，嗯……\x02\x03",

            "#1015F好像是在使用『福音』之后，\x01",
            "遗迹的照明全部灭了……\x02\x03",

            "然后就听到了警告的声音，\x01",
            "周围的柱子都下降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#022F#6P警告内容是──『第１结界消灭』和\x01",
            "『装置塔启动』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xE,
        (
            "#1060F#5P对对，就是这个。\x02\x03",

            "#1065F然后，结合目击情报\x01",
            "调查后我明白了……\x02\x03",

            "#1063F４座塔的装置开始启动的时间\x01",
            "正是在『封印区域』里\x01",
            "使用『福音』的时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1005F#2P你，你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "#065F#2P这，这么说，警告里说的\x01",
            "『装置塔启动』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        (
            "#072F#4P就是指启动了\x01",
            "『四轮之塔』塔顶的装置。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xE,
        (
            "#1065F#5P嗯嗯，除此以外\x01",
            "没有其他更合理的解释了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#035F#6P唔，把信息整理一下可以得出……\x02\x03",

            "#030F格兰赛尔城的地下遗迹\x01",
            "具备制造『第１结界』\x01",
            "的机能。\x02\x03",

            "但是，由于上校\x01",
            "使用了『福音』，\x01",
            "导致『第１结界』被消灭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#047F#6P然后，取而代之的是\x01",
            "『装置塔』开始启动了……\x02\x03",

            "#042F说不定\x01",
            "是为了产生\x01",
            "被称为『第２结界』的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1002F#2P『第２结界』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#053F#2P哦，有第１\x01",
            "就有第２，这倒也合情合理。\x02\x03",

            "#552F问题是，这个所谓的结界\x01",
            "到底是什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xE,
        (
            "#1065F#5P关于这个……\x02\x03",

            "#1063F我想，结界的存在\x01",
            "是为了隐藏『辉之环』的所在。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x101, 2)
    Sleep(50)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x8, 1)
    Sleep(60)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xC, 2)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xB, 1)
    Sleep(60)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x9, 2)
    Sleep(50)
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x101,
        (
            "#1020F#2P是吗，『辉之环』\x01",
            "不在封印区域里面……\x02\x03",

            "也就是说藏在\x01",
            "利贝尔某处？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xE,
        (
            "#1060F#5P就是这么回事。\x02\x03",

            "#1065F假设结社的目的\x01",
            "是想得到『辉之环』……\x02\x03",

            "#1063F那他们的『实验』\x01",
            "就可以看成是\x01",
            "为了达成这个目的所使用的手段吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1007F#2P嗯、嗯～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#035F#6P『辉之环』、『福音』……\x01",
            "『结社酝酿的实验』……\x02\x03",

            "呵呵，看来一切\x01",
            "都联系上了呢。\x02\x03",

            "#030F而描绘这张蓝图的\x01",
            "就是那个被称为『教授』的人物吗。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)

    ChrTalk(    #28
        0x101,
        (
            "#1007F#2P嗯……是啊。\x02\x03",

            "#1002F在龙的额头上埋入『福音』\x01",
            "袭击柏斯各地的主谋……\x02\x03",

            "以及……\x02\x03",

            "#1003F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xC,
        "#064F#2P……姐姐？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 1)
    Sleep(100)

    ChrTalk(    #30
        0xE,
        "#1064F#5P咋了，怎么了？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(100)

    ChrTalk(    #31
        0x101,
        (
            "#1007F#2P嗯……\x01",
            "#1002F关于这个『教授』。\x02\x03",

            "我认为约修亚的失踪\x01",
            "有可能就是他一手造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "#043F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#022F#6P这么说……\x02\x03",

            "就是５年前，促成约修亚\x01",
            "被老师收留的\x01",
            "幕后黑手吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(100)

    ChrTalk(    #34
        0x101,
        (
            "#1003F#5P嗯……\x02\x03",

            "#1010F还有，操纵理查德上校\x01",
            "和克鲁茨前辈们记忆的人，\x01",
            "我想也是那个教授。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        "#052F#2P什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "#072F#4P喔，记忆操纵的事情确实\x01",
            "尚未解明……\x02\x03",

            "那你为什么会这么想？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1026F#5P嗯，这个……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05艾斯蒂尔向大家说明了约修亚消失的那天傍晚，\x01",
            "自己遇到过的人已经无法记起的事情。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #39
        0x8,
        "#022F#6P还有这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#555F#2P你……\x01",
            "一直隐瞒至今？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1025F#5P倒不是想故意要隐瞒什么……\x02\x03",

            "#1007F……抱歉，可能说得太晚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xB,
        (
            "#042F#6P不过……\x01",
            "看来没错了。\x02\x03",

            "我想那个人很可能\x01",
            "就是各种事件的元凶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#032F#6P唔，看来是个性格\x01",
            "相当冷酷的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "#074F#4P啊啊……\x01",
            "看来必须要多加注意了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        "#063F#2P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1004F#5P对了……\x01",
            "#1025F抱歉，提妲。\x02\x03",

            "难得你来玩\x01",
            "却说些这么扫兴的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "#560F#2P哪里……\x01",
            "别在意，姐姐。\x02\x03",

            "#561F我只是在想，为什么\x01",
            "那个人要做这种事……\x02\x03",

            "让大家留下痛苦的回忆，\x01",
            "又让约修亚哥哥受苦……\x02\x03",

            "我……真是不理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1016F#5P好啦～那种性格扭曲的家伙\x01",
            "没必要去理解啦。\x02\x03",

            "#1006F提妲走自己的路就对啦！\x02\x03",

            "对吧，阿加特？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#055F#2P我说啊～！\x01",
            "为什么要问我啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 2)
    Sleep(100)

    ChrTalk(    #50
        0xB,
        "#041F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(100)

    ChrTalk(    #51
        0x8,
        (
            "#027F#6P呵呵……\x01",
            "这话问得还真是时候。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0)
    Sleep(100)

    ChrTalk(    #52
        0xE,
        "#1067F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    Sleep(100)

    ChrTalk(    #53
        0x101,
        (
            "#1015F#2P嗯？\x01",
            "怎么了，凯文先生？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(75)
    SetChrSubChip(0xB, 1)
    Sleep(100)

    ChrTalk(    #54
        0xE,
        (
            "#1060F#5P不……没什么。\x02\x03",

            "#1061F总而言之情报交换\x01",
            "差不多就这样吧？\x02\x03",

            "来来来，难得这么美味的料理\x01",
            "凉了可就不好吃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1006F#2P嗯，说得也是。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(50)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    SetChrSubChip(0xC, 0)
    Sleep(50)
    SetChrSubChip(0x9, 0)
    Sleep(100)

    ChrTalk(    #56
        0xA,
        (
            "#037F#6P呼，太好了。\x02\x03",

            "尽情享受\x01",
            "美酒佳肴吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x8,
        "#021F#5P哎呀，说啥呢？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0xA,
        (
            "#034F#4P……对不起。\x01",
            "请原谅我的失礼。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    Sleep(500)
    OP_22(0xD, 0x0, 0x64)
    Sleep(6000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05就这样……\x01",
            "艾丝蒂尔等人享受了\x01",
            "片刻的闲暇。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_2_49D end

    def Function_3_1C7F(): pass

    label("Function_3_1C7F")

    EventBegin(0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x20, 0x2)
    SetChrPos(0x20, 49000, -100, 22700, 180)
    SetChrChipByIndex(0x20, 18)
    SetChrSubChip(0x20, 0)
    OP_6F(0x1B, 11)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0x101, 50500, 0, 21820, 270)
    SetChrPos(0xE, 50500, 0, 22640, 270)
    SetChrPos(0x8, 50560, 0, 23630, 225)
    SetChrPos(0xA, 50120, 0, 25120, 180)
    SetChrPos(0x9, 48850, 0, 24330, 180)
    SetChrPos(0xB, 51170, 0, 24660, 225)
    SetChrPos(0xC, 49770, -100, 24140, 180)
    SetChrPos(0xD, 48990, 0, 25290, 180)
    SetChrChipByIndex(0x8, 8)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0xB, 11)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_6D(51790, 0, 24790, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)
    OP_6D(56510, 0, 29350, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(294, 0)

    def lambda_1E0A():
        OP_6D(51790, 0, 24790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E0A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #60
        0xE,
        (
            "#1065F#2P──虽然做了急救治疗，\x01",
            "但伤势可不轻啊。\x02\x03",

            "#1063F暂时还是不要动比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1026F#2P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "#552F#5P没想到克鲁茨这家伙\x01",
            "竟然会被打成这样……\x02\x03",

            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1002F#2P我记得克鲁茨前辈说过，\x01",
            "他们的队伍好像已经找到\x01",
            "结社的据点了。\x02\x03",

            "这么说，亚妮拉丝\x01",
            "和卡露娜前辈应该也在一起……\x02\x03",

            "#1020F啊……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xD,
        "#572F#5P……糟了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#022F#5P已经用房间里的通信器\x01",
            "和卢格兰爷爷联络过了。\x02\x03",

            "应该也会很快\x01",
            "和各地的协会和王国军取得联络的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1020F#2P但，但是……！\x02\x03",

            "搞不好\x01",
            "亚妮拉丝他们会……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#020F#5P嗯嗯……我明白的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#053F#5P我们最好也\x01",
            "想办法行动吧。\x02\x03",

            "#555F问题是载着克鲁茨的小船\x01",
            "是从哪里漂来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#032F#5P唔，记得瓦雷利亚湖里\x01",
            "并没有岛屿或礁石吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xB,
        "#043F#5P是的，因为水很深很深……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#035F#5P那么就必定是从\x01",
            "某处湖岸漂来的。\x02\x03",

            "但是要确定这个地点\x01",
            "不是件容易的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1007F#2P嗯……\x01",
            "这湖又那么大。\x02\x03",

            "#1015F要是能拜托军用警备艇\x01",
            "参加搜索就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x20,
        "#847F呜……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x101,
        "#1004F#2P克鲁茨前辈！？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x20, 1)
    Sleep(300)
    SetChrSubChip(0x20, 2)
    Sleep(1500)
    SetChrSubChip(0x20, 3)
    Sleep(1000)

    ChrTalk(    #75
        0x20,
        (
            "#844F这……这里是……\x02\x03",

            "艾丝蒂尔……\x01",
            "……还有阿加特你们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "#556F#5P这里是柏斯地方南部，\x01",
            "湖畔的『川蝉亭』。\x02\x03",

            "你乘上小船\x01",
            "被漂到这里来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x20,
        (
            "#844F是……是吗……\x02\x03",

            "#843F我记得和其他的队员\x01",
            "潜入了『结社』据点……\x02\x03",

            "…………然后……………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x20, 0xFFFFFE70, 1800, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #78
        0x101,
        "#1020F#2P克，克鲁茨前辈……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#023F#5P难不成……\x02",
    )

    CloseMessageWindow()
    OP_63(0x20)
    Sleep(500)

    ChrTalk(    #80
        0x20,
        (
            "#844F唔……怎么搞的……\x02\x03",

            "竟然连续两次……\x01",
            "被夺去记忆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1002F#2P果，果然……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "#032F#5P看来被那什么『教授』\x01",
            "封印了记忆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 2)
    Sleep(500)

    ChrTalk(    #83
        0x20,
        (
            "#842F拜，拜托……金先生！\x02\x03",

            "就像以前那样，\x01",
            "把『气』打到我身上……！\x02\x03",

            "不然这样下去的话，库拉茨他们会……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xD,
        (
            "#572F#5P……那仅仅是\x01",
            "一种对症疗法。\x02\x03",

            "应该是没法恢复\x01",
            "因暗示而被封印的记忆。\x02\x03",

            "#074F而且，对现在有伤在身的你来说\x01",
            "负担太重了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x20,
        "#844F但，但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        (
            "#1060F#2P……这样的话\x01",
            "我来想想办法吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0xFFFFFED4, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_26A7():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26A7)

    def lambda_26B5():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26B5)
    Sleep(100)

    def lambda_26C8():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26C8)

    def lambda_26D6():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26D6)
    Sleep(400)

    ChrTalk(    #87
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 3)
    Sleep(500)

    ChrTalk(    #88
        0x20,
        "#842F……你是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xE,
        (
            "#1060F#2P我是七耀教会『星杯骑士』，\x01",
            "凯文·格拉汉姆。\x02\x03",

            "亚妮拉丝他们\x01",
            "没告诉过你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x20,
        "#841F噢……是你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1015F#2P但，但是，凯文先生。\x01",
            "你能解除暗示吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xE,
        (
            "#1071F#2P嗯～如果已经深入到深层心理\x01",
            "那就完全没有办法了……\x02\x03",

            "不过若是解放暂时封印的记忆，\x01",
            "应该能有办法。\x02\x03",

            "#1062F而且，似乎被暗示\x01",
            "的时间也不是很久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1025F#2P是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "#032F#5P唔，难道是所谓的教会流传的\x01",
            "秘藏法术吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        (
            "#1061F#2P嗯，算是吧。\x02\x03",

            "#1060F不过，精神上可能\x01",
            "多少会受点伤害……\x02\x03",

            "这样也没关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x20,
        (
            "#842F没问题……\x01",
            "务必请您一试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        "#1065F#2P明白。\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    Fade(500)
    SetChrChipByIndex(0xE, 19)
    SetChrSubChip(0xE, 0)
    OP_21()
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xE, 1)
    Sleep(1000)

    ChrTalk(    #98
        0xE,
        (
            "#1063F#2P──空之女神名下\x01",
            "谨此圣化七耀。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x21)
    Sleep(500)

    def lambda_29A2():
        OP_6B(2600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29A2)

    def lambda_29B2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29B2)

    def lambda_29C0():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29C0)
    Sleep(50)

    def lambda_29D3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_29D3)

    def lambda_29E1():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_29E1)
    Sleep(500)
    LoadEffect(0x1, "map\\\\mp082_00.eff")
    PlayEffect(0x1, 0x0, 0xE, -450, 800, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #99
        0x101,
        "#1004F#2P（哇哇……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xC,
        "#560F#5P（哇，好漂亮……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xE,
        (
            "#1065F#2P识之银耀，时之黒耀──\x02\x03",

            "以其相克之力\x01",
            "在此除却\x01",
            "嵌入此人之楔……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    LoadEffect(0x0, "scraft\\\\sc008_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 50020, 900, 22900, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0xC9)
    OP_82(0x0, 0x2)
    Sleep(2000)
    SetChrSubChip(0x20, 3)
    Sleep(100)
    SetChrSubChip(0x20, 4)
    Sleep(100)
    SetChrSubChip(0x20, 5)

    ChrTalk(    #102
        0x20,
        "#847F……呜……！\x02",
    )

    OP_9E(0x20, 0x14, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1020F#2P没事吧，克鲁茨前辈！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x20,
        (
            "#847F啊啊……没事……\x02\x03",

            "……………………………\x01",
            "……好像迷雾散去一般\x01",
            "想起了……很多事情……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xE, 14)
    SetChrSubChip(0xE, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #105
        0xE,
        (
            "#1063F#2P虽然迷雾已经散去，\x01",
            "但还请慢慢让自己的心平静下来。\x02\x03",

            "千万不可急于窥视\x01",
            "那彼岸的黑暗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x20,
        (
            "#843F啊啊……我明白。\x02\x03",

            "呵呵，我明白所谓精神上的伤害\x01",
            "是指什么了……\x02\x03",

            "那就是……正反面的自我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xE,
        "#1064F#2P哎呀，你明白了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x20,
        (
            "#843F别看我现在这样，\x01",
            "也是修练过冥想的人……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 5)
    Sleep(300)
    SetChrSubChip(0x20, 4)
    Sleep(300)
    SetChrSubChip(0x20, 3)
    Sleep(1000)

    ChrTalk(    #109
        0x20,
        (
            "#845F……已经没事了。\x01",
            "我什么都想起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1025F#2P真，真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xD,
        "#070F#5P唔……真是高超的法术。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "#051F#5P呼，看来你不仅仅是个\x01",
            "不良神父那么简单嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#021F#5P呵呵……\x01",
            "干得好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xE,
        (
            "#1061F#2P啊哈哈，没什么大不了的。\x02\x03",

            "#1063F那么克鲁茨先生。\x01",
            "你能想起来些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x20,
        (
            "#843F啊啊……\x02\x03",

            "#842F『结社』的据点在\x01",
            "瓦雷利亚湖西北的湖岸……\x02\x03",

            "那里有他们秘密建造\x01",
            "的研究设施……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1020F#2P研，研究设施！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        "#022F#5P这东西究竟是什么时候……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xB,
        (
            "#043F#5P说到瓦雷利亚湖西北岸，\x01",
            "确实是远离都市的地方……\x02\x03",

            "不过应该也有\x01",
            "警备艇在搜索啊……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x20,
        (
            "#843F他们好像用特殊的方法\x01",
            "隐藏了设施所在……\x02\x03",

            "似乎是在上空播放伪装影像\x01",
            "来防御空中搜索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1005F#2P你，你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "#034F#5P这真是……\x01",
            "让人无法理解的技术啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "#065F#5P原，原理上来说是可能的，\x01",
            "但还是有点难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x20,
        (
            "#844F而且在地面上……\x02\x03",

            "一旦接近，似乎周围\x01",
            "就会产生浓雾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        "#042F#5P雾……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        "#552F#5P令人联想到洛连特的事件啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x20,
        (
            "#843F我们的队伍穿过浓雾\x01",
            "潜入了研究设施……\x02\x03",

            "但遭到名为『执行者』的\x01",
            "厉害人物的埋伏……\x02\x03",

            "#844F我们完全被抓住了破绽，\x01",
            "全线溃退……\x02\x03",

            "刚逃到船上\x01",
            "我就失去了意识……\x02\x03",

            "#847F呜，没想到居然抛下了同伴\x01",
            "独自逃生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1006F#2P克鲁茨前辈……放心吧！\x02\x03",

            "我们一定会把亚妮拉丝他们\x01",
            "救出来的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x20,
        "#842F艾，艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "#051F#5P噢，既然已经掌握了这么多情报，\x01",
            "我们总能做点什么吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#020F#5P是啊。\x01",
            "而且军队也应该会派出支援。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        "#070F#5P之后就交给我们吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x20,
        (
            "#845F谢，谢谢……\x02\x03",

            "#847F抱歉……拜托你们了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x20, 4)
    Sleep(300)
    SetChrSubChip(0x20, 5)
    Sleep(200)
    SetChrSubChip(0x20, 6)
    Sleep(200)
    SetChrSubChip(0x20, 7)
    Sleep(1000)

    ChrTalk(    #133
        0x101,
        "#1020F#2P怎，怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xE,
        (
            "#1065F#2P没事，只是昏过去了。\x02\x03",

            "#1063F但是……\x01",
            "看来已经没有时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1005F#2P嗯……！\x02\x03",

            "在王国军行动之前\x01",
            "我们也必须采取行动才行！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0xB, 0x101, 400)
    Sleep(200)

    ChrTalk(    #136
        0x8,
        (
            "#022F#5P艾丝蒂尔，我想不说\x01",
            "你应该也知道……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)

    ChrTalk(    #137
        0x101,
        (
            "#1003F#4P嗯……我明白。\x02\x03",

            "和之前的任务相比\x01",
            "这次的危险程度完全不同对吧。\x02\x03",

            "#1002F不过，总有一天会\x01",
            "以这种形式和『结社』对决，\x01",
            "这我早有心理准备……\x02\x03",

            "只不过是提前了点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#023F#5P艾丝蒂尔……\x02\x03",

            "#524F呵呵，真是短暂的休假呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        (
            "#051F#5P喔，足够了吧。\x02\x03",

            "该下定决心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        (
            "#074F#5P但是，大家一起潜入\x01",
            "反而会更显眼。\x02\x03",

            "#070F我们还是精简一下人数吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1006F#4P嗯……也是。\x02\x03",

            "#1015F对了，各位。\x02\x03",

            "就跟那时一样……\x01",
            "也让我来选可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#020F#5P那时是说……\x01",
            "探索封印区域的时候吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xD,
        "#070F#5P啊啊，没问题吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x9,
        (
            "#051F#5P嗯，就算没选我\x01",
            "我也不会恨你啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xA,
        (
            "#031F#5P呼，我确信\x01",
            "一定会选到我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "#048F#5P如果需要人负责回复，\x01",
            "请务必带上我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        (
            "#062F#5P我，我对机械的事\x01",
            "也一定能帮上忙的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1025F#4P大家……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)

    ChrTalk(    #149
        0xE,
        (
            "#1068F#5P啊～抱歉打个岔。\x02\x03",

            "#1060F先把我选进队伍\x01",
            "怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1004F#4P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xE,
        (
            "#1063F#5P看来亚妮拉丝他们\x01",
            "已经落入『结社』手中了。\x02\x03",

            "解救的时候，要是他们也被\x01",
            "施了刚才那种法术该怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1020F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        "#070F#5P原来如此，有道理。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x9,
        (
            "#051F#5P没办法……\x01",
            "你就确定入选了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        "#1061F#5P嘿嘿，多谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1016F#4P真是的，要说谢谢的\x01",
            "是我才对啦。\x02\x03",

            "#1006F那么……\x01",
            "来选剩下的队员吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)

    label("loc_3862")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A98")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #157
        (
            "\x06\x18\x07\x05※进行队伍的重新编组。\x01",
            "　更换队员，进行必要的装备变更，\x01",
            "　确定后，请选择【继续】。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【编成队伍】\x01",      # 0
            "【变更装备】\x01",      # 1
            "【继续】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3996")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #158
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_3A95")

    label("loc_3996")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_39CF")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_39FA")

    label("loc_39CF")


    AnonymousTalk(    #159
        "\x07\x05※进行队伍的编组之后再选择。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_39FA")

    Jump("loc_3A95")

    label("loc_39FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A6A")
    SetChrName("")

    AnonymousTalk(    #160
        "\x06\x18\x07\x05※可以继续剧情了吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A67")
    Jump("loc_3A98")

    label("loc_3A67")

    Jump("loc_3A95")

    label("loc_3A6A")


    AnonymousTalk(    #161
        "\x07\x05※进行队伍的编组之后再选择。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_3A98")

    OP_69(0x0, 0x0)
    SetMapFlags(0x1)
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_31(0xFF, 0xFE, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0901   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_3A95")

    Jump("loc_3862")

    # Function_3_1C7F end

    def Function_4_3AC1(): pass

    label("Function_4_3AC1")

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
        (0, "loc_3B3E"),
        (1, "loc_3B44"),
        (SWITCH_DEFAULT, "loc_3B4A"),
    )


    label("loc_3B3E")

    OP_A2(0x1200)
    Jump("loc_3B4A")

    label("loc_3B44")

    OP_A2(0x1201)
    Jump("loc_3B4A")

    label("loc_3B4A")

    Return()

    # Function_4_3AC1 end

    def Function_5_3B4B(): pass

    label("Function_5_3B4B")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_5_3B4B end

    SaveToFile()

Try(main)
