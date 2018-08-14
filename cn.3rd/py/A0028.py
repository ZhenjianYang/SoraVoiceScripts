from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'A0028   ._SN',
        MapName             = 'Minigame',
        Location            = 'MG05_00.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        '基尔巴特',                             # 9
        '',                                     # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 0,
        Unknown_18              = 0,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 10000,
        Unknown_28              = 2800,
        Unknown_2C              = 1400,
        Unknown_30              = 0,
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

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 0,
        Unknown_18              = 0,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 10000,
        Unknown_28              = 2800,
        Unknown_2C              = 1400,
        Unknown_30              = 0,
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10E",          # 00, 0
        "Function_1_132",          # 01, 1
        "Function_2_133",          # 02, 2
        "Function_3_182",          # 03, 3
        "Function_4_576",          # 04, 4
        "Function_5_5BB",          # 05, 5
        "Function_6_602",          # 06, 6
    )


    def Function_0_10E(): pass

    label("Function_0_10E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121")
    Event(0, 4)
    Jump("loc_131")

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131")
    Event(0, 5)

    label("loc_131")

    Return()

    # Function_0_10E end

    def Function_1_132(): pass

    label("Function_1_132")

    Return()

    # Function_1_132 end

    def Function_2_133(): pass

    label("Function_2_133")

    OP_E2(0x3, 0x2)

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【游戏】(DEBUG)\x01",      # 0
            "【停顿】(DEBUG)\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_17B"),
        (SWITCH_DEFAULT, "loc_181"),
    )


    label("loc_17B")

    OP_A2(0x0)
    Jump("loc_181")

    label("loc_181")

    Return()

    # Function_2_133 end

    def Function_3_182(): pass

    label("Function_3_182")

    FadeToDark(0, 0, -1)
    OP_E2(0x3, 0x2)
    OP_1D(0xC2)
    OP_AD(0x240144, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_555")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　设定　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_218"),
        (1, "loc_286"),
        (2, "loc_54A"),
        (3, "loc_54F"),
        (SWITCH_DEFAULT, "loc_552"),
    )


    label("loc_218")


    Menu(
        1,
        -1,
        330,
        1,
        (
            "【ＮＯＲＭＡＬ】\x01",      # 0
            "【  ＥＡＳＹ  】\x01",      # 1
        )
    )

    MenuEnd(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_26D"),
        (1, "loc_273"),
        (SWITCH_DEFAULT, "loc_279"),
    )


    label("loc_26D")

    OP_E2(0xB, 0x0)
    Jump("loc_283")

    label("loc_273")

    OP_E2(0xB, 0x1)
    Jump("loc_283")

    label("loc_279")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_283")

    Jump("loc_552")

    label("loc_286")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　使用乔丝特操控机关炮\x01",
            "　将来敌和导弹击落。\x01",
            "　操作方法如下。\x01",
            "　\x01",
            "　方向键／鼠标移动　：瞄准目标。\x01",
            "　决定键　　　　　　：开炮（按住为连续开炮）\x01",
            "　取消键　　　　　　：缩放\x01",
            "　[B](星杯手册)键 　：视点操作的设定\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_3E9")

    label("loc_3E9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　虽然机关炮的弹药数量是没有限制的，\x01",
            "　但是过量的连续射击会导致射击效率的降低。\x01",
            "　不过只要停止发射便可以自动恢复。\x01",
            "　\x01",
            "　请注意，如果山猫号的ＨＰ变为０，\x01",
            "　游戏将以失败告终。\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_53B")

    label("loc_53B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_552")

    label("loc_54A")

    OP_E2(0x7)
    Jump("loc_552")

    label("loc_54F")

    Jump("loc_552")

    label("loc_552")

    Jump("loc_1B3")

    label("loc_555")

    FadeToBright(0, 0)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_182 end

    def Function_4_576(): pass

    label("Function_4_576")

    Call(0, 3)
    OP_E2(0x9, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0")
    Sleep(1000)
    OP_E2(0x8)
    Sleep(1000)
    OP_E2(0x4, 0x0)
    Sleep(1000)
    OP_E2(0x0, 0x1)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0xA)"), scpexpr(EXPR_END)), "loc_5B0")
    OP_A2(0x2509)
    OP_E2(0x5, 2163187, 0x0)
    ExitThread()

    label("loc_5B0")

    OP_A2(0x2506)
    OP_E2(0x5, 2162855, 0x0)
    Return()

    # Function_4_576 end

    def Function_5_5BB(): pass

    label("Function_5_5BB")

    OP_E2(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7")
    OP_E2(0x4, 0x0)
    OP_E2(0x0, 0x2)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0xA)"), scpexpr(EXPR_END)), "loc_5E0")
    OP_A2(0x2509)
    OP_E2(0x5, 2163187, 0x64)
    ExitThread()

    label("loc_5E0")

    OP_E2(0x3, 0x0)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    Sleep(4000)

    label("loc_5F7")

    OP_A2(0x2506)
    OP_E2(0x5, 2163187, 0x0)
    Return()

    # Function_5_5BB end

    def Function_6_602(): pass

    label("Function_6_602")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_627")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_769")

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_769")

    label("loc_640")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_769")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_769")

    label("loc_672")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_769")

    label("loc_68B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_769")

    label("loc_6A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_769")

    label("loc_6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_769")

    label("loc_6D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_769")

    label("loc_6EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_769")

    label("loc_708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_721")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_769")

    label("loc_721")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_769")

    label("loc_73A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_753")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_769")

    label("loc_753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_769")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_769")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_77E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_769")

    label("loc_77E")

    Return()

    # Function_6_602 end

    SaveToFile()

Try(main)
