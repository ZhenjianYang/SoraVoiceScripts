from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3133   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3133   ._SN',
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
        '拉赛尔博士',                           # 9
        '提妲',                                 # 10
        '卡西乌斯',                             # 11
        '福音',                                 # 12
        '重剑用零件',                           # 13
        '提妲的报告书',                         # 14
        '莱恩',                                 # 15
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH00065 ._CH',             # 02
        'ED6_DT27/CH03003 ._CH',             # 03
        'ED6_DT07/CH00053 ._CH',             # 04
        'ED6_DT07/CH00023 ._CH',             # 05
        'ED6_DT07/CH00043 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00063 ._CH',             # 08
        'ED6_DT07/CH02023 ._CH',             # 09
        'ED6_DT27/CH03670 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
        'ED6_DT06/CH20140 ._CH',             # 0C
        'ED6_DT06/CH20141 ._CH',             # 0D
        'ED6_DT07/CH00061 ._CH',             # 0E
        'ED6_DT07/CH01450 ._CH',             # 0F
        'ED6_DT26/CH20278 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH00065P._CP',             # 02
        'ED6_DT27/CH03003P._CP',             # 03
        'ED6_DT07/CH00053P._CP',             # 04
        'ED6_DT07/CH00023P._CP',             # 05
        'ED6_DT07/CH00043P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00063P._CP',             # 08
        'ED6_DT07/CH02023P._CP',             # 09
        'ED6_DT27/CH03670P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
        'ED6_DT06/CH20140P._CP',             # 0C
        'ED6_DT06/CH20141P._CP',             # 0D
        'ED6_DT07/CH00061P._CP',             # 0E
        'ED6_DT07/CH01450P._CP',             # 0F
        'ED6_DT26/CH20278P._CP',             # 10
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 131088,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 32950,
        Z                   = -1000,
        Y                   = 10430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_282",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_6BE",          # 03, 3
        "Function_4_9F8",          # 04, 4
        "Function_5_159F",         # 05, 5
        "Function_6_2F9F",         # 06, 6
        "Function_7_3009",         # 07, 7
        "Function_8_3096",         # 08, 8
        "Function_9_4019",         # 09, 9
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_236")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_236")
    SetChrPos(0xE, 34650, -1000, 2160, 90)

    label("loc_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_281")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    Event(0, 4)

    label("loc_26D")

    Jump("loc_281")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_281")

    Return()

    # Function_0_212 end

    def Function_1_282(): pass

    label("Function_1_282")

    Return()

    # Function_1_282 end

    def Function_2_283(): pass

    label("Function_2_283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_427")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        (
            "呜哇……！？\x01",
            "是、是谁！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#064F啊……？\x01",
            "是……莱恩先生吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #2
        0xFE,
        (
            "啊、啊啊……\x01",
            "什么啊，原来是提妲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "抱歉啊。\x01",
            "随随便便就进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "我现在正在检查\x01",
            "市内的导力器……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "看起来这里的器材\x01",
            "也全部瘫痪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        (
            "#063F嗯……\x01",
            "嗯～好像确实是这样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "所以请暂时\x01",
            "不要打扰我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "用不了多久就可以完工了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#560F啊，是的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x20BF)
    Jump("loc_6BA")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_5B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_490")

    ChrTalk(    #10
        0xFE,
        (
            "看起来这里的器材\x01",
            "全部都无法运转了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "在这样的状态下\x01",
            "要重新开始研究太勉强了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B0")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #12
        0xFE,
        (
            "拉赛尔博士\x01",
            "好像接受军队的求援，前去援助了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "听说由博士挑选的研究员\x01",
            "也一起同行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "也就是说，王国未来的命运\x01",
            "就全要托付给他们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "身为中央工房的一员，\x01",
            "我也感到自豪啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5B0")

    label("loc_558")


    ChrTalk(    #16
        0xFE,
        (
            "王国未来的命运\x01",
            "就全靠博士他们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "身为中央工房的一员，\x01",
            "我也替他们感到自豪呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B0")

    Jump("loc_6BA")

    label("loc_5B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_662")

    ChrTalk(    #18
        0xFE,
        (
            "根据工房长的指示，\x01",
            "要对市内的全部导力器\x01",
            "进行检查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "果然，这里的机械\x01",
            "也全部都无法运转了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "呼～在这种状况下，要怎样\x01",
            "才能重新展开研究呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6BA")

    label("loc_662")


    ChrTalk(    #21
        0xFE,
        (
            "看起来这里的器材\x01",
            "全部都无法运转了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "在这样的状态下\x01",
            "要重新开始研究太勉强了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BA")

    TalkEnd(0xFE)
    Return()

    # Function_2_283 end

    def Function_3_6BE(): pass

    label("Function_3_6BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_6D8")

    EventBegin(0x0)
    SetChrPos(0x101, -1220, 0, -2240, 0)
    SetChrPos(0xF7, -2340, 0, -2240, 0)
    SetChrPos(0x105, -1220, 0, -3260, 0)
    SetChrPos(0x104, -2340, 0, -3260, 0)
    OP_6D(-960, 0, 4280, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_77F():
        OP_67(0, 6150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77F)
    OP_6D(-490, 0, -1760, 2500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #23
        0x101,
        (
            "#1015F#4P嗯……\x01",
            "不知道博士和提妲在不在家。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_808")

    ChrTalk(    #24
        0x106,
        (
            "#051F#6P也没准是去了\x01",
            "中央工房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_831")

    label("loc_808")


    ChrTalk(    #25
        0x103,
        (
            "#027F#6P也有可能是去了\x01",
            "中央工房吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_831")

    SetChrPos(0x8, 3920, 0, -830, 270)

    NpcTalk(    #26
        0x8,
        "女孩子的声音",
        (
            "#1S#5P爷爷～\x01",
            "2楼已经整理好啦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_879():
        OP_6D(1720, 0, -1220, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_879)
    Sleep(100)

    def lambda_896():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_896)
    Sleep(100)

    def lambda_8A9():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8A9)
    Sleep(100)

    def lambda_8BC():
        OP_8C(0xFE, 88, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8BC)
    Sleep(100)

    def lambda_8CF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8CF)
    WaitChrThread(0x101, 0x2)

    NpcTalk(    #27
        0x8,
        "老人的声音",
        "#1S#1P喔，辛苦你啦。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x8,
        "老人的声音",
        (
            "#1S#1P接着帮我把那里的零件\x01",
            "也收拾一下吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x8,
        "女孩子的声音",
        "#1S#5P好的～\x02",
    )

    CloseMessageWindow()

    def lambda_960():
        OP_6D(-490, 0, -1760, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_960)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #30
        0x101,
        (
            "#1017F#6P呵呵，两个人\x01",
            "好像都在研究室。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9D0")

    ChrTalk(    #31
        0x106,
        "#051F#6P嗯，过去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F2")

    label("loc_9D0")


    ChrTalk(    #32
        0x103,
        "#021F#6P嗯，那就过去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_9F2")

    OP_A2(0x1409)
    EventEnd(0x0)
    Return()

    # Function_3_6BE end

    def Function_4_9F8(): pass

    label("Function_4_9F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A12")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_A12")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(35500, -1000, 10320, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(503, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x9, 34650, -1000, 2190, 90)
    FadeToBright(1000, 0)

    def lambda_AA0():
        OP_6D(36140, -1000, 7440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AA0)

    def lambda_AB8():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB8)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_8E(0x9, 0x8700, 0xFFFFFC18, 0x10FE, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_8E(0x9, 0x875A, 0xFFFFFC18, 0x88E, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        "#5P嘿咻、嘿咻……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D62")
    SetChrPos(0x106, 25790, 0, -130, 90)

    ChrTalk(    #34
        0x106,
        "#2P哟！打扰了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BAC():
        OP_6D(34640, -1000, 5940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BAC)

    def lambda_BC4():
        OP_8E(0x106, 0x7EF4, 0xFFFFFC18, 0x6E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_BC4)
    SetChrChipByIndex(0x9, 1)
    TurnDirection(0x9, 0x106, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x106, 400)
    Sleep(800)

    ChrTalk(    #35
        0x9,
        "#560F#2P啊，阿加特哥哥！\x02",
    )

    CloseMessageWindow()

    def lambda_C31():
        OP_8E(0x8, 0x7EF4, 0xFFFFFC18, 0xD20, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C31)

    def lambda_C4C():
        OP_8F(0x9, 0x82DC, 0xFFFFFC18, 0x6E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C4C)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #36
        0x9,
        (
            "#061F#2P嘿嘿，欢迎！\x01",
            "今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #37
        0x8,
        (
            "#100F#5P哎呀。\x01",
            "是不良青年来了吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #38
        0x106,
        (
            "#551F来的好像不是时候啊。\x02\x03",

            "#051F话说回来，这里一点都没变，\x01",
            "还是这么乱七八糟的。\x02\x03",

            "刚才的地震\x01",
            "把东西都震倒了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#067F#2P嘿嘿嘿……\x01",
            "就是那样了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F46")

    label("loc_D62")

    SetChrPos(0x103, 25790, 0, -130, 90)

    ChrTalk(    #40
        0x103,
        "#2P呵呵呵，早啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DB9():
        OP_6D(34640, -1000, 5940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB9)

    def lambda_DD1():
        OP_8E(0x103, 0x7EF4, 0xFFFFFC18, 0x6E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DD1)
    SetChrChipByIndex(0x9, 1)
    TurnDirection(0x9, 0x103, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x103, 400)
    Sleep(800)

    ChrTalk(    #41
        0x9,
        "#064F#2P啊！雪拉姐！\x02",
    )

    CloseMessageWindow()

    def lambda_E3A():
        OP_8E(0x8, 0x7EF4, 0xFFFFFC18, 0xD20, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E3A)

    def lambda_E55():
        OP_8F(0x9, 0x82DC, 0xFFFFFC18, 0x6E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E55)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #42
        0x9,
        (
            "#061F#2P好久不见了啊。\x01",
            "今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #43
        0x8,
        "#103F#5P噢噢，卡西乌斯的弟子吗。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #44
        0x103,
        (
            "#021F好久不见了啊，二位。\x02\x03",

            "#027F屋子里真是一片狼籍啊，\x01",
            "是因为刚才的地震吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "#067F#2P啊，是的。\x01",
            "确实是那样……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F46")

    SetChrPos(0x101, 25230, 0, -750, 90)
    SetChrPos(0x105, 24390, 0, 660, 90)
    SetChrPos(0x104, 23490, 0, -870, 90)

    ChrTalk(    #46
        0x101,
        "#2P好久不见了啊，二位。\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x9,
        "#064F#2P啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_FEA():

        label("loc_FEA")

        TurnDirection(0x8, 0x101, 400)
        OP_48()
        Jump("loc_FEA")

    QueueWorkItem2(0x8, 2, lambda_FEA)

    def lambda_FFB():
        OP_6D(33140, -1000, 3940, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FFB)

    def lambda_1013():
        OP_8E(0xFE, 0x73AA, 0xFFFFFC18, 0x140, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1013)
    Sleep(500)

    def lambda_1033():
        OP_8E(0xFE, 0x756C, 0xFFFFFC18, 0x3D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1033)
    Sleep(200)

    def lambda_1053():
        OP_8E(0xFE, 0x7634, 0xFFFFFC18, 0xFFFFFFD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1053)
    WaitChrThread(0x101, 0x1)

    def lambda_1073():
        OP_8E(0xFE, 0x7C56, 0xFFFFFC18, 0x686, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1073)
    OP_8C(0xF7, 180, 400)

    def lambda_1095():
        OP_8E(0xFE, 0x7E2B, 0xFFFFFC18, 0x190, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1095)
    WaitChrThread(0xF7, 0x1)

    def lambda_10B5():

        label("loc_10B5")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_10B5")

    QueueWorkItem2(0xF7, 2, lambda_10B5)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #48
        0x101,
        (
            "#1016F#6P嘿嘿……\x01",
            "久疏问候了，真是抱歉啊。\x02",
        )
    )

    WaitChrThread(0x104, 0x1)
    TurnDirection(0x104, 0x9, 400)
    OP_44(0xF7, 0x2)
    OP_44(0x8, 0x2)
    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#103F#5P喔喔！！艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "#065F#2P姐、姐姐……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #51
        0x9,
        "#068F#2P#3S艾丝蒂尔姐姐！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_118A():
        OP_6D(32640, -1000, 3440, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_118A)

    def lambda_11A2():
        OP_6B(1770, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11A2)

    def lambda_11B2():

        label("loc_11B2")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_11B2")

    QueueWorkItem2(0x8, 1, lambda_11B2)
    SetChrChipByIndex(0x9, 14)
    OP_92(0x9, 0x101, 0x190, 0x1388, 0x0)

    def lambda_11D6():
        OP_94(0x1, 0x9, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11D6)
    OP_48()
    OP_8C(0x9, 270, 0)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 0)
    OP_8C(0x101, 90, 0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x3)

    ChrTalk(    #52
        0x101,
        "#1004F#6P哇哇～提妲？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#069F#2P艾丝蒂尔姐姐……\x02\x03",

            "太好了……\x01",
            "真的是姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1016F#6P怎、怎么了提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#069F#2P我、我听说……\x02\x03",

            "约修亚哥哥他\x01",
            "不见了……\x02\x03",

            "连艾丝蒂尔姐姐\x01",
            "也去了国外……\x02\x03",

            "#562F我还以为以后再也见不到你们了！\x01",
            "一直……都好难过的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1025F#6P是嘛……\x02\x03",

            "对不起……\x01",
            "对不起…没和你打招呼就去了那么远的地方。\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)

    ChrTalk(    #57
        0x8,
        (
            "#100F#5P嗯，你是去了列曼自治州\x01",
            "的训练场对吧。\x02\x03",

            "是什么时候回国的？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 32350, -1000, 1670, 270)
    OP_0D()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1017F#6P回来还没多久呢。\x02\x03",

            "做完了卢安的工作之后\x01",
            "刚刚才到了蔡斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#101F#5P是这样啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #60
        0x8,
        "#103F#5P啊，你们……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #61
        0x105,
        (
            "#048F好久不见了，\x01",
            "博士，提妲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        "#031F#4P呼～打扰啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 400)

    ChrTalk(    #63
        0x9,
        (
            "#560F#2P科洛丝姐姐……\x01",
            "还有奥利维尔先生……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1006F#6P他们两个都在\x01",
            "协助我进行调查。\x02\x03",

            "在卢安可是发生了不少事情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#104F#5P嗯，是吗……\x02\x03",

            "#100F别一直在这里站着说话，\x01",
            "大家都去客厅坐吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 5)
    Return()

    # Function_4_9F8 end

    def Function_5_159F(): pass

    label("Function_5_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B9")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_15B9")

    OP_6D(-860, 0, 1560, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(40000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    SetChrFlags(0x3, 0x4)
    SetChrPos(0x101, -2270, 200, 480, 90)
    SetChrPos(0xF7, -2270, 200, 1700, 90)
    SetChrPos(0x8, 270, 200, 1700, 270)
    SetChrPos(0x9, 250, 200, 480, 270)
    SetChrPos(0x105, -1100, 200, -800, 0)
    SetChrPos(0x104, -1100, 200, 2650, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_167F")
    SetChrChipByIndex(0xF7, 4)
    Jump("loc_1684")

    label("loc_167F")

    SetChrChipByIndex(0xF7, 5)

    label("loc_1684")

    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x105, 6)
    SetChrChipByIndex(0x104, 7)
    SetChrChipByIndex(0x9, 8)
    SetChrChipByIndex(0x8, 9)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #66
        0x8,
        (
            "#104F政变的幕后黑手\x01",
            "已经开始行动了吗……\x02\x03",

            "#102F而且再次动用到『福音』\x01",
            "的力量……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#065F将空间投影装置生出的影像\x01",
            "传送到远方的座标……\x02\x03",

            "那、那种事…\x01",
            "到底是怎么做到的啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #68
        0x8,
        (
            "#100F#5P空间投影装置并不是\x01",
            "什么难以实现的东西。\x02\x03",

            "只要时间充足的话\x01",
            "我也可以造出来。\x02\x03",

            "#104F只是把生出的影像\x01",
            "传送到远处……\x02\x03",

            "#102F嗯嗯……\x01",
            "这现象就难以解释了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#6P那个戴面具的男子说是在进行\x01",
            "『新型福音』的试验。\x02\x03",

            "#1015F那个新型福音…虽然体积比原来大了一圈，\x01",
            "但并没有引发导力停止现象……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_18F7")

    ChrTalk(    #70
        0x106,
        (
            "#050F对了，在政变时出现的那个\x01",
            "『福音』现在怎样了？\x02\x03",

            "对它的研究有没有什么进展？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1943")

    label("loc_18F7")


    ChrTalk(    #71
        0x103,
        (
            "#020F说起来，在政变时使用过的那个\x01",
            "『福音』怎么样了？\x02\x03",

            "还在继续解析吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1943")

    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #72
        0x8,
        (
            "#104F嗯……那个啊。\x02\x03",

            "随着解析工作的深入，\x01",
            "一个奇妙的现象就显现出来了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x101,
        "#1004F#6P奇妙的现象？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#102F嗯，从结论开始讲吧……\x02\x03",

            "那个『福音』本身\x01",
            "似乎并没有引起『导力停止现象』\x01",
            "的功效。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1020F#6P哎……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#043F可、可是……\x02\x03",

            "可是，那个黑色导力器\x01",
            "确实引起了导力停止现象啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #77
        0x8,
        (
            "#104F#5P喔，这只是表面现象而已。\x02\x03",

            "#102F正如我刚才所说的，\x01",
            "随着我对它内部结晶回路的不断分析，\x01",
            "更加可以确定它没有那种功效。\x02\x03",

            "只是它可以引起\x01",
            "『导力场扭曲』的现象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#042F『导力场扭曲』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#560F那个，所谓的『导力场』\x01",
            "就是由导力能源在周围产生\x01",
            "出的干涉区域。\x02\x03",

            "一般都可以根据特定的规则\x01",
            "将它的作用线路描绘出来，不过……\x02\x03",

            "根据爷爷解析出的结果来看，\x01",
            "『福音』产生的导力场\x01",
            "却违背了这个规则……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#034F#5P唔唔，话题怎么开始\x01",
            "转为专业性的学术讨论了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        "#1007F#6P我也是听得脑袋都大了啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #82
        0x8,
        (
            "#100F啊，简单来说，\x01",
            "就是产生了违背现有法则\x01",
            "的导力场扭曲。\x02\x03",

            "#104F不过，导力场必须\x01",
            "存在于一定的时间和空间内，\x01",
            "不然也无法产生导力能源。\x02\x03",

            "如果没有赋予具体的方向命令，\x01",
            "是肯定不会出现\x01",
            "『导力停止』这种现象的…\x02\x03",

            "#100F总之研究确实是进入瓶颈了啊，\x01",
            "但听了你们在卢安遇到的事件之后\x01",
            "可能会有什么新转机也说不定啊。\x02\x03",

            "#101F总之先谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "还是不能理解…\x01",
            "我是不大懂啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1E98")

    ChrTalk(    #84
        0x106,
        (
            "#051F有关敌人使用的投影装置，\x01",
            "王国军应该已经开始调查了。\x02\x03",

            "有兴趣的话就和他们联络一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF0")

    label("loc_1E98")


    ChrTalk(    #85
        0x103,
        (
            "#020F王国军应该已经开始调查\x01",
            "敌人使用的投影装置了。\x02\x03",

            "有兴趣的话就和他们联络一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF0")


    ChrTalk(    #86
        0x8,
        (
            "#104F嗯……\x01",
            "那就联络看看好了。\x02\x03",

            "#100F对了，你们现在\x01",
            "有什么打算？\x02\x03",

            "打算继续在\x01",
            "蔡斯工作一阵吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F#6P啊，这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x05将协会的要求，以及地震的调查情况\x01",
            "向博士做了汇报。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #89
        0x8,
        (
            "#103F喔……\x01",
            "刚才的地震吗？\x02\x03",

            "#102F利贝尔确实是\x01",
            "很少发生地震的。\x02\x03",

            "而且三天前在沃尔费堡垒\x01",
            "也发生过同样的地震呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#064F三天前……\x02\x03",

            "#063F嗯～但在蔡斯市内\x01",
            "却感觉不到一点摇动，\x02\x03",

            "确实有些奇怪啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1006F#6P现在还无法判明到底是\x01",
            "自然现象还是『结社』搞的鬼……\x02\x03",

            "但既然开始调查了，就好好调查一下吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#104F嗯，地震吗……\x02\x03",

            "也许可以用上\x01",
            "那东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1004F#6P哎？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2178")

    ChrTalk(    #94
        0x106,
        (
            "#552F啊～又有什么可以派上用场\x01",
            "的发明品了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21AA")

    label("loc_2178")


    ChrTalk(    #95
        0x103,
        (
            "#526F哎呀～您又要拿出什么\x01",
            "有用的发明品了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AA")


    ChrTalk(    #96
        0x8,
        (
            "#102F嗯，这是我在数年前\x01",
            "制造的装置……\x02\x03",

            "如果给它装上传送器\x01",
            "然后用『卡佩尔』解析的话……\x02\x03",

            "#101F嗯嗯……也许能行！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1016F#6P好啦～博士。\x01",
            "别再吊大家胃口了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#100F嗯，我已经想出一个可以\x01",
            "协助你们调查的好主意了。\x02\x03",

            "你们现在就去沃尔费堡垒\x01",
            "好了。\x02\x03",

            "在这段时间我会把『好东西』造好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1025F#6P那、那样当然是好，不过……\x02\x03",

            "『好东西』究竟是指什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#101F呵呵。\x01",
            "那个以后再告诉你们。\x02\x03",

            "那么我这就要去\x01",
            "中央工房了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #101
        0x8,
        "#100F#5P提妲，你也来帮忙吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25CB")
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #102
        0x9,
        "#560F啊，嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(    #103
        0x9,
        (
            "#561F对不起了。\x01",
            "姐姐、阿加特哥哥。\x02\x03",

            "才刚见面就…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1016F#6P啊哈哈，没关系的。\x02\x03",

            "#1017F能看见提妲\x01",
            "我就已经很开心啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        "#066F艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x106,
        (
            "#051F而且我们这段时间\x01",
            "都会待在蔡斯，\x02\x03",

            "见面的机会还有的是呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "#067F嘿嘿嘿～是呀。\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 360, 0, 2530, 225)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    SetChrSubChip(0x9, 0)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_24DC():
        OP_96(0xFE, 0x17C, 0x0, 0xFFFFFF38, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24DC)
    OP_8C(0x9, 180, 1000)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x105, 2)
    Sleep(500)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #108
        0x9,
        (
            "#560F#2P那个那个…招待不周，\x01",
            "对不住大家啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x105,
        "#048F#6P呵呵，没有的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x104,
        (
            "#031F#5P嘿～有机会的话\x01",
            "我还会再来拜访的。\x02\x03",

            "下次再见的时候小提妲你一定要\x01",
            "叫人家『大哥哥』才行呀……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2803")

    label("loc_25CB")

    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #111
        0x9,
        "#560F啊，嗯……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(    #112
        0x9,
        (
            "#561F对不起了。\x01",
            "艾丝蒂尔姐姐。\x02\x03",

            "才刚见面就…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1016F#6P啊哈哈，没关系的。\x02\x03",

            "#1017F能看见提妲\x01",
            "我就已经很开心啦。\x02\x03",

            "我们这段时间都会待在蔡斯，\x01",
            "见面的机会还有的是啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#560F艾丝蒂尔姐姐……\x02\x03",

            "#067F嘿嘿～说的也对啊。\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 360, 0, 2530, 225)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    SetChrSubChip(0x9, 0)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_270E():
        OP_96(0xFE, 0x17C, 0x0, 0xFFFFFF38, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_270E)
    OP_8C(0x9, 180, 1000)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x105, 2)
    Sleep(500)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #115
        0x9,
        (
            "#560F#2P那个那个…招待不周，\x01",
            "对不住大家啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x105,
        "#048F#6P呵呵，没有的事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#021F嘿～有机会的话\x01",
            "我还会再来拜访的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x104,
        (
            "#031F#5P下次再见的时候小提妲你一定要\x01",
            "叫人家『大哥哥』才行呀……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2803")

    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #119
        0x101,
        "#1019F#6P好啦～你给我适可而止！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "#067F#2P啊、啊哈哈……\x01",
            "那就一会见啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "#101F我们准备好以后\x01",
            "会去协会和你们联络的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2893():
        OP_6D(-980, 0, -50, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2893)
    OP_43(0x9, 0x1, 0x0, 0x6)
    OP_43(0x8, 0x1, 0x0, 0x7)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    SetChrSubChip(0xF7, 2)
    Sleep(50)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x8, 0x1)
    OP_6D(-860, 0, 1560, 1000)
    SetChrSubChip(0x105, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #122
        0x101,
        (
            "#1016F#6P嗯～……\x01",
            "那２个人真是一点也没有变啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C30")

    ChrTalk(    #123
        0x106,
        (
            "#551F#1P不过，那么小的年龄\x01",
            "就这么专注于机械的世界……\x02\x03",

            "总让人有些不安啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #124
        0x101,
        (
            "#1015F#6P嗯，确实啊，小孩子\x01",
            "还是应该拥有小孩子的生活。\x02\x03",

            "#1006F不过如果是提妲的话\x01",
            "我们就没有必要担心了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#552F#1P哼……真正应该担心\x01",
            "这些的应该是她的父母。\x02\x03",

            "但人在国外就没办法了啊。\x02\x03",

            "下次有机会的话\x01",
            "要让她爷爷注意一下这个问题了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #126
        0x104,
        (
            "#031F#5P哎呀～阿加特兄。\x02\x03",

            "真是标准的大哥哥式\x01",
            "发言啊～～\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 0)
    Sleep(75)
    SetChrSubChip(0x106, 1)
    Sleep(300)

    ChrTalk(    #127
        0x106,
        "#055F#6P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x104,
        (
            "#035F#5P又或者是父亲式的发言……\x02\x03",

            "#037F呵呵呵～要是被别的男人们听见的话，\x01",
            "他们一定会羡慕死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x106,
        (
            "#555F#6P听不懂你在说什么……\x01",
            "难道是想打架吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x104,
        (
            "#031F#5P啊哈哈～没有的事。\x02\x03",

            "只是看那孩子对你这么信赖，\x01",
            "实在是让人有些嫉妒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x105,
        (
            "#041F呵呵，我有点理解\x01",
            "奥利维尔的心情。\x02\x03",

            "#048F我也很想和提妲\x01",
            "成为更好的朋友呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA4")

    label("loc_2C30")


    ChrTalk(    #132
        0x103,
        (
            "#021F#1P哈～小提妲还是\x01",
            "那么可爱啊～\x02\x03",

            "真想紧紧地\x01",
            "抱住她不放。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #133
        0x104,
        (
            "#035F#5P呼……我也是啊。\x02\x03",

            "那散发着牛奶香味，\x01",
            "像小猫一样柔弱幼嫩的身体……\x02\x03",

            "#037F光是想象一下\x01",
            "我就快要受不了了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #134
        0x101,
        (
            "#1019F#6P雪拉姐也就算了……\x01",
            "你那可是犯罪行为啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        (
            "#041F呵呵……\x01",
            "雪拉扎德小姐的心情，\x01",
            "我也能够明白一些。\x02\x03",

            "#048F其实我也很想和提妲\x01",
            "成为更好的朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA4")

    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #136
        0x101,
        (
            "#1016F#6P真是的，连科洛丝也……\x02\x03",

            "#1006F不用担心啦，\x01",
            "除了奥利维尔之外，\x01",
            "大家一定都能很快和提妲成为好朋友的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x104,
        "#036F#5P艾丝蒂尔～你好过分啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2EC4")
    SetChrSubChip(0x106, 0)
    Sleep(75)
    SetChrSubChip(0x106, 2)
    Sleep(300)

    ChrTalk(    #138
        0x106,
        (
            "#551F#1P真是的……\x01",
            "让人头疼的家伙。\x02\x03",

            "#555F好了，现在马上\x01",
            "开始处理协会交付的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EFF")

    label("loc_2EC4")


    ChrTalk(    #139
        0x103,
        (
            "#020F#1P呵呵，接下来……\x02\x03",

            "赶快开始协会交付\x01",
            "的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EFF")

    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #140
        0x101,
        (
            "#1006F#6P嗯，是啊。\x02\x03",

            "在工作时顺便去\x01",
            "沃尔费堡垒调查一下吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    OP_A2(0x140A)
    OP_28(0x85, 0x1, 0x2)
    OP_28(0x85, 0x1, 0x4)
    NewScene("ED6_DT21/T3100   ._SN", 118, 0, 0)
    IdleLoop()
    Return()

    # Function_5_159F end

    def Function_6_2F9F(): pass

    label("Function_6_2F9F")

    ClearChrFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x32, 0x0, 0xFFFFFA2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7AE, 0x0, 0xFFFFF0BA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_2FE3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FE3)
    OP_8E(0xFE, 0xFFFFF79A, 0xFFFFFE0C, 0xFFFFE73C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_2F9F end

    def Function_7_3009(): pass

    label("Function_7_3009")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x49C, 0x0, 0x988, 0x9C4, 0x0)
    OP_8E(0xFE, 0x532, 0x0, 0xFFFFFF42, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF7D6, 0x0, 0xFFFFF0C4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF827, 0xFFFFFE0C, 0xFFFFEE3A, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_306B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_306B)
    OP_8E(0xFE, 0xFFFFF79A, 0xFFFFFE0C, 0xFFFFE73C, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_7_3009 end

    def Function_8_3096(): pass

    label("Function_8_3096")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(30650, -1000, 330, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, 29950, -1000, 8750, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 34450, -350, 10510, 0)
    SetChrPos(0xC, 28600, -850, 7700, 0)
    SetChrPos(0xD, 28750, -900, 8450, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    def lambda_3147():
        OP_6D(29210, 0, 8080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3147)

    def lambda_315F():
        OP_67(0, 6000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_315F)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #141
        0x8,
        (
            "#102F#5P原来如此，这次的『福音』\x01",
            "已经可以干涉到人的精神吗……\x02\x03",

            "而且以雾的粒子作为媒介，\x01",
            "进行广范围的掌握和控制。\x02\x03",

            "#104F嗯……看来只有这样了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 22550, 0, 0, 45)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #142
        0xA,
        "男性的声音",
        "#2P博士，打扰啦。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3277():
        OP_6D(26250, 0, 4030, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3277)

    def lambda_328F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_328F)
    OP_6B(3000, 2500)

    ChrTalk(    #143
        0x8,
        (
            "#103F#6P喔喔！卡西乌斯。\x01",
            "有1个月没见了吧。\x02\x03",

            "是从雷斯顿要塞来的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "#1120F#5P嗯，工作总算是\x01",
            "暂时告一段落了。\x02\x03",

            "就来探望您一趟。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_332E():

        label("loc_332E")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_332E")

    QueueWorkItem2(0x8, 1, lambda_332E)

    def lambda_333F():
        OP_6D(30720, -1000, 7630, 6500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_333F)

    def lambda_3357():
        OP_6B(2750, 6500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3357)
    OP_8E(0xA, 0x779C, 0xFFFFFC18, 0x32A, 0x9C4, 0x0)
    OP_8E(0xA, 0x779C, 0xFFFFFC18, 0x155E, 0x9C4, 0x0)
    TurnDirection(0xA, 0x8, 400)
    Sleep(1000)
    OP_44(0x8, 0x1)

    def lambda_339F():

        label("loc_339F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_339F")

    QueueWorkItem2(0xA, 1, lambda_339F)

    ChrTalk(    #145
        0xA,
        (
            "#1120F那个是……\x01",
            "您孙女的报告吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#101F#5P嗯，今天早上\x01",
            "才从洛连特送来的。\x02\x03",

            "#100F通过这份报告\x01",
            "我更加确信了自己的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        "#1122F是关于『福音』的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#104F#5P嗯，其实只能算是个假想。\x02\x03",

            "#102F不过这也是通过上千次思考试验和\x01",
            "『卡佩尔』演算所得到的结果。\x02\x03",

            "要听听吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        "#1125F当然，洗耳恭听。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        "#101F#5P嗯，那么──\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x80B6, 0xFFFFFC18, 0x2882, 0x7D0, 0x0)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0x74FE, 0xFFFFFC18, 0x222E, 0x7D0, 0x0)
    SetChrPos(0xB, 29260, -400, 8750, 0)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)
    ClearChrFlags(0xB, 0x80)
    OP_22(0x82, 0x0, 0x64)
    OP_44(0xA, 0x1)
    Sleep(1000)

    ChrTalk(    #151
        0x8,
        (
            "#104F#5P有关这个『福音』引起的\x01",
            "『导力停止现象』……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #152
        0x8,
        (
            "#100F#5P按照你的理解，\x01",
            "是怎么一回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "#1122F『福音』可以让周围的\x01",
            "导力器产生连锁的\x01",
            "机能停止反应……\x02\x03",

            "大概就是这样了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "#100F#5P半对半错。\x02\x03",

            "#104F你所说的这种现象\x01",
            "和导力魔法中的\x01",
            "『反魔法领域』类似。\x02\x03",

            "让内部结晶回路瘫痪，\x01",
            "从而使导力器暂时\x01",
            "无法运转。\x02\x03",

            "#102F但是『福音』引起的现象\x01",
            "和那个却有着本质上的区别……\x02\x03",

            "它是直接将导力器中产生出的导力\x01",
            "彻底夺走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#1122F也就是说，不是『导力停止』，\x01",
            "而是『导力吸收』吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#100F嗯，用内燃引擎来做个比喻的话，\x01",
            "就是汽油被抽干了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#1128F嗯，如果是那样的话，\x01",
            "确实是和『反魔法领域』\x01",
            "有着本质上的区别啊……\x02\x03",

            "#1122F啊……等等。\x02\x03",

            "那么被抽走的导力\x01",
            "难道是储存在『福音』中了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#101F#5P嗯，你终于发现关键问题了。\x02\x03",

            "#100F但从结论上来看，\x01",
            "被夺走的导力并没有\x01",
            "被储存在『福音』中。\x02\x03",

            "甚至连１ＥＰ都没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        "#1122F有没有可能是扩散到周围了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#104F#5P绝无可能。\x02\x03",

            "是完全彻底地\x01",
            "消失在某个地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        "#1128F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#100F#5P而且，艾丝蒂尔她们遇到\x01",
            "的那一连串『新型福音』……\x02\x03",

            "引发出了一系列连最新导力技术\x01",
            "也无法解释的『不可能发生的现象』。\x02\x03",

            "#104F那些现象的发生原因\x01",
            "现在虽然还无法探明……\x02\x03",

            "但有一点我可以确定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        "#1124F那是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#102F#5P发生装置实在太小了。\x02\x03",

            "那种超大规模异常现象的\x01",
            "发生装置竟然是那种手掌大的小东西，\x01",
            "从物理角度上来看无论如何也是不可能的。\x02\x03",

            "就算『结社』拥有比我们\x01",
            "先进很多的技术力也是一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#1123F原来如此……\x01",
            "看来总算是抓住关键了啊。\x02\x03",

            "#1120F也就是说，这『福音』\x01",
            "只是『终端』设备而已，对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#101F嗯……正是如此！\x02\x03",

            "#100F『福音』拥有\x01",
            "能发生异常的\x01",
            "导力场扭曲效能。\x02\x03",

            "而这种扭曲会和周围导力器产生共鸣，\x01",
            "将导力器的导力夺走。\x02\x03",

            "而被夺走的导力\x01",
            "都会被吸入扭曲的源头而消失。\x02\x03",

            "#104F啊，正确的说并不是消失。\x02\x03",

            "#102F而是被送到了另一个空间内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "#1125F而在那个空间中应该\x01",
            "就存在着引发这些奇异现象\x01",
            "的关键物体……\x02\x03",

            "#1122F大概就是这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "#102F嗯，应该没错的。\x02\x03",

            "结社大概是通过『福音』\x01",
            "将那神秘物体的力量引发出来\x01",
            "并加以利用了。\x02\x03",

            "#104F唉，『福音』\x01",
            "确实是个了不起的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        (
            "#1128F……………………………………\x02\x03",

            "这样的话……\x01",
            "我对那个『神秘物体』开始感兴趣了。\x02\x03",

            "那是用超先进的技术制造出的\x01",
            "导力器吗，又或是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#104F#5P这就不知道了。\x02\x03",

            "虽然存在着各种的可能性，\x01",
            "但我现在无法再进一步推断。\x02\x03",

            "#100F那么，卡西乌斯──\x01",
            "我仍然要问你这个同１０年前一样的问题。\x02\x03",

            "在如今这种状况，\x01",
            "你希望我接下来怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "#1120F哈哈，在警备飞艇完成时\x01",
            "您也是这么问我的啊。\x02\x03",

            "#1125F唔，这样的话……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(1200)
    OP_90(0xA, 0x258, 0x0, 0x0, 0x3E8, 0x0)
    Sleep(800)
    OP_8C(0xA, 270, 400)
    Sleep(1000)
    OP_90(0xA, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Sleep(1500)
    TurnDirection(0xA, 0x8, 400)
    Sleep(500)

    ChrTalk(    #172
        0xA,
        (
            "#1122F『福音』可以产生出\x01",
            "让导力场扭曲的共鸣现象──\x02\x03",

            "您能否开发出防止这种\x01",
            "共鸣现象的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#101F#5P呵呵，我就知道你会这么说。\x02\x03",

            "#100F现在我手上的发明\x01",
            "马上就要完成了。\x02\x03",

            "把这个结束之后\x01",
            "我就马上开始研究你说的那个东西吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0001   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3096 end

    def Function_9_4019(): pass

    label("Function_9_4019")

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
        (0, "loc_4093"),
        (1, "loc_4099"),
        (SWITCH_DEFAULT, "loc_409F"),
    )


    label("loc_4093")

    OP_A2(0x1200)
    Jump("loc_409F")

    label("loc_4099")

    OP_A2(0x1201)
    Jump("loc_409F")

    label("loc_409F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_40AD")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_40B1")

    label("loc_40AD")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_40B1")

    Return()

    # Function_9_4019 end

    SaveToFile()

Try(main)
