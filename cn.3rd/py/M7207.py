from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7207   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7207.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        '黑骑士',                               # 9
        '阿拉克涅·格赖埃',                     # 10
        '阿拉克涅·艾普洛斯',                   # 11
        '阿拉克涅·塔利亚',                     # 12
        '封印石? ',                             # 13
        '假定角色①',                           # 14
        '假定角色②',                           # 15
        '假定角色③',                           # 16
        '',                                     # 17
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
        'ED6_DT29/CH14320 ._CH',             # 00
        'ED6_DT26/CH20668 ._CH',             # 01
        'ED6_DT27/CH04450 ._CH',             # 02
        'ED6_DT27/CH04455 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH14320P._CP',             # 00
        'ED6_DT26/CH20668P._CP',             # 01
        'ED6_DT27/CH04450P._CP',             # 02
        'ED6_DT27/CH04455P._CP',             # 03
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3830,
        Y                   = -1000,
        Z                   = 34110,
        Range               = 4210,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x8EE4,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -5060,
        Y                   = -1000,
        Z                   = 76030,
        Range               = 4750,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x13560,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_23D",          # 01, 1
        "Function_2_255",          # 02, 2
        "Function_3_26B",          # 03, 3
        "Function_4_1122",         # 04, 4
        "Function_5_11D1",         # 05, 5
        "Function_6_1285",         # 06, 6
        "Function_7_1339",         # 07, 7
        "Function_8_1394",         # 08, 8
        "Function_9_13F4",         # 09, 9
        "Function_10_1454",        # 0A, 10
        "Function_11_14A2",        # 0B, 11
        "Function_12_14F0",        # 0C, 12
        "Function_13_153E",        # 0D, 13
        "Function_14_1587",        # 0E, 14
        "Function_15_2EAC",        # 0F, 15
        "Function_16_2F85",        # 10, 16
        "Function_17_3ACF",        # 11, 17
        "Function_18_3C41",        # 12, 18
        "Function_19_3D1F",        # 13, 19
        "Function_20_3DEC",        # 14, 20
        "Function_21_3F02",        # 15, 21
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_21D")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_21D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_235"),
        (SWITCH_DEFAULT, "loc_23C"),
    )


    label("loc_235")

    Event(0, 18)
    Jump("loc_23C")

    label("loc_23C")

    Return()

    # Function_0_20A end

    def Function_1_23D(): pass

    label("Function_1_23D")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFEA840, 0x230092)
    OP_1B(0x1, 0x0, 0x13)
    Return()

    # Function_1_23D end

    def Function_2_255(): pass

    label("Function_2_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_262")
    Return()

    label("loc_262")

    Call(0, 3)
    Call(0, 14)
    Return()

    # Function_2_255 end

    def Function_3_26B(): pass

    label("Function_3_26B")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp298_00.eff")
    LoadEffect(0x1, "map\\mp298_01.eff")
    LoadEffect(0x2, "map\\mp302_00.eff")
    OP_E0(238, 0x44, 0x2)
    OP_E0(238, 0x45, 0x3)
    OP_E0(239, 0x46, 0x2)
    OP_E0(239, 0x47, 0x3)
    OP_E0(240, 0x48, 0x2)
    OP_E0(240, 0x49, 0x3)
    OP_E0(241, 0x4A, 0x2)
    OP_E0(241, 0x4B, 0x3)
    OP_E0(238, 0x4C, 0x4)
    OP_E0(239, 0x4D, 0x4)
    OP_E0(240, 0x4E, 0x4)
    OP_E0(241, 0x4F, 0x4)
    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)

    ChrTalk(    #0
        0x101,
        "#1004F#12P啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_323():
        OP_6D(0, 200, 93630, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_323)

    def lambda_33B():
        OP_67(0, 8750, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_33B)

    def lambda_353():
        OP_6B(5650, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_353)

    def lambda_363():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_363)

    def lambda_373():
        OP_6E(327, 4500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_373)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)
    SetChrPos(0x10F, -870, -400, 54030, 0)
    SetChrPos(0x101, 1110, -400, 54610, 0)
    SetChrPos(0xF0, -1030, -400, 51900, 0)
    SetChrPos(0xF1, 1030, -400, 52150, 0)
    Fade(500)
    OP_6D(1700, -400, 54800, 0)
    OP_67(0, 4470, -10000, 0)
    OP_6B(4800, 0)
    OP_6C(45000, 0)
    OP_6E(178, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x101,
        (
            "#1006F#5P看起来，\x01",
            "那个就是这个星层的出口吧。\x02\x03",

            "好像没有什么障碍，\x01",
            "我们快点进去吧——\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        "#1443F#6P……请稍等一下。\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #3
        0x101,
        (
            "#1004F#11P哎……\x01",
            "怎么了，莉丝小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10F,
        (
            "#1445F#6P不会有错的。\x01",
            "这是冥府的味道……\x02\x03",

            "而且，越来越强烈了…… \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1020F#11P什么……！？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_599():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_599)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x101, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)

    def lambda_5BB():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5BB)
    SetChrChipByIndex(0xF0, 8)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)

    def lambda_5DD():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_5DD)
    SetChrChipByIndex(0xF1, 10)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#1002F#5P……要是有东西过来的话，\x01",
            "一定得通过魔法阵吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10F,
        "#1441F#6P不对，这次……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x10F,
        "#1449F#6P——上面！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DE")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_745")

    label("loc_6DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_706")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_745")

    label("loc_706")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_745")

    label("loc_72E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_745")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7D9")

    label("loc_772")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7D9")

    label("loc_79A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C2")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7D9")

    label("loc_7C2")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7D9")

    Sleep(1000)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(300, 16777215, -1)

    def lambda_7F3():
        OP_6D(1700, 6000, 54800, 600)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_7F3)
    WaitChrThread(0x10F, 0x3)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(-1820, 11100, 50880, 0)
    OP_67(0, 500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(57000, 0)
    OP_6E(200, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_861():

        label("loc_861")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_861")

    QueueWorkItem2(0x10F, 2, lambda_861)
    OP_1D(0x9A)
    FadeToBright(500, 16777215)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x6)
    OP_43(0x15, 0x0, 0x0, 0x7)
    OP_43(0x16, 0x0, 0x0, 0x8)
    OP_43(0x17, 0x0, 0x0, 0x9)
    Sleep(1000)

    def lambda_8B7():
        OP_6D(-1820, 5100, 50880, 9500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_8B7)

    def lambda_8CF():
        OP_67(0, 6460, -10000, 9500)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_8CF)

    def lambda_8E7():
        OP_6B(4500, 9500)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_8E7)

    def lambda_8F7():
        OP_6E(220, 9500)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_8F7)
    Sleep(5500)
    OP_43(0x10F, 0x0, 0x0, 0xA)
    OP_43(0x101, 0x0, 0x0, 0xB)
    OP_43(0xF0, 0x0, 0x0, 0xC)
    OP_43(0xF1, 0x0, 0x0, 0xD)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(1000)
    Fade(500)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x3)
    OP_44(0xF0, 0x3)
    OP_44(0xF1, 0x3)
    OP_6D(0, -700, 57300, 0)
    OP_67(0, 2290, -10000, 0)
    OP_6B(4720, 0)
    OP_6C(0, 0)
    OP_6E(210, 0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_44(0x10F, 0x2)
    OP_23(0x85)
    Sleep(500)

    ChrTalk(    #9
        0x101,
        "#1020F#6P什、什、什么……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A00")

    ChrTalk(    #10
        0x108,
        "#077F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A30")

    ChrTalk(    #11
        0x10D,
        "#271F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_A30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A60")

    ChrTalk(    #12
        0x10C,
        "#114F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_A60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A90")

    ChrTalk(    #13
        0x10E,
        "#177F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC0")

    ChrTalk(    #14
        0x106,
        "#054F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_AC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1")

    ChrTalk(    #15
        0x103,
        "#1524F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B22")

    ChrTalk(    #16
        0x102,
        "#1506F#6P蜘蛛……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B55")

    ChrTalk(    #17
        0x104,
        "#1550F#6P蜘蛛吗……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_B55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B87")

    ChrTalk(    #18
        0x107,
        "#065F#6P蜘、蜘蛛！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB9")

    ChrTalk(    #19
        0x10B,
        "#216F#6P蜘、蜘蛛！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_BB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")

    ChrTalk(    #20
        0x105,
        "#1166F#6P这是……蜘蛛！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_C20")

    label("loc_BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C20")

    ChrTalk(    #21
        0x10A,
        "#1317F#6P蜘、蜘蛛！？\x02",
    )

    CloseMessageWindow()

    label("loc_C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5C")

    ChrTalk(    #22
        0x110,
        (
            "#1306F#6P嘻嘻……\x01",
            "真是震撼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_C5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CAA")

    ChrTalk(    #23
        0x10A,
        (
            "#1317F#6P真、真是的……\x01",
            "这东西一点儿都不可爱……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_CAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE1")

    ChrTalk(    #24
        0x105,
        "#1162F#6P唉……女神啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_CE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D17")

    ChrTalk(    #25
        0x10B,
        "#216F#6P开、开玩笑吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_D17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(    #26
        0x107,
        "#065F#6P哇哇……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_D49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7A")

    ChrTalk(    #27
        0x104,
        "#1550F#6P……来了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_D7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAD")

    ChrTalk(    #28
        0x102,
        "#1506F#6P哼……来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE0")

    ChrTalk(    #29
        0x103,
        "#1524F#6P哼……来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_DE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E12")

    ChrTalk(    #30
        0x106,
        "#054F#6P嘁……来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_E12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E44")

    ChrTalk(    #31
        0x10E,
        "#177F#6P哼……来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_E44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E76")

    ChrTalk(    #32
        0x10C,
        "#114F#6P哼……来了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA5")

    label("loc_E76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA5")

    ChrTalk(    #33
        0x10D,
        "#271F#6P哼……来了。\x02",
    )

    CloseMessageWindow()

    label("loc_EA5")

    Sleep(500)

    ChrTalk(    #34
        0x10F,
        (
            "#1446F#6P恶梦的编织者。\x01",
            "吞噬误入迷宫的灵魂——\x01",
            "令人绝对恐惧的三姐妹。\x02\x03",

            "#1441F是记载于圣典的\x01",
            "七十七恶魔的眷属——\x01",
            "『暴食』的阿拉克涅！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1002F#6P这种不详的感觉……\x01",
            "看来的确是真正的恶魔啊。\x02\x03",

            "#1005F既然这样，我们就做好觉悟\x01",
            "把它们一口气打飞吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1449F#6P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_22(0x148, 0x0, 0x64)

    def lambda_FE9():

        label("loc_FE9")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_FE9")

    QueueWorkItem2(0x11, 3, lambda_FE9)
    Sleep(30)
    OP_22(0x148, 0x0, 0x64)

    def lambda_1006():

        label("loc_1006")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_1006")

    QueueWorkItem2(0x12, 3, lambda_1006)
    Sleep(30)
    OP_22(0x148, 0x0, 0x64)

    def lambda_1023():

        label("loc_1023")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_1023")

    QueueWorkItem2(0x13, 3, lambda_1023)
    Sleep(500)

    def lambda_103B():
        OP_6D(0, -250, 58250, 300)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_103B)

    def lambda_1053():
        OP_67(0, 2210, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1053)

    def lambda_106B():
        OP_6B(5220, 300)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_106B)

    def lambda_107B():
        OP_6E(139, 300)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_107B)

    def lambda_108B():
        OP_8F(0xFE, 0xFFFFFDB2, 0xFFFFFE70, 0xD00C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_108B)
    Sleep(10)

    def lambda_10AB():
        OP_8F(0xFE, 0x294, 0xFFFFFE70, 0xD048, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10AB)
    Sleep(10)

    def lambda_10CB():
        OP_8F(0xFE, 0xFFFFF9E8, 0xFFFFFE70, 0xCA26, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_10CB)
    Sleep(10)

    def lambda_10EB():
        OP_8F(0xFE, 0x708, 0xFFFFFE70, 0xCC7E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_10EB)
    WaitChrThread(0x10F, 0x3)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF0, 0x3)
    WaitChrThread(0xF1, 0x3)
    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_26B end

    def Function_4_1122(): pass

    label("Function_4_1122")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, 14000, 50840, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1175():

        label("loc_1175")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1175")

    QueueWorkItem2(0xFE, 3, lambda_1175)
    PlayEffect(0x2, 0x3, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFCB44, 0x0, 0x5DC, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_4_1122 end

    def Function_5_11D1(): pass

    label("Function_5_11D1")

    Sleep(150)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2300, 16000, 52450, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1229():

        label("loc_1229")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1229")

    QueueWorkItem2(0xFE, 3, lambda_1229)
    PlayEffect(0x2, 0x4, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x640, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_5_11D1 end

    def Function_6_1285(): pass

    label("Function_6_1285")

    Sleep(400)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2300, 15000, 53500, 180)
    OP_51(0xFE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_12DD():

        label("loc_12DD")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12DD")

    QueueWorkItem2(0xFE, 3, lambda_12DD)
    PlayEffect(0x2, 0x5, 0xFE, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC950, 0x0, 0x640, 0x0)
    OP_22(0x193, 0x0, 0x64)
    Return()

    # Function_6_1285 end

    def Function_7_1339(): pass

    label("Function_7_1339")

    SetChrPos(0x15, 0, 15000, 51000, 0)
    PlayEffect(0x1, 0x0, 0x15, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFCD38, 0x0, 0x5DC, 0x0)
    Return()

    # Function_7_1339 end

    def Function_8_1394(): pass

    label("Function_8_1394")

    Sleep(150)
    SetChrPos(0x16, -2300, 17000, 52650, 0)
    PlayEffect(0x1, 0x1, 0x16, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC180, 0x0, 0x5DC, 0x0)
    Return()

    # Function_8_1394 end

    def Function_9_13F4(): pass

    label("Function_9_13F4")

    Sleep(400)
    SetChrPos(0x17, 2300, 16000, 53700, 0)
    PlayEffect(0x1, 0x2, 0x17, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xFFFFC568, 0x0, 0x5DC, 0x0)
    Return()

    # Function_9_13F4 end

    def Function_10_1454(): pass

    label("Function_10_1454")

    Sleep(140)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1475():
        OP_96(0xFE, 0xFFFFFD58, 0xFFFFFE70, 0xB716, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1475)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_10_1454 end

    def Function_11_14A2(): pass

    label("Function_11_14A2")

    Sleep(80)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_14C3():
        OP_96(0xFE, 0x3C0, 0xFFFFFE70, 0xB810, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C3)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_11_14A2 end

    def Function_12_14F0(): pass

    label("Function_12_14F0")

    Sleep(30)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_1511():
        OP_96(0xFE, 0xFFFFFB14, 0xFFFFFE70, 0xAE88, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1511)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_14F0 end

    def Function_13_153E(): pass

    label("Function_13_153E")

    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_155A():
        OP_96(0xFE, 0x5A0, 0xFFFFFE70, 0xAE7E, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_155A)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_13_153E end

    def Function_14_1587(): pass

    label("Function_14_1587")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10F, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0xF0, 0x1)
    OP_44(0xF1, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    LoadEffect(0x3, "map\\mp263_00.eff")
    LoadEffect(0x4, "map\\mp263_01.eff")
    OP_E0(238, 0x44, 0x5)
    OP_E0(239, 0x45, 0x5)
    OP_E0(240, 0x46, 0x5)
    OP_E0(241, 0x47, 0x5)
    SetChrPos(0x10F, -800, -400, 52050, 0)
    SetChrPos(0x101, 930, -400, 51930, 0)
    SetChrPos(0xF0, -1130, -400, 50190, 0)
    SetChrPos(0xF1, 1060, -400, 50160, 0)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 3)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 3)
    SetChrChipByIndex(0xF0, 6)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 7)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xEE, 0x800)
    SetChrFlags(0xEF, 0x800)
    SetChrFlags(0xF0, 0x800)
    SetChrFlags(0xF1, 0x800)
    OP_43(0xEE, 0x0, 0x0, 0xF)
    OP_43(0xEF, 0x0, 0x0, 0xF)
    OP_43(0xF0, 0x0, 0x0, 0xF)
    OP_43(0xF1, 0x0, 0x0, 0xF)
    OP_6D(770, -400, 50900, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(135000, 0)
    OP_6E(168, 0)

    def lambda_1707():
        OP_6B(4850, 2500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1707)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x2)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        (
            "#1007F#5P呼呼…呼呼……\x02\x03",

            "#1019F最后那个到底算什么嘛……\x01",
            "这不是明显犯规吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        (
            "#1446F#6P那个是『基古玛』……\x01",
            "是三姐妹的母亲吧。\x02\x03",

            "#1806F不过……\x01",
            "总算是将她们给赶走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x15F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x10F, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xEE, 0x0)
    Sleep(50)
    OP_62(0x101, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xEF, 0x0)
    Sleep(50)
    OP_62(0xF0, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xF0, 0x0)
    Sleep(50)
    OP_62(0xF1, 0xFFFFFED4, 1400, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_44(0xF1, 0x0)
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x14, 0x80)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 180, 800, 55300, 0)
    PlayEffect(0x3, 0x6, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    ClearChrFlags(0x0, 0x800)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    ClearChrFlags(0x1, 0x800)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    ClearChrFlags(0x2, 0x800)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x3, 0x800)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x10F,
        "#1444F#11P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1004F#5P那、那个是……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_19CF():
        OP_6D(1200, -400, 53000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_19CF)

    def lambda_19E7():
        OP_67(0, 4890, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_19E7)
    OP_8F(0x10F, 0x8C, 0xFFFFFE70, 0xD2DC, 0x3E8, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x14, 0x82, 0x320, 0xD57A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x6, 0x0)
    OP_82(0x7, 0x0)
    SetChrFlags(0x14, 0x80)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x00得到了\x1F\x60\x03\x07\x00。\x02",
    )

    Jump("loc_1A82")

    label("loc_1A82")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x360, 1)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0x101,
        (
            "#1002F#11P又是封印石……\x02\x03",

            "我还以为\x01",
            "玲的那块封印石是最后的呢……\x02",
        )
    )

    Jump("loc_1B0F")

    label("loc_1B0F")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(    #43
        0x110,
        (
            "#265F唔……\x01",
            "这么说玲也曾经被\x01",
            "关在这种漂亮的宝石里面啊。\x02\x03",

            "#261F嘻嘻……\x01",
            "就像是童话里面的公主一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1016F#5P哈哈，如果是玲的话，\x01",
            "也许正是那种感觉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD4")


    ChrTalk(    #45
        0x10F,
        (
            "#1443F#5P………………………………\x02\x03",

            "#1446F……不知道为什么，\x01",
            "总觉得这个封印石非同一般。\x02\x03",

            "拿在手上的时候，\x01",
            "一点儿也感觉不到温暖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1004F#11P哎……\x02\x03",

            "#1015F难道这是不祥的气息？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1CB6():
        OP_6D(920, -400, 51870, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1CB6)
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0x10F, 0x1)

    ChrTalk(    #47
        0x10F,
        (
            "#1448F#6P不是，总的来说，\x01",
            "应该是有一种冰凉清澈的感觉吧。\x02\x03",

            "一定要说的话，\x01",
            "应该就是像女神那样的神圣感……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 64500, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #48
        0x10,
        "男子的声音",
        (
            "\x07\x05#2P呵呵……\x01",
            "你的感觉还是那样敏锐嘛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E15")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E7C")

    label("loc_1E15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E7C")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E65")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1E7C")

    label("loc_1E65")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1E7C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA9")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F10")

    label("loc_1EA9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F10")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F10")

    label("loc_1EF9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1F10")

    Sleep(1000)

    def lambda_1F1B():
        OP_6D(600, 0, 64000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1F1B)

    def lambda_1F33():
        OP_67(0, 5770, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1F33)

    def lambda_1F4B():
        OP_6B(4380, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1F4B)

    def lambda_1F5B():
        OP_6E(186, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1F5B)
    OP_8C(0x10F, 0, 600)
    WaitChrThread(0x10F, 0x0)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, 0, 100, 64500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    OP_0D()
    Sleep(1000)
    OP_1D(0xB0)
    Fade(1000)
    OP_6D(1100, 0, 65400, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(4380, 0)
    OP_6C(45000, 0)
    OP_6E(186, 0)

    def lambda_2000():
        OP_6B(4100, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2000)

    def lambda_2010():
        OP_6E(185, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2010)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2055():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2055)
    OP_22(0x59, 0x0, 0x64)
    OP_23(0xBA)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_209F")

    ChrTalk(    #49
        0x102,
        "#1502F#1P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_209F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20CE")

    ChrTalk(    #50
        0x110,
        "#264F#1P……哎………\x02",
    )

    CloseMessageWindow()

    label("loc_20CE")


    ChrTalk(    #51
        0x101,
        "#1004F#1P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        (
            "#1441F#1P黑骑士……\x01",
            "你又不知羞耻地出现了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "\x07\x05#1591F#5P呵呵……\x01",
            "那位神父现在还不省人事吗。\x02\x03",

            "可是，除了『制裁异端』之时，\x01",
            "就绝不使用『圣痕』的力量吗…… \x02\x03",

            "呵呵……\x01",
            "真是无聊的坚持啊。\x07\x00\x02",
        )
    )

    Jump("loc_21D8")

    label("loc_21D8")

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1445F#1P………哎………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-30, -200, 61510, 0)
    OP_67(0, 2350, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x10F, -490, -400, 53000, 0)
    SetChrPos(0x101, 500, -400, 52130, 0)
    SetChrPos(0xF0, -1090, -400, 49800, 0)
    SetChrPos(0xF1, 1030, -400, 49700, 0)
    SetChrPos(0x10, 0, 0, 63820, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #55
        0x10,
        (
            "\x07\x05#1591F#5P不过，我本以为……\x01",
            "你们还得多花点时间才能来到这里的……\x02\x03",

            "看来最后的棋子……\x01",
            "稍微有点超出规则之外啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241B")

    ChrTalk(    #56
        0x110,
        (
            "#1306F#6P哎呀……\x01",
            "你说的最后的棋子是指玲吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "\x07\x05#1591F#5P呵呵，因为这颗棋子，\x01",
            "让我的出场时间提前了不少哦。\x02\x03",

            "……不愧是开办\x01",
            "『茶会』的主人呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x110,
        (
            "#263F#6P嘻嘻……\x01",
            "你还真是明白事理呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_241B")


    ChrTalk(    #59
        0x101,
        "#1002F#6P最后的棋子……是指玲吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "\x07\x05#1591F#5P哼哼，因为那颗棋子，\x01",
            "让我的出场时间提前了不少哦。\x02\x03",

            "……不愧是开办\x01",
            "『茶会』的主人呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1026F#6P……竟然连这事也知道………\x02",
    )

    CloseMessageWindow()

    label("loc_24EE")


    ChrTalk(    #62
        0x10,
        (
            "\x07\x05#1591F#5P接下来……\x01",
            "我该完成这回的任务了。\x02\x03",

            "那块石头，\x01",
            "你们就当作是凑齐所有棋子的奖励好了。\x02\x03",

            "被封印的并不是棋子，\x01",
            "而是『规则手册』之类的东西。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#1002F#6P规则手册……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10F,
        (
            "#1446F#6P为了能对等地进行游戏，\x01",
            "而记载有规定知识和准则的小册子……\x02\x03",

            "#1443F也就是说，\x01",
            "你终于有心堂堂正正的和我们对决了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "\x07\x05#1591F#5P呵呵……这就要看你们了。\x02\x03",

            "一言以蔽之……\x02\x03",

            "在下一局棋盘里，\x01",
            "你们所有人都会遭遇到『试炼』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_26EA():

        label("loc_26EA")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_26EA")

    QueueWorkItem2(0x10, 3, lambda_26EA)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 0, 0, 63820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 0, 0, 63820, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27CF")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_27CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_27F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281F")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2836")

    label("loc_281F")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2836")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2863")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_2863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_288B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B3")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28CA")

    label("loc_28B3")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28CA")

    Sleep(1000)

    ChrTalk(    #66
        0x10F,
        "#1449F#6P……又想逃吗……？！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1005F#6P请、请等一下！\x02\x03",

            "你说的『试炼』……\x01",
            "到底是什么东西！？ \x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(250)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #68
        0x10,
        (
            "\x07\x05#1591F#5P哼哼……\x01",
            "是必须跨过的各种『试炼』……\x02\x03",

            "我，也是其中之一。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1020F#6P哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1A")

    ChrTalk(    #70
        0x102,
        "#1503F#6P…………哼………………\x02",
    )

    CloseMessageWindow()

    label("loc_2A1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A4F")

    ChrTalk(    #71
        0x110,
        "#262F#6P………哼……………\x02",
    )

    CloseMessageWindow()

    label("loc_2A4F")


    ChrTalk(    #72
        0x10,
        (
            "\x07\x05#1590F#5P你们到底能不能\x01",
            "通过这些『试炼』呢……\x02\x03",

            "#1591F呵呵，我很期待你们的表现哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0x2, 0xFF, 0, 0, 63820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2AF4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2AF4)
    OP_22(0x59, 0x0, 0x64)
    OP_23(0xBA)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_20(0x7D0)
    Sleep(2000)
    Fade(1000)
    OP_6D(1880, -400, 56000, 0)
    OP_67(0, 4000, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(44000, 0)
    OP_6E(185, 0)

    def lambda_2B60():
        OP_6D(1850, -400, 53600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2B60)
    SetChrPos(0x10F, -240, -400, 53860, 0)
    SetChrPos(0x101, 730, -400, 52100, 0)
    SetChrPos(0xF0, -1130, -400, 50090, 0)
    SetChrPos(0xF1, 1260, -400, 50260, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #73
        0x101,
        (
            "#1020F#11P啊……\x02\x03",

            "#1026F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10F,
        (
            "#1446F#5P……又逃走了。\x02\x03",

            "#1445F真是的……\x01",
            "那种故弄玄虚的态度依旧不变。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1007F#11P嗯……的确是这样……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CC3")

    ChrTalk(    #76
        0x102,
        "#1503F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2CC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(    #77
        0x110,
        "#262F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2CFE")

    OP_62(0x10F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x10F, 180, 400)
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D74")

    ChrTalk(    #78
        0x10F,
        "#1444F#5P大家……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D9C")

    label("loc_2D74")


    ChrTalk(    #79
        0x10F,
        "#1444F#5P艾丝蒂尔小姐……？\x02",
    )

    CloseMessageWindow()

    label("loc_2D9C")


    ChrTalk(    #80
        0x101,
        (
            "#1016F#11P啊，没、没什么。\x02\x03",

            "#1006F先不说这个，\x01",
            "又找到新的封印石了呢……\x02\x03",

            "我们先回据点\x01",
            "把封印给解开吧。 \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        (
            "#1448F#5P嗯，好的。\x02\x03",

            "#1446F规则手册……\x01",
            "到底隐含着什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E76():
        OP_6D(1850, 5000, 53600, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2E76)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10F, 0x0)
    Sleep(2000)
    OP_A2(0x2505)
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1587 end

    def Function_15_2EAC(): pass

    label("Function_15_2EAC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F84")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED6")
    Sleep(100)
    Jump("loc_2F51")

    label("loc_2ED6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EEB")
    Sleep(200)
    Jump("loc_2F51")

    label("loc_2EEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F00")
    Sleep(300)
    Jump("loc_2F51")

    label("loc_2F00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F15")
    Sleep(400)
    Jump("loc_2F51")

    label("loc_2F15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2A")
    Sleep(500)
    Jump("loc_2F51")

    label("loc_2F2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3F")
    Sleep(600)
    Jump("loc_2F51")

    label("loc_2F3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F51")
    Sleep(700)

    label("loc_2F51")

    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_15_2EAC")

    label("loc_2F84")

    Return()

    # Function_15_2EAC end

    def Function_16_2F85(): pass

    label("Function_16_2F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 1)), scpexpr(EXPR_END)), "loc_2F8D")
    Return()

    label("loc_2F8D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-250, -400, 97250, 0)
    OP_67(0, 12670, -10000, 0)
    OP_6B(5670, 0)
    OP_6C(0, 0)
    OP_6E(318, 0)
    SetChrPos(0x109, -870, 0, 80100, 0)
    SetChrPos(0xEF, 360, 0, 79320, 0)
    SetChrPos(0xF0, -1120, 0, 77610, 0)
    SetChrPos(0xF1, 560, 0, 77100, 0)
    OP_0D()

    def lambda_301C():
        OP_6D(640, -400, 90990, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_301C)

    def lambda_3034():
        OP_67(0, 6040, -10000, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3034)

    def lambda_304C():
        OP_6B(3730, 7000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_304C)

    def lambda_305C():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_305C)

    def lambda_306C():
        OP_6E(218, 7000)
        ExitThread()

    QueueWorkItem(0xF1, 2, lambda_306C)
    Sleep(1000)

    def lambda_3081():
        OP_8E(0xFE, 0xFFFFFC2C, 0xFFFFFE70, 0x16058, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3081)

    def lambda_309C():
        OP_8E(0xFE, 0x258, 0xFFFFFE70, 0x16094, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_309C)

    def lambda_30B7():
        OP_8E(0xFE, 0xFFFFF9F2, 0x0, 0x157C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_30B7)

    def lambda_30D2():
        OP_8E(0xFE, 0x28, 0x0, 0x157D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_30D2)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #82
        0x109,
        (
            "#1079F#6P哦……\x01",
            "这就是通往第六星层的传送阵啊。\x02\x03",

            "#1060F好……\x01",
            "我们马上进去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3237")
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #83
        0x10F,
        "#1445F#11P凯文……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #84
        0x109,
        (
            "#1075F#6P哈哈……\x01",
            "别这么一副忧心忡忡的样子嘛。\x02\x03",

            "#1840F时间宝贵……\x01",
            "我们还是先进去再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10F,
        "#1802F#11P……嗯。\x02",
    )

    CloseMessageWindow()

    label("loc_3237")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C8")
    OP_8C(0x101, 270, 400)
    Sleep(300)

    ChrTalk(    #86
        0x101,
        "#1002F#11P凯文先生……你不要紧吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_32C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3317")
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #87
        0x102,
        (
            "#1502F#11P凯文先生……\x01",
            "你没什么事吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_3317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3363")
    OP_8C(0x10B, 270, 400)
    Sleep(300)

    ChrTalk(    #88
        0x10B,
        (
            "#212F#11P那个……\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_3363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33AD")
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #89
        0x107,
        (
            "#065F#11P那个……\x01",
            "真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_33AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33F7")
    OP_8C(0x10A, 270, 400)
    Sleep(300)

    ChrTalk(    #90
        0x10A,
        (
            "#812F#11P哎……\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3448")

    label("loc_33F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3448")
    OP_8C(0x110, 270, 400)
    Sleep(300)

    ChrTalk(    #91
        0x110,
        (
            "#267F#11P对了，这位哥哥。\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3448")

    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #92
        0x109,
        (
            "#1075F#6P哈哈，不要紧。\x01",
            "我已经可以活蹦乱跳啦。\x02\x03",

            "#1840F时间宝贵……\x01",
            "我们还是先进去再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34F3")

    ChrTalk(    #93
        0x101,
        "#1006F#11P嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_34F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3523")

    ChrTalk(    #94
        0x102,
        "#1505F#11P明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_3523")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3556")

    ChrTalk(    #95
        0x10B,
        "#210F#11P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_3556")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3589")

    ChrTalk(    #96
        0x107,
        "#560F#11P知、知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_3589")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BC")

    ChrTalk(    #97
        0x10A,
        "#816F#11P嗯，没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_35EC")

    label("loc_35BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35EC")

    ChrTalk(    #98
        0x110,
        "#268F#11P算了，走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_35EC")

    Jump("loc_3AC4")

    label("loc_35EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3AC4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369A")
    OP_8C(0x105, 270, 400)
    Sleep(300)

    ChrTalk(    #99
        0x105,
        (
            "#1163F#2P凯文先生……\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_369A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E6")
    OP_8C(0x103, 270, 400)
    Sleep(300)

    ChrTalk(    #100
        0x103,
        (
            "#1522F#2P那个……\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_36E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3732")
    OP_8C(0x106, 270, 400)
    Sleep(300)

    ChrTalk(    #101
        0x106,
        (
            "#555F#11P喂喂……\x01",
            "你真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_3732")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377C")
    OP_8C(0x108, 270, 400)
    Sleep(300)

    ChrTalk(    #102
        0x108,
        (
            "#072F#11P唔……\x01",
            "身体状况怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_377C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37CE")
    OP_8C(0x10E, 270, 400)
    Sleep(300)

    ChrTalk(    #103
        0x10E,
        (
            "#178F#11P凯文神父……\x01",
            "觉得身体状态如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_37CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381F")
    OP_8C(0x104, 270, 400)
    Sleep(300)

    ChrTalk(    #104
        0x104,
        (
            "#1542F#11P唔……\x01",
            "你现在的身体状态如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_381F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386C")
    OP_8C(0x10D, 270, 400)
    Sleep(300)

    ChrTalk(    #105
        0x10D,
        "#276F#11P……现在的身体状态怎么样？\x02",
    )

    CloseMessageWindow()
    Jump("loc_38B9")

    label("loc_386C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B9")
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    ChrTalk(    #106
        0x10C,
        (
            "#112F#11P唔……\x01",
            "你现在的身体状态如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B9")

    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #107
        0x109,
        (
            "#1075F#6P哈哈，不要紧。\x01",
            "我已经可以活蹦乱跳啦。\x02\x03",

            "#1840F时间宝贵……\x01",
            "我们还是先进去再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3968")

    ChrTalk(    #108
        0x105,
        "#1382F#11P……我明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_3968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399C")

    ChrTalk(    #109
        0x103,
        "#1534F#11P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_399C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39CD")

    ChrTalk(    #110
        0x106,
        "#051F#11P嘿，好吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_39CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FE")

    ChrTalk(    #111
        0x108,
        "#573F#11P嗯，好吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_39FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2B")

    ChrTalk(    #112
        0x10E,
        "#179F#11P明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_3A2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A65")

    ChrTalk(    #113
        0x104,
        "#1541F#11P呵呵，那就进去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_3A65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A96")

    ChrTalk(    #114
        0x10D,
        "#277F#11P……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AC4")

    label("loc_3A96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC4")

    ChrTalk(    #115
        0x10C,
        "#119F#11P嗯，没错。\x02",
    )

    CloseMessageWindow()

    label("loc_3AC4")

    OP_A2(0x2B01)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_16_2F85 end

    def Function_17_3ACF(): pass

    label("Function_17_3ACF")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-80, -400, 94230, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(4390, 0)
    OP_6C(45000, 0)
    OP_6E(206, 0)
    SetChrPos(0x109, 0, -400, 95030, 0)
    SetChrPos(0xEF, 930, -400, 94030, 0)
    SetChrPos(0xF0, -1220, -400, 94080, 0)
    SetChrPos(0xF1, -170, -400, 93210, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()

    def lambda_3B86():
        OP_6B(3000, 3500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3B86)
    OP_0D()
    Sleep(1500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_3BEE():
        OP_67(0, 8500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3BEE)

    def lambda_3C06():
        OP_6E(420, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3C06)
    Call(0, 21)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_20(0x7D0)
    Sleep(2000)
    NewScene("ED6_DT21/M4113   ._SN", 102, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_17_3ACF end

    def Function_18_3C41(): pass

    label("Function_18_3C41")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x3, 0, -400, 95030, 180)
    SetChrPos(0x2, 930, -400, 94030, 180)
    SetChrPos(0x1, -1220, -400, 94080, 180)
    SetChrPos(0x0, -170, -400, 93210, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x150), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_18_3C41 end

    def Function_19_3D1F(): pass

    label("Function_19_3D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D30")
    Call(0, 17)
    Return()

    label("loc_3D30")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x0, 0, -400, 95030, 0)
    SetChrPos(0x1, 930, -400, 94030, 0)
    SetChrPos(0x2, -1220, -400, 94080, 0)
    SetChrPos(0x3, -170, -400, 93210, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, -400, 94100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M4113   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3D1F end

    def Function_20_3DEC(): pass

    label("Function_20_3DEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E15")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E09():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3E09)

    label("loc_3E15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E3E")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E32():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3E32)

    label("loc_3E3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E67")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3E5B)

    label("loc_3E67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E90")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3E84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3E84)

    label("loc_3E90")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EBC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3EBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3ED3")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3ED3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EEA")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3EEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F01")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3F01")

    Return()

    # Function_20_3DEC end

    def Function_21_3F02(): pass

    label("Function_21_3F02")


    def lambda_3F08():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F08)

    def lambda_3F1A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F1A)

    def lambda_3F2C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F2C)

    def lambda_3F3E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F3E)
    Sleep(1000)
    Return()

    # Function_21_3F02 end

    SaveToFile()

Try(main)
