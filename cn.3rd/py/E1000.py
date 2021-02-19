from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E1000   ._SN',
        MapName             = 'Event',
        Location            = 'E1000.x',
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
        '肯帕雷拉',                             # 9
        '',                                     # 10
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
        'ED6_DT27/CH03600 ._CH',             # 00
        'ED6_DT26/CH20305 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03600P._CP',             # 00
        'ED6_DT26/CH20305P._CP',             # 01
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


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_F2",           # 01, 1
        "Function_2_F3",           # 02, 2
        "Function_3_1B3",          # 03, 3
        "Function_4_954",          # 04, 4
        "Function_5_E9C",          # 05, 5
        "Function_6_13D4",         # 06, 6
        "Function_7_18A4",         # 07, 7
        "Function_8_1B48",         # 08, 8
        "Function_9_1BEF",         # 09, 9
        "Function_10_3706",        # 0A, 10
        "Function_11_60E2",        # 0B, 11
        "Function_12_60E3",        # 0C, 12
        "Function_13_613C",        # 0D, 13
        "Function_14_64C4",        # 0E, 14
        "Function_15_64EE",        # 0F, 15
        "Function_16_84B7",        # 10, 16
        "Function_17_9F9F",        # 11, 17
        "Function_18_B431",        # 12, 18
        "Function_19_CCAB",        # 13, 19
        "Function_20_E125",        # 14, 20
        "Function_21_E191",        # 15, 21
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Event(0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_F1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_F1")

    Return()

    # Function_0_DA end

    def Function_1_F2(): pass

    label("Function_1_F2")

    Return()

    # Function_1_F2 end

    def Function_2_F3(): pass

    label("Function_2_F3")

    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110")
    Call(0, 3)
    Jump("loc_1A8")

    label("loc_110")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123")
    Call(0, 8)
    Jump("loc_1A8")

    label("loc_123")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136")
    Call(0, 11)
    Jump("loc_1A8")

    label("loc_136")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149")
    Call(0, 13)
    Jump("loc_1A8")

    label("loc_149")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C")
    Call(0, 15)
    Jump("loc_1A8")

    label("loc_15C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F")
    Call(0, 16)
    Jump("loc_1A8")

    label("loc_16F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182")
    Call(0, 17)
    Jump("loc_1A8")

    label("loc_182")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_195")
    Call(0, 18)
    Jump("loc_1A8")

    label("loc_195")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    Call(0, 19)
    Jump("loc_1A8")

    label("loc_1A8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_F3 end

    def Function_3_1B3(): pass

    label("Function_3_1B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x1004, 0x32C8, 0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(0, 80000, 1000, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(665, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 80000, 0, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 4)), scpexpr(EXPR_END)), "loc_2AF")
    StopSound(0x3264, 0x61A8, 0x0)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #0
        0x10,
        (
            "#5P#850F哟，是你啊。\x01",
            "又来了吗。\x02\x03",

            "#5P是来玩问答游戏的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_54B")

    label("loc_2AF")

    OP_A2(0x2F14)
    SetChrPos(0x10, 0, 80000, 0, 0)
    FadeToBright(4000, 0)
    OP_0D()
    Sleep(200)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("妖气的声音")

    AnonymousTalk(    #1
        "\x07\x00哟，最近过得还不错吧？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    StopSound(0x3264, 0x61A8, 0x9C4)
    OP_0D()
    Sleep(2500)
    OP_8C(0x10, 180, 400)
    Sleep(800)

    ChrTalk(    #2
        0x10,
        (
            "#5P#850F呵呵，是我、是我啊。\x01",
            "可别说你已经把我忘了哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    Fade(100)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    OP_99(0x10, 0x0, 0x3, 0x3E8)
    Sleep(500)

    ChrTalk(    #3
        0x10,
        (
            "#5P#853F竟能来到这种地方，欢迎至极。\x02\x03",

            "#854F呵呵，\x01",
            "今天大家就来欢庆一场吧⊙\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    Fade(700)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#5P#850F……哎，\x01",
            "为什么我会在这里？\x02\x03",

            "#851F呵呵，真讨厌……\x01",
            "按照惯例不是不能问这种问题的吗㈱\x02\x03",

            "#5P#853F这事暂且不提……\x01",
            "今天，我为你\x01",
            "准备了一个珍藏的计划。\x02\x03",

            "#850F这名字就是『轨迹之PONG』。#2700W \x01",
            "#20W就是所谓的\x01",
            "回答问题游戏啦……\x02\x03",

            "要不要来和我玩玩呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54B")

    Sleep(300)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #5
        "\x18\x07\x05挑战猜谜游戏吗？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_584")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_953")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【 挑战 】\x01",      # 0
            "【 放弃 】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5D6"),
        (1, "loc_8A0"),
        (SWITCH_DEFAULT, "loc_950"),
    )


    label("loc_5D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1B, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_681")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【 简单 】\x01",      # 0
            "★【 稍难 】\x01",      # 1
            "★【 极难 】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_64A"),
        (1, "loc_657"),
        (2, "loc_664"),
        (SWITCH_DEFAULT, "loc_671"),
    )


    label("loc_64A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E")

    label("loc_657")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E")

    label("loc_664")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E")

    label("loc_671")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67E")

    label("loc_67E")

    Jump("loc_7D1")

    label("loc_681")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_72C")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【 简单 】\x01",      # 0
            "★【 稍难 】\x01",      # 1
            "  【 极难 】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6F5"),
        (1, "loc_702"),
        (2, "loc_70F"),
        (SWITCH_DEFAULT, "loc_71C"),
    )


    label("loc_6F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729")

    label("loc_702")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729")

    label("loc_70F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729")

    label("loc_71C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_729")

    label("loc_729")

    Jump("loc_7D1")

    label("loc_72C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_7B9")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        380,
        330,
        1,
        (
            "★【 简单 】\x01",      # 0
            "  【 稍难 】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78F"),
        (1, "loc_79C"),
        (SWITCH_DEFAULT, "loc_7A9"),
    )


    label("loc_78F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B6")

    label("loc_79C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B6")

    label("loc_7A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B6")

    label("loc_7B6")

    Jump("loc_7D1")

    label("loc_7B9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_862")
    OP_56(0x0)

    ChrTalk(    #6
        0x10,
        (
            "#5P#853F呵呵，我就知道你会接受的。\x02\x03",

            "#5P#850F好了，\x01",
            "那我去换身衣服……\x02\x03",

            "#851F稍微等一下哦⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(300, 0, -1)
    OP_0D()

    label("loc_862")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (101, "loc_87B"),
        (102, "loc_882"),
        (103, "loc_889"),
        (255, "loc_890"),
        (SWITCH_DEFAULT, "loc_89D"),
    )


    label("loc_87B")

    Call(0, 4)
    Jump("loc_89D")

    label("loc_882")

    Call(0, 5)
    Jump("loc_89D")

    label("loc_889")

    Call(0, 6)
    Jump("loc_89D")

    label("loc_890")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_89D")

    label("loc_89D")

    Jump("loc_950")

    label("loc_8A0")

    OP_5F(0x0)
    OP_56(0x0)

    ChrTalk(    #7
        0x10,
        (
            "#5P#855F唉～好无聊啊。\x02\x03",

            "#5P#850F不过，也罢。\x01",
            "改变主意的话，随时都可以来哦。\x02\x03",

            "#5P那么，拜拜～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_950")

    label("loc_950")

    Jump("loc_584")

    label("loc_953")

    Return()

    # Function_3_1B3 end

    def Function_4_954(): pass

    label("Function_4_954")

    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240133, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E7"),
        (1, "loc_9F4"),
        (2, "loc_B50"),
        (SWITCH_DEFAULT, "loc_B8A"),
    )


    label("loc_9E7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_9F4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　一共有十个谜题，请选择正确答案。\x01",
            "　谜题的形式都是４选１，各有限制时间。\x01",
            "丂\x01",
            "　选择错误答案，或者超过限制时间\x01",
            "　就会计算一次『失误』。\x01",
            "　『失误』达到三次时，\x01",
            "　游戏将以失败告终，请注意。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_B41")

    label("loc_B41")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_B8A")

    label("loc_B50")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_B8A")

    label("loc_B8A")

    Jump("loc_97D")

    label("loc_B8D")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x19, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C88")
    OP_0D()
    Sleep(200)

    ChrTalk(    #9
        0x10,
        (
            "#5P#853F呵呵，真是遗憾啊。\x02\x03",

            "#854F那么，你打算怎么办呢。\x01",
            "再挑战一次吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x18\x07\x05再挑战一次谜题吗？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_C88")

    OP_0D()
    Sleep(200)

    ChrTalk(    #11
        0x10,
        (
            "#5P#853F呵呵，恭喜顺利过关⊙\x02\x03",

            "#850F好了……\x01",
            "已经玩够了，\x01",
            "我也差不多要回去了。\x02\x03",

            "嗯，有心情的话再来玩哦。\x01",
            "我随时欢迎。\x02\x03",

            "#851F好了，拜拜～⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00Episode『轨迹之PONG』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8A")
    OP_28(0x19, 0x4, 0x20)
    OP_28(0x1A, 0x4, 0x2)
    OP_3E(0x1E6, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00得到了\x1F\xE6\x01\x07\x00。\x02",
    )

    Jump("loc_DDF")

    label("loc_DDF")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E20")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x45)"), scpexpr(EXPR_END)), "loc_DFA")
    Jump("loc_E20")

    label("loc_DFA")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #14
        "\x1F\xE6\x01\x07\x00的制作方法已经记下了。\x02",
    )

    CloseMessageWindow()

    label("loc_E20")

    Sleep(1000)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05追加了难易度『稍难』。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        (
            "\x07\x05进入太阳之房间后，\x01",
            "可以从选项中选择难度挑战。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_E8A")

    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_4_954 end

    def Function_5_E9C(): pass

    label("Function_5_E9C")

    OP_28(0x1A, 0x4, 0x8)
    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240134, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F34"),
        (1, "loc_F41"),
        (2, "loc_109D"),
        (SWITCH_DEFAULT, "loc_10D7"),
    )


    label("loc_F34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10D7")

    label("loc_F41")

    SetMessageWindowPos(-1, 85, 55, 10)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　一共有十个谜题，请选择正确答案。\x01",
            "　谜题的形式都是４选１，各有限制时间。\x01",
            "丂\x01",
            "　选择错误答案，或者超过限制时间\x01",
            "　就会计算一次『失误』。\x01",
            "　『失误』达到三次时，\x01",
            "　游戏将以失败告终，请注意。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_108E")

    label("loc_108E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_10D7")

    label("loc_109D")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10D7")

    label("loc_10D7")

    Jump("loc_ECA")

    label("loc_10DA")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x1A, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    OP_0D()
    Sleep(200)

    ChrTalk(    #18
        0x10,
        (
            "#5P#853F呵呵，真是遗憾啊。\x02\x03",

            "#854F那么，你打算怎么办呢。\x01",
            "再挑战一次吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x18\x07\x05再挑战一次谜题吗？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_11D5")

    OP_0D()
    Sleep(200)

    ChrTalk(    #20
        0x10,
        (
            "#5P#853F呵呵，恭喜顺利过关⊙\x02\x03",

            "#850F好了……\x01",
            "已经玩够了，\x01",
            "我也差不多要回去了。\x02\x03",

            "嗯，有心情的话再来玩哦。\x01",
            "我随时欢迎。\x02\x03",

            "#851F好了，拜拜～⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x00Episode『轨迹之PONG』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1A, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    OP_28(0x1A, 0x4, 0x20)
    OP_28(0x1B, 0x4, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x8)"), scpexpr(EXPR_END)), "loc_130B")
    Jump("loc_134F")

    label("loc_130B")

    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #22
        "\x06\x07\x02暗汁『混沌』\x07\x00的制作方法已经记下了。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_134F")

    Sleep(1000)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05追加了难易度『极难』。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #24
        (
            "\x07\x05进入太阳之房间后，\x01",
            "可以从选项中选择难度挑战。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(2000)

    label("loc_13C7")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_E9C end

    def Function_6_13D4(): pass

    label("Function_6_13D4")

    OP_28(0x1B, 0x4, 0x8)
    Sleep(1000)
    OP_1D(0x19)
    OP_AD(0x240135, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1612")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_146C"),
        (1, "loc_1479"),
        (2, "loc_15D5"),
        (SWITCH_DEFAULT, "loc_160F"),
    )


    label("loc_146C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_160F")

    label("loc_1479")

    SetMessageWindowPos(-1, 85, 55, 10)
    SetChrName("")

    AnonymousTalk(    #25
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　一共有十个谜题，请选择正确答案。\x01",
            "　谜题的形式都是４选１，各有限制时间。\x01",
            "丂\x01",
            "　选择错误答案，或者超过限制时间\x01",
            "　就会计算一次『失误』。\x01",
            "　『失误』达到三次时，\x01",
            "　游戏将以失败告终，请注意。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_15C6")

    label("loc_15C6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_160F")

    label("loc_15D5")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_160F")

    label("loc_160F")

    Jump("loc_1402")

    label("loc_1612")

    OP_20(0x3E8)
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1A, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_28(0x1B, 0x4, 0x10)
    FadeToBright(4000, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170D")
    OP_0D()
    Sleep(200)

    ChrTalk(    #26
        0x10,
        (
            "#5P#853F呵呵，真是遗憾啊。\x02\x03",

            "#854F那么，你打算怎么办呢。\x01",
            "再挑战一次吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x18\x07\x05再挑战一次谜题吗？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_170D")

    OP_0D()
    Sleep(200)

    ChrTalk(    #28
        0x10,
        (
            "#5P#854F哦～竟然能通过这个……\x01",
            "你还真是钻研得够深啊。\x02\x03",

            "#853F好了……\x01",
            "已经玩够了，\x01",
            "我也差不多要回去了。\x02\x03",

            "#850F如果有兴趣了就再来玩。\x01",
            "我随时欢迎。\x02\x03",

            "#851F好了，拜拜～⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00Episode『轨迹之PONG』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_E3(0x1, 0x0)
    OP_11(0x0, 0x0, 0x0, 0xF4240, 0x1E8480, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1B, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188E")
    OP_28(0x1B, 0x4, 0x20)
    OP_3E(0x2E9, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x00得到了\x1F\xE9\x02\x07\x00。\x02",
    )

    Jump("loc_188B")

    label("loc_188B")

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_188E")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M5402   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_13D4 end

    def Function_7_18A4(): pass

    label("Function_7_18A4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F8")
    AddMira(1)

    AnonymousTalk(    #31
        "\x07\x00[Rank 10] \x07\x00得到了\x07\x02１米拉\x07\x00。\x02",
    )

    Jump("loc_18F5")

    label("loc_18F5")

    Jump("loc_1B3B")

    label("loc_18F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    AddMira(10)

    AnonymousTalk(    #32
        "\x07\x00[Rank 9] \x07\x00得到了\x07\x02１０米拉\x07\x00。\x02",
    )

    Jump("loc_193D")

    label("loc_193D")

    Jump("loc_1B3B")

    label("loc_1940")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197E")
    AddMira(100)

    AnonymousTalk(    #33
        "\x07\x00[Rank 8] \x07\x00得到了\x07\x02１００米拉\x07\x00。\x02",
    )

    Jump("loc_197B")

    label("loc_197B")

    Jump("loc_1B3B")

    label("loc_197E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BC")
    AddMira(500)

    AnonymousTalk(    #34
        "\x07\x00[Rank 7] \x07\x00得到了\x07\x02５００米拉\x07\x00。\x02",
    )

    Jump("loc_19B9")

    label("loc_19B9")

    Jump("loc_1B3B")

    label("loc_19BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19FC")
    AddMira(1000)

    AnonymousTalk(    #35
        "\x07\x00[Rank 6] \x07\x00得到了\x07\x02１０００米拉\x07\x00。\x02",
    )

    Jump("loc_19F9")

    label("loc_19F9")

    Jump("loc_1B3B")

    label("loc_19FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3C")
    AddMira(2000)

    AnonymousTalk(    #36
        "\x07\x00[Rank 5] \x07\x00得到了\x07\x02２０００米拉\x07\x00。\x02",
    )

    Jump("loc_1A39")

    label("loc_1A39")

    Jump("loc_1B3B")

    label("loc_1A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A7C")
    AddMira(3000)

    AnonymousTalk(    #37
        "\x07\x00[Rank 4] \x07\x00得到了\x07\x02３０００米拉\x07\x00。\x02",
    )

    Jump("loc_1A79")

    label("loc_1A79")

    Jump("loc_1B3B")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABC")
    AddMira(4000)

    AnonymousTalk(    #38
        "\x07\x00[Rank 3] \x07\x00得到了\x07\x02４０００米拉\x07\x00。\x02",
    )

    Jump("loc_1AB9")

    label("loc_1AB9")

    Jump("loc_1B3B")

    label("loc_1ABC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AFC")
    AddMira(5000)

    AnonymousTalk(    #39
        "\x07\x00[Rank 2] \x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_1AF9")

    label("loc_1AF9")

    Jump("loc_1B3B")

    label("loc_1AFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3B")
    AddMira(10000)

    AnonymousTalk(    #40
        "\x07\x00[Rank 1] \x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_1B3B")

    label("loc_1B3B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_7_18A4 end

    def Function_8_1B48(): pass

    label("Function_8_1B48")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1BEA")
    OP_1D(0xBF)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #41
        "\x18\x07\x05THE CASINO　赌博师杰克\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        160,
        0,
        (
            "从最初开始\x01",        # 0
            "从杰克篇开始\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Sleep(100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE3")
    OP_20(0x7D0)
    OP_21()
    Call(0, 9)
    Jump("loc_1BE7")

    label("loc_1BE3")

    Call(0, 10)

    label("loc_1BE7")

    Jump("loc_1BEE")

    label("loc_1BEA")

    Call(0, 9)

    label("loc_1BEE")

    Return()

    # Function_8_1B48 end

    def Function_9_1BEF(): pass

    label("Function_9_1BEF")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_1D(0x1)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS511._CH")
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x00──卡尔瓦德共和国。\x02\x01",

            "这个国家里，有一条从东方来的移民\x01",
            "由于思念故乡而仿照故乡建造而成的街道。\x02\x01",

            "　\x01",
            "以『东方人街』之名为人熟知，\x01",
            "东西贯通，人物交错——\x02\x01",

            "　\x01",
            "这条街的北端，\x01",
            "有一家破旧狭小的酒馆。\x02",
        )
    )

    Jump("loc_1D18")

    label("loc_1D18")

    CloseMessageWindow()

    AnonymousTalk(    #43
        (
            "\x07\x00在激荡黑暗世界的\x01",
            "世纪赌博对决之后数月——\x02\x01",

            "现在，这酒馆里有了两位本领高强的赌博高手。\x02\x01",

            "　\x01",
            "战胜过去的『胜利之杰克』，\x01",
            "和死缠着他的少女哈璐——\x02\x01",

            "　\x01",
            "围绕着两人的日子，\x01",
            "喧扰而又平静地过去——\x02",
        )
    )

    Jump("loc_1DE7")

    label("loc_1DE7")

    CloseMessageWindow()

    AnonymousTalk(    #44
        (
            "\x07\x00而今天店门也发出呻吟般的声音，\x01",
            "为酒馆带来新的客人——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_21()
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C4(0x1, 0x800)
    OP_22(0x177, 0x0, 0x64)
    Sleep(2500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    Sleep(1000)
    SetMessageWindowPos(340, 120, -1, -1)
    SetChrName("粗鲁的声音")

    AnonymousTalk(    #45
        (
            "\x07\x0C……啊？\x02\x03",

            "这人是谁啊！？\x02",
        )
    )

    Jump("loc_1EC5")

    label("loc_1EC5")

    CloseMessageWindow()
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("不怀好意的声音")

    AnonymousTalk(    #46
        (
            "\x07\x0C……这不是肥鸭吗，肥鸭。\x02\x03",

            "不过看起来，\x01",
            "倒是没背着葱来当香料嘛，嘎哈哈。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少女的声音")

    AnonymousTalk(    #47
        (
            "\x07\x00各、各位，等等!\x01",
            "不要这样就突然缠上别人啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    OP_22(0xEA, 0x1, 0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #48
        (
            "\x07\x00呼，对不起。\x01",
            "让你吓了一跳吧？\x02\x03",

            "虽然看上去这个样子，\x01",
            "不过他们绝不是坏人……\x02\x03",

            "你……是客人吧……？\x02\x03",

            "我来带路，跟我来吧。\x02",
        )
    )

    Jump("loc_20D6")

    label("loc_20D6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x15)
    Sleep(2000)
    SetMessageWindowPos(150, -1, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #49
        (
            "\x07\x00#1911F呵呵，真是挺稀奇的。\x02\x03",

            "这么破烂的酒吧……\x01",
            "大白天的也会有客人过来。\x02\x03",

            "#1915F啊，但是请不要误会。\x01",
            "这儿并不是什么不好的店。\x02\x03",

            "虽然这屋子破烂不堪，\x01",
            "常来的客人品行也不能说很好……\x02\x03",

            "#1910F该怎么说呢，这儿很暖和……\x02\x03",

            "而且单品料理和套餐\x01",
            "的确相当的美味。\x02",
        )
    )

    Jump("loc_2235")

    label("loc_2235")

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x0, 0x0)
    Sleep(700)
    OP_22(0x16C, 0x0, 0x96)
    Sleep(200)
    SetMessageWindowPos(150, -1, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #50
        (
            "\x07\x00#1913F啊，小心脚下。\x01",
            "这里的地板快要崩落了。\x02",
        )
    )

    Jump("loc_2297")

    label("loc_2297")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #51
        "\x07\x00#1910F……快坐下吧。\x02",
    )

    Jump("loc_22E8")

    label("loc_22E8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x16E, 0x0, 0x64)
    Sleep(700)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(500)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    Sleep(800)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #52
        (
            "\x07\x00那么，想点些什么？\x02\x03",

            "看来你也不是打算\x01",
            "到这里来喝酒的样子……\x02\x03",

            "对了，那就给你推荐……\x01",
            "火龙东央贡汤，怎么样？\x02\x03",

            "辣乎乎的味道和\x01",
            "恰到好处的酸味，挺不错的。\x01",
            "是这里最受欢迎的菜了。\x02",
        )
    )

    Jump("loc_241D")

    label("loc_241D")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #53
        (
            "\x07\x00好吧，那就点这个了。\x02\x03",

            "饮料……水就可以了吗？\x02",
        )
    )

    Jump("loc_2479")

    label("loc_2479")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS553._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #54
        (
            "\x07\x00……咦？你说什么？\x02\x03",

            "——杰克？\x02\x03",

            "杰克吗，现在这个时候\x01",
            "我猜他正在里面什么地方睡觉……\x02",
        )
    )

    Jump("loc_255C")

    label("loc_255C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #55
        (
            "\x07\x00……你……不会是\x01",
            "来和杰克一决胜负的吧？\x02\x03",

            "你又订桌子\x01",
            "又点菜的，\x01",
            "我根本没想到会是……\x02\x03",

            "……嗯，好吧。\x01",
            "我去帮你问一下。\x02\x03",

            "如果他心情好的话\x01",
            "也许能陪你玩一会儿。\x02\x03",

            "那么，请稍等一下。\x02",
        )
    )

    Jump("loc_26A9")

    label("loc_26A9")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(2000)
    SetMessageWindowPos(340, 80, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #56
        (
            "\x07\x0C……喂，听到了吗？\x02\x03",

            "那边的那个家伙，\x01",
            "居然想向杰克挑战。\x02",
        )
    )

    Jump("loc_274A")

    label("loc_274A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #57
        (
            "\x07\x0C啊，的确是这样。\x02\x03",

            "嘿嘿，\x01",
            "或许又有好戏看了。\x02",
        )
    )

    Jump("loc_27B1")

    label("loc_27B1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(160, 20, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #58
        (
            "\x07\x0C……哼，难说。\x02\x03",

            "想让杰克亮出真功夫，\x01",
            "简直难于登天。\x02",
        )
    )

    Jump("loc_2817")

    label("loc_2817")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    Sleep(2000)
    OP_22(0x16F, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #59
        (
            "\x07\x00来了，\x01",
            "这是您点的火龙东央贡汤。\x02\x03",

            "最好趁热\x01",
            "一口气喝完哦。\x02",
        )
    )

    Jump("loc_28CB")

    label("loc_28CB")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS554._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #60
        (
            "\x07\x00对了，关于和杰克对局的事情……\x01",
            "他说这次就免了。\x02\x03",

            "好像是因为\x01",
            "昨天的酒还没醒的样子。\x01",
            "而且他也懒得起来。\x02\x03",

            "……对不起，\x01",
            "难得你特意过来一趟……\x02",
        )
    )

    Jump("loc_29EA")

    label("loc_29EA")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #61
        (
            "\x07\x00……好吧！\x01",
            "你看这么办行吗？\x02\x03",

            "如果你胜了我的话，\x01",
            "我就再去帮你恳请一次。\x02\x03",

            "要是能打败我的话，\x01",
            "那家伙应该也会对你有兴趣的。\x02",
        )
    )

    Jump("loc_2AF6")

    label("loc_2AF6")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("少女")

    AnonymousTalk(    #62
        (
            "\x07\x00……觉得意外吗？\x01",
            "别看我这个样子，我也能来两下呢。\x02\x03",

            "我叫哈璐——\x01",
            "传说中的赌博师『王』的女儿。\x02\x03",

            "虽然并不广为人知，\x01",
            "但在这一行也算相当有名哦。\x02",
        )
    )

    Jump("loc_2BB8")

    label("loc_2BB8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS555._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #63
        (
            "\x07\x00当然，我不会手下留情。\x02\x03",

            "如果你输了，那就马上给我回去——\x02\x03",

            "只要你同意这条件，我们这就开始吧？\x02",
        )
    )

    Jump("loc_2CA4")

    label("loc_2CA4")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x170, 0x0, 0x64)
    Sleep(800)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS555._CH")
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #64
        (
            "\x07\x00呵呵，你是说ＯＫ吗？\x02\x03",

            "那我们这就换个地方\x01",
            "准备开始吧。\x02\x03",

            "我们来比――\x01",
            "『二十一点』如何？\x02",
        )
    )

    Jump("loc_2DC5")

    label("loc_2DC5")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1600)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3654")
    OP_AD(0x24013B, 0x0, 0x0, 0x1F4)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_321D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EA7"),
        (1, "loc_2EB4"),
        (2, "loc_31F0"),
        (SWITCH_DEFAULT, "loc_321A"),
    )


    label("loc_2EA7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_321A")

    label("loc_2EB4")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　用『二十一点』与哈璐进行一对一决战。\x01",
            "　采用七局四胜制，\x01",
            "　谁先胜出四盘就结束。\x01",
            "　游戏内各项指令的说明如下。\x01",
            "　\x01",
            "　【ＨＩＴ】　　：抽取一张牌。\x01",
            "　　　　　　　　　在BURST（牌面的合计值超过２１）之前\x01",
            "　　　　　　　　　最多可以抽取７张。\x01",
            "　\x01",
            "　【ＳＴＡＮＤ】：用当前手中的卡片进行较量。\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_3067")

    label("loc_3067")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05#0W―――――――――《   规则说明   》―――――――――\x01",
            "　\x01",
            "　合计值在２１以下，而且手上的牌数达到７张，\x01",
            "　就成为『７小龙』的牌型，\x01",
            "　这是比『二十一点（卡片的合计值为２１）』\x01",
            "　还要强的牌型。\x01",
            "　\x01",
            "　除此之外没有其它任何牌型。\x01",
            "　无论如何，就以２１为目标抽牌吧。\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_31E1")

    label("loc_31E1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_321A")

    label("loc_31F0")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_321A")

    label("loc_321A")

    Jump("loc_2E3D")

    label("loc_321D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1D, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    OP_21()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328A")
    Jump("loc_3654")

    label("loc_328A")

    Sleep(1000)
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS556._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #67
        (
            "\x07\x00唉，只有这种程度吗……\x01",
            "真是让人失望。\x02\x03",

            "嗯，只靠这点本事\x01",
            "就算和杰克交手也只会输。\x02\x03",

            "虽然有些残酷，不过规则就是规则。\x01",
            "之前说好了，今天就请回吧。\x02\x03",

            "呵呵，\x01",
            "下次可要好好练习后再来哦。\x02",
        )
    )

    Jump("loc_33E8")

    label("loc_33E8")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #68
        "\x18\x07\x05再度挑战小游戏吗？\x02",
    )

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_357E")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【降低难度后挑战】\x01",          # 0
            "【不改变难度继续挑战】\x01",      # 1
            "【放弃】\x01",                    # 2
        )
    )

    Jump("loc_3494")

    label("loc_3494")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34C3"),
        (1, "loc_3509"),
        (2, "loc_3534"),
        (SWITCH_DEFAULT, "loc_3534"),
    )


    label("loc_34C3")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3506")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3506")

    Jump("loc_357B")

    label("loc_3509")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_357B")

    label("loc_3534")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1500, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_357B")

    label("loc_357B")

    Jump("loc_3651")

    label("loc_357E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【 是 】\x01",      # 0
            "【 否 】\x01",      # 1
        )
    )

    Jump("loc_35B4")

    label("loc_35B4")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35DF"),
        (1, "loc_360A"),
        (SWITCH_DEFAULT, "loc_360A"),
    )


    label("loc_35DF")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3651")

    label("loc_360A")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_3651")

    label("loc_3651")

    Jump("loc_2DFF")

    label("loc_3654")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3701")
    Sleep(2000)
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x20)
    OP_28(0x20, 0x4, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x2)"), scpexpr(EXPR_END)), "loc_367E")
    Jump("loc_36C2")

    label("loc_367E")

    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #69
        "\x06\x07\x02火龙东央贡汤\x07\x00的制作方法已经记下了。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_36C2")

    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #70
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_36F5")

    label("loc_36F5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_3701")

    Call(0, 10)
    Return()

    # Function_9_1BEF end

    def Function_10_3706(): pass

    label("Function_10_3706")

    OP_28(0x20, 0x4, 0x8)
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS511._CH")
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    Sleep(1000)
    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #71
        (
            "\x07\x00……真让人吃惊，你挺行的嘛。\x02\x03",

            "好吧，那我就\x01",
            "把你的事情和杰克说一下。\x02",
        )
    )

    Jump("loc_381C")

    label("loc_381C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    Sleep(500)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(1000)
    SetMessageWindowPos(340, 120, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #72
        (
            "\x07\x0C看，那家伙……\x01",
            "居然胜了哈璐。\x02",
        )
    )

    Jump("loc_38A2")

    label("loc_38A2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #73
        (
            "\x07\x0C……好像是的。\x02\x03",

            "这下说不定\x01",
            "有好戏看了。\x02",
        )
    )

    Jump("loc_38FC")

    label("loc_38FC")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_22(0xEA, 0x1, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("沙哑的声音")

    AnonymousTalk(    #74
        "\x07\x00呵啊～我还没睡够呢。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x2, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("衣衫不整的男人")

    AnonymousTalk(    #75
        (
            "\x07\x00哦，有个陌生面孔呢。\x02\x03",

            "难道这就是\x01",
            "哈璐说的那个人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS567._CH")
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("衣衫不整的男人")

    AnonymousTalk(    #76 op#A op#5
        (
            "\x07\x00#51A痛痛痛……\x01",
            "脑袋里面一跳一跳地痛#150W……\x05\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("衣衫不整的男人")

    AnonymousTalk(    #77 op#A op#5
        "\x07\x00#5A#20W哇！？\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x171, 0x0, 0x64)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #78
        "\x07\x00#1914F唉～糟了。\x02",
    )

    Jump("loc_3B3A")

    label("loc_3B3A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(40, 120, -1, -1)
    SetChrName("不怀好意的声音")

    AnonymousTalk(    #79
        (
            "\x07\x0C哈哈哈，瞧。\x01",
            "正如我说的吧？\x02\x03",

            "杰克这家伙，\x01",
            "结果还是把这破地板踏穿了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(340, 80, -1, -1)
    SetChrName("粗鲁的声音")

    AnonymousTalk(    #80
        (
            "\x07\x0C呵呵，的确如此。\x02\x03",

            "除了玩牌之外，\x01",
            "这家伙真是\x01",
            "丝毫运气都没有啊。\x02\x03",

            "……或者该说他只是迟钝而已吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS562._CH")
    OP_C6(0x2, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #81
        (
            "\x07\x00啊！？刚才的话是不是你说的？\x02\x03",

            "喂，想打架啊，随时奉陪！\x02",
        )
    )

    Jump("loc_3CE8")

    label("loc_3CE8")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(240, 180, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #82
        (
            "\x07\x00#1916F……好了好了，到此为止。\x01",
            "想打架就到外面去打。\x02\x03",

            "如果把这酒店弄得更加破落\x01",
            "那谁来负这个责？\x02\x03",

            "#1915F还有，杰克……\x01",
            "这地板就由你来修理吧。\x02",
        )
    )

    Jump("loc_3DAA")

    label("loc_3DAA")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #83
        "\x07\x00为、为什么是我……\x02",
    )

    Jump("loc_3DE5")

    label("loc_3DE5")

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(240, 180, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #84
        "\x07\x00#1912F（瞪……！）\x02",
    )

    Jump("loc_3E1E")

    label("loc_3E1E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS564._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #85
        (
            "\x07\x00……哼，知道了。\x02\x03",

            "嘁，真是麻烦。\x02",
        )
    )

    Jump("loc_3EC7")

    label("loc_3EC7")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(360, 220, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #86
        (
            "\x07\x0C呵呵，自从哈璐来了之后，\x01",
            "杰克这家伙安静多了，\x01",
            "真是帮了大忙啊。\x02",
        )
    )

    Jump("loc_3F37")

    label("loc_3F37")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(10, 110, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #87
        "\x07\x0C啊，说的没错。\x02",
    )

    Jump("loc_3F72")

    label("loc_3F72")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS562._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(-1, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #88
        "\x07\x00……………………\x02",
    )

    Jump("loc_4004")

    label("loc_4004")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_C6(0x2, 0x0, -110000, 0, 1000)
    OP_C6(0x1, 0x0, 110000, 0, 0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #89
        (
            "\x07\x00……不好意思，让你久等了。\x01",
            "我按照约定把杰克带来了。\x02",
        )
    )

    Jump("loc_40CD")

    label("loc_40CD")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #90
        (
            "\x07\x00……那么。\x02\x03",

            "想和我一决胜负的\x01",
            "就是眼前这家伙吗？\x02",
        )
    )

    Jump("loc_4185")

    label("loc_4185")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #91
        "\x07\x00是，你猜对了。\x02",
    )

    Jump("loc_41B7")

    label("loc_41B7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #92
        (
            "\x07\x00嗯，乍一看\x01",
            "也没啥了不起的样子。\x02",
        )
    )

    Jump("loc_41FA")

    label("loc_41FA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #93
        (
            "\x07\x00呵呵，可不要麻痹大意\x01",
            "到头来被人家踩个粉碎哦。\x02\x03",

            "就像刚才的地板一样。\x02",
        )
    )

    Jump("loc_4268")

    label("loc_4268")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #94
        "\x07\x00哼………\x02",
    )

    Jump("loc_42A0")

    label("loc_42A0")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x16E, 0x0, 0x64)
    Sleep(200)
    Sleep(500)
    OP_22(0xD1, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS561._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #95
        (
            "\x07\x00忘了做自我介绍了――\x01",
            "我叫杰克，请多关照。\x02\x03",

            "……好了，不管其它的，\x01",
            "先来点酒。\x02\x03",

            "喂，哈璐，拿威士忌来！\x01",
            "当然是要纯的。\x02",
        )
    )

    Jump("loc_43C1")

    label("loc_43C1")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS554._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #96
        (
            "\x07\x00啊，杰克……\x01",
            "你不是从昨天就开始醉了吗？\x02",
        )
    )

    Jump("loc_446A")

    label("loc_446A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #97
        (
            "\x07\x00啊，那个没有关系。\x01",
            "昨天的酒现在刚醒。\x02\x03",

            "喂，哈璐，快点啦。\x02",
        )
    )

    Jump("loc_44CE")

    label("loc_44CE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #98
        "\x07\x00真是个无可救药的家伙。\x02",
    )

    Jump("loc_4508")

    label("loc_4508")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1200, 0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(2000)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #99
        (
            "\x07\x00怎么，你觉得哈璐很奇怪吗？\x02\x03",

            "虽然现在一点姿色都没有，\x01",
            "不过，将来一定会是位十分出众的姑娘。\x02\x03",

            "不知为何突然心血来潮，\x01",
            "提出要到这种\x01",
            "脏兮兮的地方来干活……\x02\x03",

            "……好了，这些都无关紧要。\x02",
        )
    )

    Jump("loc_467D")

    label("loc_467D")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS565._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #100
        (
            "\x07\x00不过，你的胆子\x01",
            "也真是够大的啊。\x02\x03",

            "居然敢一个人跑到\x01",
            "这种偏僻的破酒吧来……\x02\x03",

            "像你这种人，还真是少见啊。\x02",
        )
    )

    Jump("loc_4771")

    label("loc_4771")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_22(0x16F, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #101
        (
            "\x07\x00你们好像跑题了吧。\x01",
            "给，我拿来了。\x02",
        )
    )

    Jump("loc_4823")

    label("loc_4823")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x4, 0x3, -1, 500, 0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #102
        (
            "\x07\x00哦哦，谢了。\x02\x03",

            "对了，你不用回去工作吗？\x02",
        )
    )

    Jump("loc_48D2")

    label("loc_48D2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #103
        (
            "\x07\x00呵呵，这么有趣的事情摆在面前\x01",
            "谁还有心情去管店里的事啊。\x02\x03",

            "我已经告诉过店长了，\x01",
            "就让我参观一下嘛。\x02",
        )
    )

    Jump("loc_495D")

    label("loc_495D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #104
        (
            "\x07\x00唉，真是够随便的店啊。\x02\x03",

            "也罢，赶快开始吧。\x02",
        )
    )

    Jump("loc_49B2")

    label("loc_49B2")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS561._CH")
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #105
        (
            "\x07\x00哟，这可是你挑起的对决。\x02\x03",

            "那就让我来决定\x01",
            "用什么来比试吧。\x02\x03",

            "用我最擅长的游戏――\x01",
            "『扑克』来一决胜负！\x02",
        )
    )

    Jump("loc_4AA6")

    label("loc_4AA6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    Sleep(1600)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57EE")
    OP_1D(0xBF)
    OP_AD(0x24013C, 0x0, 0x0, 0x1F4)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52EA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "【　开始　】\x01",      # 0
            "【　说明　】\x01",      # 1
            "【　结束　】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B8A"),
        (1, "loc_4B97"),
        (2, "loc_52BD"),
        (SWITCH_DEFAULT, "loc_52E7"),
    )


    label("loc_4B8A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52E7")

    label("loc_4B97")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        (
            "\x07\x05#0W―――――――――――《   规则说明   》―――――――――――\x01",
            "　\x01",
            "　用变化了规则的『扑克』与杰克进行一对一的较量。\x01",
            "　在这种规则下，桌子中间的三张牌会作为『公用牌』，\x01",
            "　玩家和杰克都可以将他们组合到『牌型』中。\x01",
            "　\x01",
            "　再加上分配的其它三张『手牌』，\x01",
            "　最后要从这六张牌中选出五张形成『牌型』。\x01",
            "　\x01",
            "　胜负以争夺星（☆）的方式来进行。\x01",
            "　玩家开始拥有三颗星，\x01",
            "　如果能增加到七个即为胜利。\x01",
            "　相反玩家的星全部失去就是杰克获胜，游戏结束。\x01",
            "　\x01",
            "　\x01",
            "―――――――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_4DAC")

    label("loc_4DAC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #107
        (
            "\x07\x05#0W―――――――――――《   规则说明   》―――――――――――\x01",
            "　\x01",
            "　游戏内各种命令的说明如下。\x01",
            "　\x01",
            "　【CHANGE】 ：将『HOLD状态』以外的牌换掉，\x01",
            "　　　　　　　　然后决定胜负。（最多只能换掉一次）\x01",
            "　【ALLHOLD】：将所有的卡片都设定为『HOLD状态』。\x01",
            "　【RAISE】　：将所押的星数增加为两个。（通常为一个）\x01",
            "　【FOLD】 　：将『公用牌』与『手牌』进行交换。\x01",
            "　　　　　　　（每次对决只能交换一次）\x01",
            "　\x01",
            "　※设定『HOLD状态』时\x01",
            "　  可直接单击牌进行切换。\x01",
            "　　若一张牌也想不交换，\x01",
            "　　请将所有手牌设为『HOLD状态』。\x01",
            "―――――――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_5009")

    label("loc_5009")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #108
        (
            "\x07\x05#0W―――――――――――《   规则说明   》―――――――――――\x01",
            "　\x01",
            "　『牌型』的说明如下。\x01",
            "　越往下的『牌型』就越强。\x01",
            "　\x01",
            "　【NO PAIR】　　　：没有形成下列任何一种『牌型』。\x01",
            "　【1 PAIR】　　　 ：相同数字的牌有２张。\x01",
            "　【2 PAIR】　　　 ：有两组1 PAIR。\x01",
            "　【3 OF A KIND】　：相同数字的牌有３张。\x01",
            "　【STRAIGHT】　　 ：５张牌的数字是连续的。\x01",
            "　【FLUSH】　　　　：５张牌的花色相同。\x01",
            "　【FULLHOUSE】　　：同时形成3 OF A KIND和1 PAIR。\x01",
            "　【4 OF A KIND】　：相同数字的牌有４张。\x01",
            "　【STRAIGHTFLUSH】：同时形成STRAIGHT和FLUSH。\x01",
            "　【ROYALFLUSH】　 ：10，Ｊ，Ｑ，Ｋ，Ａ的STRAIGHTFLUSH。\x01",
            "―――――――――――――――――――――――――――――――#20W\x02",
        )
    )

    Jump("loc_52AE")

    label("loc_52AE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_52E7")

    label("loc_52BD")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_52E7")

    label("loc_52E7")

    Jump("loc_4B20")

    label("loc_52EA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x1C, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    OP_21()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5357")
    Jump("loc_57EE")

    label("loc_5357")

    OP_1D(0xBF)
    OP_22(0xEA, 0x1, 0x64)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #109
        (
            "\x07\x00唉，我真是看错人了。\x02\x03",

            "既然打败了哈璐，\x01",
            "我还以为你会更强一些呢。\x02",
        )
    )

    Jump("loc_5463")

    label("loc_5463")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #110
        (
            "\x07\x00嗯～我可是觉得\x01",
            "刚才那应该不是碰巧……\x02",
        )
    )

    Jump("loc_54AC")

    label("loc_54AC")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #111
        (
            "\x07\x00……唉，算了。\x01",
            "还真是扫兴。\x02\x03",

            "下次再来的时候，\x01",
            "记得给我看点更强的招数啊。\x02",
        )
    )

    Jump("loc_5524")

    label("loc_5524")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #112
        "\x18\x07\x05再度挑战小游戏吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56FF")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【降低难度后挑战】\x01",          # 0
            "【不改变难度继续挑战】\x01",      # 1
            "【放弃】\x01",                    # 2
        )
    )

    Jump("loc_55E4")

    label("loc_55E4")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5613"),
        (1, "loc_5668"),
        (2, "loc_56A2"),
        (SWITCH_DEFAULT, "loc_56A2"),
    )


    label("loc_5613")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5665")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5665")

    Jump("loc_56FC")

    label("loc_5668")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_56FC")

    label("loc_56A2")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_56FC")

    label("loc_56FC")

    Jump("loc_57EB")

    label("loc_56FF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "【 是 】\x01",      # 0
            "【 否 】\x01",      # 1
        )
    )

    Jump("loc_5735")

    label("loc_5735")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5757"),
        (1, "loc_5791"),
        (SWITCH_DEFAULT, "loc_57EB"),
    )


    label("loc_5757")

    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_57EB")

    label("loc_5791")

    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 1500, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_21()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_57EB")

    label("loc_57EB")

    Jump("loc_4AEF")

    label("loc_57EE")

    OP_1D(0xBF)
    OP_C6(0x0, 0x3, -1, 3000, 0)
    Sleep(3000)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1500, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2000)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #113
        (
            "\x07\x00……原来如此，\x01",
            "本事不错嘛。\x02\x03",

            "我会老实认输的。\x02",
        )
    )

    Jump("loc_58E3")

    label("loc_58E3")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_22(0xEA, 0x1, 0x64)
    Sleep(1000)
    SetMessageWindowPos(360, 220, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #114
        (
            "\x07\x0C喂，不会吧……\x01",
            "杰克居然被打败了。\x02",
        )
    )

    Jump("loc_5940")

    label("loc_5940")

    CloseMessageWindow()
    SetMessageWindowPos(80, 260, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #115
        (
            "\x07\x0C笨蛋，你没看出来\x01",
            "杰克根本就没有认真玩吗。\x02\x03",

            "……嗯，不过说不定\x01",
            "对手也是一样啦。\x02",
        )
    )

    Jump("loc_59BF")

    label("loc_59BF")

    CloseMessageWindow()
    SetMessageWindowPos(280, 280, -1, -1)
    SetChrName("窃窃私语")

    AnonymousTalk(    #116
        (
            "\x07\x0C是、是啊……\x01",
            "总之，还真是场精彩的比赛啊。\x02",
        )
    )

    Jump("loc_5A13")

    label("loc_5A13")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xEA, 0x1, 0x0)
    Sleep(1000)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #117
        "\x07\x00呵呵，真是引人注目呢。\x02",
    )

    Jump("loc_5A57")

    label("loc_5A57")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x4, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS565._CH")
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #118
        (
            "\x07\x00嗯，既然有这种本事，\x01",
            "已经足够去独闯天下了。\x02\x03",

            "虽然输了是不甘心，\x01",
            "不过我也很久没有这样\x01",
            "纯粹地享受赌博的乐趣了。\x02",
        )
    )

    Jump("loc_5B4D")

    label("loc_5B4D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #119
        (
            "\x07\x00确实哦，只是在一旁看着，\x01",
            "就连我都想玩扑克了哦。\x02",
        )
    )

    Jump("loc_5BA0")

    label("loc_5BA0")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x2, 0x0, 0x0, 0x200, 0x200, 0xFF92, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS560._CH")
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x4, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #120
        (
            "\x07\x00嗯，那个……\x02\x03",

            "只要愿意的话，随时都可以来哦。\x01",
            "到时我们再来比试比试。\x02\x03",

            "话说在前头，我的实力\x01",
            "可远不止这样而已哦。\x02",
        )
    )

    Jump("loc_5C9E")

    label("loc_5C9E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS551._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #121
        (
            "\x07\x00呵呵，竟敢说这种话……\x02\x03",

            "引火上身的，\x01",
            "不正是杰克你吗。\x02",
        )
    )

    Jump("loc_5D5C")

    label("loc_5D5C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #122
        "\x07\x00哦，还真敢说。\x02",
    )

    Jump("loc_5D8E")

    label("loc_5D8E")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS557._CH")
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x3, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #123
        (
            "\x07\x00呵呵……那个就暂且不提了。\x01",
            "我和杰克的心情是一样的。\x02\x03",

            "无论何时都欢迎你到这里来。\x01",
            "然后，再来切磋一番。\x02",
        )
    )

    Jump("loc_5E7B")

    label("loc_5E7B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x3, 0x0, 0x0, 0x200, 0x200, 0x6E, 0x0, 0x300, 0x200, 0x0, 0x0, 0x200, 0x200, 0xFFFFFF, 0x0, "C_VIS550._CH")
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(800)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(30, 270, -1, -1)
    SetChrName("杰克")

    AnonymousTalk(    #124
        (
            "\x07\x00就这么定了，好吗。\x01",
            "你可不能赢了就跑哦。\x02",
        )
    )

    Jump("loc_5F24")

    label("loc_5F24")

    CloseMessageWindow()
    OP_56(0x0)
    OP_23(0xEA)
    OP_C6(0x0, 0x3, 16777215, 5000, 0)
    FadeToDark(5000, 16777215, -1)
    OP_0D()
    Sleep(1500)
    SetMessageWindowPos(350, 310, -1, -1)
    SetChrName("哈璐")

    AnonymousTalk(    #125
        (
            "\x07\x00那么，你这就要回去了。\x02\x03",

            "呵呵，再见……\x01",
            "期待有机会能再见面。\x02",
        )
    )

    Jump("loc_5FAC")

    label("loc_5FAC")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x3, 0x3, 16777215, 2000, 0)
    OP_C6(0x2, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_20(0xFA0)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x00Episode『THE CASINO～赌博师杰克～』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D5")
    Sleep(1000)
    OP_28(0x20, 0x4, 0x10)
    OP_28(0x20, 0x4, 0x20)
    OP_3E(0x163, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x00得到了\x1F\x63\x01\x07\x00。\x02",
    )

    Jump("loc_6093")

    label("loc_6093")

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #128
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_60C9")

    label("loc_60C9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_60D5")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3706 end

    def Function_11_60E2(): pass

    label("Function_11_60E2")

    Return()

    # Function_11_60E2 end

    def Function_12_60E3(): pass

    label("Function_12_60E3")

    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    Sleep(200)
    OP_24(0x1C3, 0xA)
    Sleep(200)
    OP_24(0x1C3, 0x0)
    OP_23(0x1C3)
    Return()

    # Function_12_60E3 end

    def Function_13_613C(): pass

    label("Function_13_613C")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_1D(0x64)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #129
        (
            "\x07\x00夜空中布满了星星，仿佛就要飘落下来——\x02\x01",

            "夜风吹拂，森林轻摇——\x01",
            "忽然，一线流星从夜空中划过。\x02\x01",

            "　\x01",
            "绽放着七耀的光辉从天而降\x01",
            "仿如空之女神落下的泪滴。\x02",
        )
    )

    Jump("loc_6206")

    label("loc_6206")

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #130
        (
            "\x07\x00——不可思议的事情随之而来。\x02\x01",

            "　\x01",
            "流星本应放射出瞬间的光辉，其后悄然消逝\x01",
            "然而它却在漆黑的空中放射出眩目的闪光——\x02\x01",

            "然后分散成数条光线，\x01",
            "划出轨道落向地面。\x02",
        )
    )

    Jump("loc_62B7")

    label("loc_62B7")

    CloseMessageWindow()

    AnonymousTalk(    #131
        (
            "\x07\x00其在分开时变成16条线\x01",
            "分别降临在16个人的面前。\x02\x01",

            "　\x01",
            "接下的事令人惊异——。\x01",
            "七耀的光辉将他们包围，\x01",
            "分别向他们讲述。\x02",
        )
    )

    Jump("loc_6334")

    label("loc_6334")

    CloseMessageWindow()

    AnonymousTalk(    #132
        (
            "\x07\x05『人啊……人之子啊………\x01",
            "  听得见我的声音吗……』\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #133
        (
            "\x07\x05『你被授予参加试炼……\x01",
            "  请环游王国一周，造访王城吧。』\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #134
        (
            "\x07\x05『追寻在同一天空下生活的\x01",
            "  各种各样的人们那多姿多彩的人生……\x01",
            "  追寻那无数相互交织的思想之轨迹。』\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #135
        "\x07\x05『人啊……人之子啊………』\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #136
        (
            "\x07\x05『当你完成之时，\x01",
            "  我将赐予你祝福。』\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_56(0x0)
    OP_C4(0x1, 0x800)
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x5, (scpexpr(EXPR_EXEC_OP, "OP_C0(0x19, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1000   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_613C end

    def Function_14_64C4(): pass

    label("Function_14_64C4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64DC")

    label("loc_64DC")

    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/U5110   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_64C4 end

    def Function_15_64EE(): pass

    label("Function_15_64EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    Sleep(3500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #137
        (
            "\x07\x00#2S#80W诺桑比亚旧大公国由于『盐之桩』所造成的损害情况。#20W\x02\x01",

            "　　　　 #80W以及有关『桩』的研究报告――#20W\x02\x01",

            "　\x01",
            "　　　　　　　　　　　　　　　#80W亚尔特利亚法典国·封圣省。#20W\x02",
        )
    )

    Jump("loc_65DB")

    label("loc_65DB")

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0x6E)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS328._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #138
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "谨以本报告，向作为众生之母的女神之座前，最可敬的导师，\x01",
            "至高的法王阁下复命#150W…………#20W\x02\x01",

            "　\x01",
            "　\x01",
            "机密#150W…………#20W\x02\x01",

            "本报告书仅限枢密院内阅览。\x02\x01",

            "然则，关于一部分秘匿事项的文字已被涂抹掉。\x02",
        )
    )

    Jump("loc_67AF")

    label("loc_67AF")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #139
        "\x07\x00#2S『桩』出现的事件经过――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)

    AnonymousTalk(    #140
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "#150W七耀历１１７８年７月１日，上午５时４５分――#20W\x02\x01",

            "　\x01",
            "　\x01",
            "塞姆里亚大陆北部诺桑比亚旧大公国（※现为自治州）\x01",
            "哈利亚斯科大圣堂发布紧急消息。\x02\x01",

            "内容为：旧公都哈利亚斯科近郊，\x01",
            "出现『直冲云霄的白色巨柱』。\x02\x01",

            "　\x01",
            "　\x01",
            "报告者阿雷克赛司教表现相当惊慌――\x02\x01",

            "受审问会紧急命令，在邻国执行其它任务的\x01",
            "星杯骑士２名（第八位『吼天狮子』与随从骑士一名）\x01",
            "被派遣到当地。#20W\x02",
        )
    )

    Jump("loc_69C5")

    label("loc_69C5")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #141
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "星杯骑士驾驶当时刚刚投入应用的\x01",
            "特殊作战艇『梅尔卡瓦』八号机，急速赶往当地。\x02\x01",

            "　\x01",
            "　\x01",
            "同日上午６时２２分。\x02\x01",

            "该事件已得到确认#150W…………#20W\x02",
        )
    )

    Jump("loc_6A99")

    label("loc_6A99")

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS331._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2000)
    SetMessageWindowPos(-1, 416, 52, 2)
    SetChrName("")

    AnonymousTalk(    #142
        "\x07\x00#2S――现在被称为『盐之桩』的物体。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #143
        (
            "\x07\x00#2S虽被命名为『桩』，\x01",
            "但最初发现时，总高度已超过数百亚矩――\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #144
        "\x07\x00#2S――其气势之宏伟，几可称之为矗立于大地之上的巨塔。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #145
        "\x07\x00#2S关于当时的状况，星杯骑士作了如下报告――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #146
        (
            "\x07\x00#2S『公都哈利亚斯科方向吹来混乱交错的猛烈逆风――\x01",
            "  最后我发现那不是冰，而是盐的碎片。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #147
        "\x07\x00#2S『物体的表面已被盐所覆盖而不可见――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 416, 52, 2)

    AnonymousTalk(    #148
        (
            "\x07\x00#2S  周围的空气化为盐的微粒逐渐沉降，\x01",
            "  其姿态正如在冻原上缓缓飘落的雪花。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #149
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "这种可被称为『盐化』的现象进行速度极其惊人，\x01",
            "损害在瞬间扩大――\x02\x01",

            "　\x01",
            "　\x01",
            "星杯骑士到达时旧公都全域都化成了盐，\x01",
            "确认已有大量来不及逃避的市民（包括司教）遇难。\x02",
        )
    )

    Jump("loc_6E26")

    label("loc_6E26")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #150
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "出现后一昼夜――\x02\x01",

            "旧公都北部延伸开来的广大针叶林带也因结晶化而崩毁。\x02\x01",

            "桥梁倒塌，主要街道全部无法通行。\x02\x01",

            "（※当时的元首巴尔蒙特大公\x01",
            "    此时已转移到邻国避难。）\x02\x01",

            "　\x01",
            "　\x01",
            "出现后２日――\x02\x01",

            "国土约一半化为盐海。\x02\x01",

            "居民大多数转移到受格雷布河所遮蔽的南部地域避难。\x02\x01",

            "　\x01",
            "　\x01",
            "出现后３日拂晓――\x02\x01",

            "『盐化』的进行终于停止。\x01",
            "星杯骑士开始为调查旧公都哈利亚斯科而前进。\x02",
        )
    )

    Jump("loc_6FFF")

    label("loc_6FFF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #151
        (
            "\x07\x00#2S同日下午，星杯骑士到达『盐之桩』――\x02\x01",

            "但其姿态已与发现当时截然迥异。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS330._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #152
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "在『盐化』现象的中心地发现的『桩』\x01",
            "总高度仅２．５亚矩有余――\x02\x01",

            "表面发现有像被某种东西划过的条状痕迹。\x02\x01",

            "　\x01",
            "　\x01",
            "（※以下为审问会注记）\x02\x01",

            "推测伴随『盐化』现象的进行，\x01",
            "『桩』本体的质量也会减少（※注记完毕）――\x02",
        )
    )

    Jump("loc_721B")

    label("loc_721B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #153
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "虽然失去了将大地化为盐的压倒性力量，\x01",
            "但『桩』本体至今仍然残留有『盐化』的能力――\x02\x01",

            "其中隐藏着严重的威胁，\x01",
            "就算仅仅是『直接』接触，\x01",
            "任何对象都会在片刻之间变成盐的结晶。\x02\x01",

            "　\x01",
            "　\x01",
            "其后星杯骑士使用本院转交的\x01",
            "圣器『克雷普尼尔』之力，以非接触的形式将其回收――\x02\x01",

            "自此至今日为止\x01",
            "『盐之桩』都被严密封印在本院深处。\x02",
        )
    )

    Jump("loc_73A3")

    label("loc_73A3")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #154
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "虽然回收顺利完成――\x01",
            "但『桩』在该国造成了巨大的损害。\x02\x01",

            "　\x01",
            "　\x01",
            "虽然对临近诸国无任何损害――\x01",
            "但从结果上来说，５个行政区有３个（包括旧公都）都遭到毁灭。\x02\x01",

            "包括外国来的旅行者等在内，\x01",
            "遇难者的数量在总人口的１／３以上。\x02\x01",

            "　\x01",
            "　\x01",
            "突如其来的灾祸\x01",
            "给人们带来了巨大的不安与恐慌――\x02\x01",

            "从信仰上的观点来看\x01",
            "由七耀教会进行事后处理已刻不容缓。\x02",
        )
    )

    Jump("loc_756B")

    label("loc_756B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #155
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "因此，审问会立即\x01",
            "决定派遣相关人员前往当地救援――\x02\x01",

            "致力于在当地重建礼拜堂\x01",
            "及治愈身心皆疲的国民。\x02\x01",

            "　\x01",
            "　\x01",
            "同时，失去容身之处，\x01",
            "成为孤儿的孩子们将被托付于福音设施，\x01",
            "其将来的各方各面都会得到悉心照料。\x02\x01",

            "（※此外，大片盐化的北部地域\x01",
            "　  在事件以后已置于教会的严格管理之下，\x01",
            "　  一般人等严禁入内。）\x02",
        )
    )

    Jump("loc_76E8")

    label("loc_76E8")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS352._CH")
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #156
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "附记――\x02\x01",

            "　\x01",
            "一段时间之后，该国前元首\x01",
            "巴尔蒙特原大公虽意图重建国政――\x02\x01",

            "　\x01",
            "　\x01",
            "但在紧急事态下\x01",
            "只顾自保的元首早已权威尽失――\x02\x01",

            "翌年民众群起武装反抗，\x01",
            "诺桑比亚大公国分崩离析。\x02\x01",

            "　\x01",
            "　\x01",
            "其后，通过选举\x01",
            "选出代表的民主议会成立，\x01",
            "至此，大公国重生为自治州。\x02",
        )
    )

    Jump("loc_78DE")

    label("loc_78DE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #157
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "同时，旧军部作为自警团\x01",
            "重新编制――\x02\x01",

            "　\x01",
            "　\x01",
            "然而在贫穷的自治州，\x01",
            "其中大半人都想尽快赚取外快――\x02\x01",

            "　\x01",
            "　\x01",
            "结果，被称为『北之猎兵』的\x01",
            "大规模佣兵部队诞生了。\x02",
        )
    )

    Jump("loc_79CE")

    label("loc_79CE")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_AE(0x96)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        (
            "\x07\x00#2S就这样，事件在『世俗面』迎来了结局――\x02\x01",

            "但还残留有数个包括教义性问题的重大谜团。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #159
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "到底『桩』是从何而来#150W…………#20W\x02\x01",

            "　\x01",
            "　\x01",
            "超过数百亚矩的巨大物体\x01",
            "出现在都市的近郊暂且不论，\x01",
            "关于其出现瞬间的情报还完全无法获得。\x02\x01",

            "　\x01",
            "　\x01",
            "虽然利用『空间转移』等类似现象\x01",
            "出现在旧公都近郊的想法是比较有说服力的，\x01",
            "但仍纯粹停留在类推的阶段上。\x02",
        )
    )

    Jump("loc_7BAD")

    label("loc_7BAD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #160
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "更为重大的是『桩』在教义上的立场所在。\x02\x01",

            "　\x01",
            "　\x01",
            "『盐之桩』与『古代遗物』是截然不同的存在，\x01",
            "是更本源性的『女神创造力的显现』（审问会答复）――\x02\x01",

            "虽然不得不如此考虑，但现状已超越了我们知识的界限。\x02\x01",

            "　\x01",
            "　\x01",
            "也有相反说法认为『桩』是『七至宝』之一，\x01",
            "但并未发现其与圣典或传承的相似之处。\x02",
        )
    )

    Jump("loc_7D20")

    label("loc_7D20")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #161
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "为了终有一天解决这些难题，\x01",
            "封圣省管内现在仍在继续对『桩』的研究――\x02\x01",

            "　\x01",
            "　\x01",
            "其中，甚至有将『桩』视为女神的恩恵，\x01",
            "认为其应当被用于教会使命的考量。\x02",
        )
    )

    Jump("loc_7DFD")

    label("loc_7DFD")

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS329._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #162
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "用高压水流加工『桩』的碎片而成的圣器――\x01",
            "是现在实践性最高的计划。\x02\x01",

            "　\x01",
            "　\x01",
            "装配使用以盐的结晶所制造的筒\x01",
            "便可避免直接接触而将『桩』投射向目标。\x02\x01",

            "　\x01",
            "　\x01",
            "#2S攻击对象如果是人类，\x01",
            "在数秒内就会全身结晶化至死――\x02\x01",

            "使用任何手段都无法复生。\x02",
        )
    )

    Jump("loc_7FCA")

    label("loc_7FCA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #163
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "在『桩』的实体尚未被解明的现状下\x01",
            "的确不应该轻率使用，\x01",
            "从人道上的观点来看也有问题被指出――\x02\x01",

            "　\x01",
            "　\x01",
            "但是，当存在确定应被抹消的对象的情况下\x01",
            "可以说这是极其有效的圣器。\x02",
        )
    )

    Jump("loc_80BA")

    label("loc_80BA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #164
        "\x07\x00#2S――研究预计今后仍将继续进行。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 4000, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_20(0xFA0)
    OP_21()
    OP_C7(0x1, 0x0, 0x0)
    Sleep(800)

    AnonymousTalk(    #165
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "有关本圣器的追记――\x02\x01",

            "　\x01",
            "＊＊年＊月，开始仅限非公开活动中本圣器的试用。\x02\x01",

            "＊＊年＊月，针对抹杀＊＊＊的行动，审问会下令使用。\x02\x01",

            "＊＊年＊月，在抹杀＊＊＊时使用（以弩枪投射）。\x02\x01",

            "　　　　　　结果极其良好，毫无对周边的损害……\x02\x01",

            "　　　　　　将对象＊＊＊完全抹消成功。\x02",
        )
    )

    Jump("loc_8271")

    label("loc_8271")

    CloseMessageWindow()
    Sleep(1000)
    OP_56(0x0)
    OP_59()

    AnonymousTalk(    #166
        (
            "\x07\x00#2S　　　　　　　　　　　　　　　　　　　\x01",
            "※注记：关于抹消者＊＊＊\x02\x01",

            "　\x01",
            "＊＊＊是『盐之桩』事件的受灾孤儿。\x02\x01",

            "以下略历――\x02\x01",

            "　\x01",
            "Ｓ１１８０年　皈依七耀教会。\x02\x01",

            "Ｓ１１８５年　进入封圣省。就任圣务官。\x02\x01",

            "Ｓ１１９０年　升迁为司教。\x02\x01",

            "Ｓ１１９５年　被认定为异端。逐出教会。\x02",
        )
    )

    Jump("loc_83B3")

    label("loc_83B3")

    CloseMessageWindow()
    Sleep(2000)
    OP_56(0x0)
    OP_59()
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #167
        "\x07\x00Episode『盐之桩』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x13, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8497")
    Sleep(1000)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x4, 0x20)
    OP_3E(0x27F, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #168
        "\x07\x00得到了\x1F\x7F\x02\x07\x00。\x02",
    )

    Jump("loc_8460")

    label("loc_8460")

    CloseMessageWindow()
    AddMira(3500)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #169
        "\x07\x00得到了\x07\x02３５００米拉\x07\x00。\x02",
    )

    Jump("loc_848B")

    label("loc_848B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_8497")

    OP_A2(0x2506)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_84AD")
    NewScene("ED6_DT21/U4134   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_84B6")

    label("loc_84AD")

    NewScene("ED6_DT21/U4131   ._SN", 112, 0, 0)
    IdleLoop()

    label("loc_84B6")

    Return()

    # Function_15_64EE end

    def Function_16_84B7(): pass

    label("Function_16_84B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS332._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_1D(0x6E)
    Sleep(2000)
    OP_C6(0x0, 0x3, -1, 4000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(4000)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #170
        (
            "\x07\x00#2S#80W『怪盗Ｂ』调查报告――\x02\x01",

            "关于其犯罪历史以及经历的考察。#20W\x02\x01",

            "　　　　　　　　#80W《帝国时报社》调查小组编#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS333._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #171
        (
            "\x07\x00正如我们所收集的大量资料显示――\x01",
            "『怪盗Ｂ』在帝国的活跃表现极其华丽。\x02\x01",

            "　\x01",
            "以帝国美术馆收藏的几幅画为首――\x02\x01",

            "到税关仓库的七耀石结晶、\x02\x01",

            "帝国军研究设施的新型战车……\x02\x01",

            "他盯上的东西没有一样幸免于难。\x02\x01",

            "（最后甚至化身青年将校潜入舞会，\x01",
            "  跟某个侯爵夫人私奔了。）\x02",
        )
    )

    Jump("loc_87EC")

    label("loc_87EC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #172
        (
            "\x07\x00但话虽如此，他似乎却并不以此牟利。\x01",
            "（这也是最不可理解的地方）\x02\x01",

            "　\x01",
            "因为大部分情况下，他所拿到的物品\x01",
            "都会被丢弃在失主看见会晕倒的\x01",
            "极其诡异的地方――\x02\x01",

            "　\x01",
            "换成米拉在贫民街某处\x01",
            "下场金币雨，也是常用的套路。\x02",
        )
    )

    Jump("loc_88DD")

    label("loc_88DD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #173
        (
            "\x07\x00但是，可别搞错了――\x02\x01",

            "怪盗Ｂ决不是单纯的侠盗。\x02\x01",

            "　\x01",
            "最好的例子就是刚才说的侯爵夫人。\x02\x01",

            "私奔至今约过了半年多――\x01",
            "其行踪依然不明。\x02\x01",

            "　\x01",
            "――像这种他盯上的猎物\x01",
            "从来没回来的例子也时常发生。\x02",
        )
    )

    Jump("loc_89C8")

    label("loc_89C8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #174
        (
            "\x07\x00有如神助的偷盗技术\x01",
            "以及对赃物所显示出的毫无常理的态度――\x02\x01",

            "　\x01",
            "乍一看好像是心血来潮的犯罪，\x01",
            "但观察怪盗Ｂ的目标物品\x01",
            "却发现一个共同的思想。\x02",
        )
    )

    Jump("loc_8A70")

    label("loc_8A70")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #175
        (
            "\x07\x00例如从美术馆盗走的画\x01",
            "虽然全都是出于名匠之手的杰作――\x02\x01",

            "――但对贵族阶级爱好者来说太难懂而评价不好，\x01",
            "都是失去展示机会不受欢迎的作品。\x02\x01",

            "　\x01",
            "同样，仓库的七耀石被税关没收以后，\x01",
            "一直保管在不见天日的地方――\x02\x01",

            "　\x01",
            "帝国军的新型战车，也是以高性能为傲\x01",
            "却停止开发而被尘封的东西。\x02\x01",

            "（顺带一提那个侯爵夫人也是类似的状态。\x02\x01",

            "　她丈夫侯爵只为小妾着迷，\x01",
            "　对妻子则完全置之不理。）\x02",
        )
    )

    Jump("loc_8C31")

    label("loc_8C31")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #176
        (
            "\x07\x00找出世上被遗弃的『美』，\x01",
            "将其从愚蠢的物主手中救出――\x02\x01",

            "怪盗Ｂ的脑中毫无疑问存在这种理念。\x02\x01",

            "　\x01",
            "『美的解放』――\x02\x01",

            "装饰在他的预告卡片上的话语，正是其佐证。\x02\x01",

            "　\x01",
            "――不为金钱而为理念犯罪的怪盗。\x02\x01",

            "恐怕在面具下隐藏的他的真面目\x01",
            "就潜藏在这种独特的美学之中吧。\x02",
        )
    )

    Jump("loc_8D66")

    label("loc_8D66")

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS334._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #177
        (
            "\x07\x00关于怪盗Ｂ的真面目\x01",
            "虽然已有数种说法――\x02\x01",

            "　\x01",
            "但遗憾的是仅仅是数量众多，\x01",
            "实际上却没有任何一种有决定性证据。\x02\x01",

            "（甚至最近，还有声称「自己就是怪盗Ｂ」，\x01",
            "  故意送上门来的疯狂假货出现。）\x02\x01",

            "　\x01",
            "话虽如此，\x01",
            "却也并不是说这些传言全都毫无根据。\x02\x01",

            "在此介绍最近坊间\x01",
            "流传甚广的三种说法吧。\x02",
        )
    )

    Jump("loc_8F2F")

    label("loc_8F2F")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #178
        "\x07\x00《案例１：『多情的欺诈师Ｘ』》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #179
        (
            "\x07\x00经历――\x02\x01",

            "　\x01",
            "『Ｘ』不断伪造身份，\x01",
            "频频与贵族阶级小姐们发生风流韵事，\x01",
            "是个绝代的欺诈师。\x02\x01",

            "他容颜秀丽，\x01",
            "是个相当高傲的人物。\x02\x01",

            "　\x01",
            "生于温暖南方贫穷家庭的Ｘ\x01",
            "为了赚取零花钱，\x01",
            "从小就养成了偷盗的恶习。\x02\x01",

            "（证言来源于当时的同伴，\x01",
            "　据说Ｘ一次也没因「偷盗」\x01",
            "　而被逮捕过。）\x02",
        )
    )

    Jump("loc_90B6")

    label("loc_90B6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #180
        (
            "\x07\x00――Ｘ成为欺诈师的契机，\x01",
            "是一次与身份悬殊的\x01",
            "美丽小姐『坠入爱河』。\x02\x01",

            "当时在Ｘ的国家，贵族处于绝对的统治地位，\x01",
            "身份悬殊的恋爱不可能有结果――\x02\x01",

            "因此他就开始伪造身份。\x02\x01",

            "　\x01",
            "一度伪造过身份的Ｘ，\x01",
            "也开始尝试其它各种禁断之恋。\x02\x01",

            "在１０年前因伪造经历嫌疑被捕，\x01",
            "其后奇迹般地成功逃狱，\x01",
            "至今行踪不明。\x02",
        )
    )

    Jump("loc_9207")

    label("loc_9207")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #181
        (
            "\x07\x00考察――\x02\x01",

            "　\x01",
            "无可比拟的偷盗技术，\x02\x01",

            "加上与贵族小姐的禁断之恋――\x02\x01",

            "这些都感觉像是怪盗Ｂ的关键词。\x02\x01",

            "　\x01",
            "而值得一提的是，Ｘ对她们家里的\x01",
            "财产完全没有兴趣这点。\x02\x01",

            "Ｘ与她们交往，\x01",
            "并没有任何金钱利益。\x02\x01",

            "　\x01",
            "――由于身份这等身外之物\x01",
            "而无法谱出恋曲令『Ｘ』感到忧虑。\x02\x01",

            "而他的想法，似乎与怪盗Ｂ所倡导的\x01",
            "美的标准有何种相似之处。\x02",
        )
    )

    Jump("loc_9399")

    label("loc_9399")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #182
        "\x07\x00《案例２：『悲剧的画家Ｙ』》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #183
        (
            "\x07\x00经历――\x02\x01",

            "　\x01",
            "『Ｙ』是个富于悲剧色彩的画家。\x02\x01",

            "出生于北方中流家庭的Ｙ，\x01",
            "在某个有势力的贵族支持下成为画家，\x01",
            "留下众多传世名作。\x02\x01",

            "（――稍后也得知，这段时间\x01",
            "　Ｙ也向世间输送了众多『赝品』。\x02\x01",

            "　当时，那贵族让Ｙ描画赝品\x01",
            "　以此牟取非法利益。）\x02\x01",

            "　\x01",
            "然而，某时Ｙ突然离开了那个贵族。\x02\x01",

            "（详细的理由至今未明。）\x02\x01",

            "――然后，悲剧开始了。\x02",
        )
    )

    Jump("loc_956B")

    label("loc_956B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #184
        (
            "\x07\x00突如其来的讣告――\x02\x01",

            "Ｙ刚刚离开贵族，\x01",
            "他的恋人，一位良家女孩\x01",
            "就因交通事故而一命呜呼。\x02\x01",

            "（虽然没有证据，\x01",
            "　但传闻这位女孩的死\x01",
            "　或许和贵族有所关联。）\x02\x01",

            "　\x01",
            "最后被人目击到在恋人沉眠的墓地出现之后，\x01",
            "Ｙ就断绝了消息，此后\x01",
            "作为悲剧的画家为人所传诵。\x02\x01",

            "而数年后，\x01",
            "贵族惨遭不明人士杀害，\x01",
            "使这个事件迎来了终结。\x02",
        )
    )

    Jump("loc_96C8")

    label("loc_96C8")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #185
        (
            "\x07\x00考察――\x02\x01",

            "　\x01",
            "围绕Ｙ的事件至今迷雾重重，\x01",
            "在各种推测流传之下，\x01",
            "成为怪盗的真面目说之一浮上水面。\x02\x01",

            "　\x01",
            "此外，这个案例还有一个具体的关联。\x02\x01",

            "那就是，怪盗Ｂ时常将赝品作为『虚伪的美』\x01",
            "从这个世上埋葬这一事实。\x02\x01",

            "也就是说，\x01",
            "这种行为被认为是――\x01",
            "「Ｙ亲手消灭自己的赝品」的行为。\x02\x01",

            "（同时，实际追寻怪盗Ｂ所埋葬的画作线索时，\x02\x01",

            "　发现确实是『Ｙ』的赝品。）\x02",
        )
    )

    Jump("loc_986D")

    label("loc_986D")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #186
        "\x07\x00《案例３：『华丽的武术家Ｚ』》\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #187
        (
            "\x07\x00经历――\x02\x01",

            "　\x01",
            "最后介绍的『Ｚ』\x01",
            "与之前稍微有点不同――\x01",
            "可称得上是『奇谈』。\x02\x01",

            "　\x01",
            "Ｚ是生于遥远的东方之地\x01",
            "历史悠久的武家名门的男子。\x02\x01",

            "容貌端丽体格健壮，\x01",
            "同时又拥有禀异天赋，\x01",
            "是英名垂手可得的绝代武术家。\x02\x01",

            "另传言他头脑清晰，\x01",
            "略带自我陶醉的气质。\x02",
        )
    )

    Jump("loc_99DB")

    label("loc_99DB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #188
        (
            "\x07\x00家世、才能、容貌――\x02\x01",

            "拥有这一切的Ｚ\x01",
            "开始对世间感到无聊。\x02\x01",

            "（而且，似乎还常以这种思想\x01",
            "　向别人发牢骚。）\x02\x01",

            "　\x01",
            "然后某时，他没有告诉任何人，\x01",
            "也没留下任何书信就忽然消失了踪影。\x02",
        )
    )

    Jump("loc_9AB3")

    label("loc_9AB3")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #189
        (
            "\x07\x00考察――\x02\x01",

            "　\x01",
            "人们认为这是天才的奇怪行动。\x02\x01",

            "此外，有证言说Ｚ所使用的技术动作\x01",
            "和怪盗Ｂ所使用的诡异奇术\x01",
            "有一致之处――\x02\x01",

            "但在可靠性上\x01",
            "与其它众多轶闻无太大区别。\x02\x01",

            "　\x01",
            "然而，那面具下隐藏着东方系的人物\x01",
            "这种想法本身非常有趣，\x01",
            "引人遐思。\x02",
        )
    )

    Jump("loc_9BDC")

    label("loc_9BDC")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_20(0xBB8)
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #190
        (
            "\x07\x00以上是三种方向各异的说法。\x02\x01",

            "　\x01",
            "Ｘ、Ｙ或是Ｚ，其中有一个会是Ｂ吗――\x02\x01",

            "还是说有完全不同的Ａ这个人物存在――\x02\x01",

            "　\x01",
            "除了询问怪盗Ｂ本人\x01",
            "别无确认的手段了吧――\x02\x01",

            "　\x01",
            "只不过前提是，他口中说出的『真相』\x01",
            "真的能作为真相为人所接受。\x02",
        )
    )

    Jump("loc_9D10")

    label("loc_9D10")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        (
            "\x07\x00追记――\x02\x01",

            "　\x01",
            "当这篇报道问世之后，\x01",
            "一枚怪盗Ｂ发来的卡片送到了本社。\x02\x01",

            "以下是其内容――\x02\x01",

            "　\x07\x0C\x01",
            "「诸位已经得知我的真面目――\x01",
            "　我的『数字』将指示『真相』。」\x02\x01",

            "　\x07\x00\x01",
            "根据这文字，我们已经\x01",
            "掌握了怪盗Ｂ的真面目――\x02\x01",

            "但遗憾的是，从目前\x01",
            "本杂志所持的情报看来还无法判断。\x02",
        )
    )

    Jump("loc_9E60")

    label("loc_9E60")

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #192
        (
            "\x07\x00――究竟是否有人\x01",
            "能找出这个问题的答案呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #193
        "\x07\x00Episode『『怪盗Ｂ』调查报告』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x14, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F92")
    Sleep(1000)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x4, 0x20)
    OP_3E(0x12E, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #194
        "\x07\x00得到了\x1F\x2E\x01\x07\x00。\x02",
    )

    Jump("loc_9F59")

    label("loc_9F59")

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #195
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_9F86")

    label("loc_9F86")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_9F92")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M5610   ._SN", 130, 0, 0)
    IdleLoop()
    Return()

    # Function_16_84B7 end

    def Function_17_9F9F(): pass

    label("Function_17_9F9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    Sleep(1000)
    OP_1D(0x21)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS336._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #196
        (
            "\x07\x00导力器（Orbment）――\x02\x01",

            "　\x01",
            "利用七耀石所带有的『导力』\x01",
            "引起各种现象的装置――\x02\x01",

            "　\x01",
            "它被发明以来仅过了半个多世纪，\x01",
            "却名副其实地改变了世界。\x02",
        )
    )

    Jump("loc_A113")

    label("loc_A113")

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #197
        (
            "\x07\x00从供暖、照明等日用功能，\x01",
            "到支撑国防的战车和大炮等兵器――\x02\x01",

            "　\x01",
            "当今社会，导力器已不可或缺。\x02\x01",

            "　\x01",
            "肩担其普及和发展大任的――\x02\x01",

            "就是我们『爱普斯泰恩财团』。\x02",
        )
    )

    Jump("loc_A1D7")

    label("loc_A1D7")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #198
        (
            "\x07\x00本财团设立于Ｓ１１５５年――\x02\x01",

            "　\x01",
            "继承前年去世的爱普斯泰恩博士的遗志，\x01",
            "由其数名优秀的弟子所成立。\x02\x01",

            "　\x01",
            "本部设在博士的故乡列曼自治州，\x01",
            "目前也以此处为据点持续活动。\x02",
        )
    )

    Jump("loc_A2BD")

    label("loc_A2BD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #199
        (
            "\x07\x00设立当初本财团规模很小，\x01",
            "虽然在各地进行导力器普及活动\x01",
            "其反应却并不乐观。\x02\x01",

            "　\x01",
            "为了打破这种局面，\x01",
            "出现了意求以自己的力量为导力技术播种\x01",
            "而离开列曼自治州的研究者们。\x02",
        )
    )

    Jump("loc_A37E")

    label("loc_A37E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #200
        (
            "\x07\x00其中之一是Ｇ·施密特博士――\x02\x01",

            "作为机械工学的权威,\x01",
            "鼎鼎大名的博士，访问各国企业\x01",
            "游说导力器的益处。\x02\x01",

            "　\x01",
            "其次是Ｌ·汉密顿博士――\x02\x01",

            "博士看到了技术上的差距，从一开始\x01",
            "就认为『边境更需要导力器』――\x02\x01",

            "与本已交情深厚的\x01",
            "游击士协会一同，\x01",
            "组成了以振兴偏远地区技术为目的的派遣团。\x02\x01",

            "其自身也在各地域往来巡察，\x01",
            "打下了普及、启蒙活动的基础。\x02",
        )
    )

    Jump("loc_A4FA")

    label("loc_A4FA")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #201
        (
            "\x07\x00而最后是现在\x01",
            "被称为『导力革命之父』的\x01",
            "Ａ·拉赛尔博士――\x02\x01",

            "　\x01",
            "博士回到故乡，\x01",
            "为提高祖国利贝尔的技术而竭尽全力――\x02\x01",

            "归国后仅１年\x01",
            "就设立了蔡斯技术工房（※后来的中央工房），\x01",
            "首次在列曼自治州以外成功制造出导力器。\x02\x01",

            "　\x01",
            "更在三年后，\x01",
            "受到来访视察工房的当时的利贝尔国王\x01",
            "埃德佳Ⅲ世巨额的资金援助――\x02\x01",

            "利贝尔王国瞬间被导力器所渗透，\x01",
            "展示出他国艳羡不已的繁荣。\x02",
        )
    )

    Jump("loc_A682")

    label("loc_A682")

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #202
        (
            "\x07\x00在王国的成功，\x01",
            "使得原本对导力器印象不佳的\x01",
            "人们完全改变了认识――\x02\x01",

            "　\x01",
            "此后，各国要求本财团\x01",
            "提供技术的呼声不断，\x01",
            "财团的经济基础也日益稳固。\x02\x01",

            "　\x01",
            "广泛的呼吁和坚定确实的研究活动――\x02\x01",

            "正因为先导们的努力，\x01",
            "才促成了日后被称为『导力革命』的\x01",
            "导力器急速普及运动。\x02",
        )
    )

    Jump("loc_A7A4")

    label("loc_A7A4")

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS337._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(3500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #203
        (
            "\x07\x00本财团的活动有以下３大支柱――\x02\x01",

            "　\x01",
            "　１．导力器的基础性研究\x02\x01",

            "　２．导力器的普及与启蒙活动\x02\x01",

            "　３．通过技术对世界和平的寄望\x02\x01",

            "　\x01",
            "　　以下将对各种活动进行介绍。\x02",
        )
    )

    Jump("loc_A8FA")

    label("loc_A8FA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #204
        (
            "\x07\x00【１．导力器的基础性研究】\x02\x01",

            "　\x01",
            "本财团最为重要的使命，\x01",
            "当然是导力器的改良与进一步的发展。\x02\x01",

            "　\x01",
            "虽然导力器的运作原理是不变的，\x01",
            "但被称为『基本体系』的内部构造\x01",
            "迄今为止进行过多次的大幅改良。\x02\x01",

            "　\x01",
            "所谓基本体系，是指由齿轮和螺丝这种\x01",
            "机械部件所组成的结构，\x01",
            "随着工学与技术的进步还有很大的改良余地。\x02",
        )
    )

    Jump("loc_AA4C")

    label("loc_AA4C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #205
        (
            "\x07\x00这种基础研究虽然能获得重大成果，\x01",
            "但另一方面研究所需的时间之长也可想而知，\x01",
            "因此重视收益性的企业有敬而远之的倾向。\x02\x01",

            "　\x01",
            "本财团率先推进此领域中的研究\x01",
            "从公益性的观点来看可说是极其重要的。\x02",
        )
    )

    Jump("loc_AB22")

    label("loc_AB22")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #206
        (
            "\x07\x00【２．导力器的普及与启蒙活动】\x02\x01",

            "　\x01",
            "导力器的普及以及在世上传播其正确使用方法\x01",
            "也是本财团的重要使命。\x02\x01",

            "　\x01",
            "虽然在先进国家已成为日常的工具，\x01",
            "但在边境和山岳地带等尚未都市化的地域\x01",
            "导力器至今仍未得到充分普及。\x02\x01",

            "　\x01",
            "本财团为了提高这些地区的生活水平\x01",
            "几度组成了包括游击士和技术人员的\x01",
            "地域派遣团，不断前往进行技术支援。\x02\x01",

            "　\x01",
            "此外也协助七耀教会的运动，\x01",
            "通过在主日学校教程中加入『导力』科目等方式，\x01",
            "着力于技术性的知识渗透。\x02",
        )
    )

    Jump("loc_ACF4")

    label("loc_ACF4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #207
        (
            "\x07\x00【３．通过技术对世界和平的寄望】\x02\x01",

            "　\x01",
            "对世界和平的寄望――\x02\x01",

            "为了这个崇高的使命，本财团从设立之初开始\x01",
            "就与游击士协会保持着密切的关系。\x02\x01",

            "　\x01",
            "该协会作为国际性治安维持组织而设立，\x01",
            "是进行从中立的立场调停国际纷争等活动，\x01",
            "维持今日世界稳定不可或缺的组织。\x02\x01",

            "　\x01",
            "本财团除提供资金援助以外，\x01",
            "也作为世界上唯一的战术导力器产地\x01",
            "在装备方面支援着该协会。\x02",
        )
    )

    Jump("loc_AE7A")

    label("loc_AE7A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #208
        (
            "\x07\x00在其过程中所获得的实战经验，\x01",
            "毫无疑问也在战术导力器的改良方面\x01",
            "发挥了重大的作用。\x02\x01",

            "　\x01",
            "无论是怎样的机械，\x01",
            "在其最终成形的背后\x01",
            "都隐藏着漫长艰苦的历程。\x02",
        )
    )

    Jump("loc_AF2D")

    label("loc_AF2D")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #209
        (
            "\x07\x00Ｓ１１９０年――\x02\x01",

            "　\x01",
            "面向导力文明的未来，\x01",
            "本财团与蔡斯中央工房共同\x01",
            "发表了『导力网络』的构想。\x02\x01",

            "　\x01",
            "这个将大陆全土都以导力通信的网络\x01",
            "连成一体的宏大计划，\x01",
            "寄托了我们的希望。\x02\x01",

            "　\x01",
            "――那就是对通过对话来实现和平的探索。\x02",
        )
    )

    Jump("loc_B056")

    label("loc_B056")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #210
        (
            "\x07\x00近年来，导力器与『和平』的关系\x01",
            "变得前所未有的复杂。\x02\x01",

            "　\x01",
            "『能够实现无限\x01",
            "　能量循环的导力器\x01",
            "　才能为世界带来恒久的安定』――\x02\x01",

            "仿佛故意违背爱普斯泰恩博士的话语一般，\x01",
            "导力革命之后世界走上了迷茫的道路。\x02\x01",

            "　\x01",
            "在埃雷波尼亚帝国与利贝尔王国的纷争中，\x01",
            "飞艇首次作为导力兵器投入使用。\x02\x01",

            "　\x01",
            "兵器导力化的潮流今后也将继续推进，\x01",
            "使得战争的结果更为悲剧化。\x02",
        )
    )

    Jump("loc_B1DF")

    label("loc_B1DF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #211
        (
            "\x07\x00在这种现实面前，\x01",
            "如何才能构筑和平的世界――\x02\x01",

            "　\x01",
            "导力通信将开拓的未来――\x02\x01",

            "超越国境和人种将人们融为一体的力量，\x01",
            "或许才是解决这问题的关键。\x02\x01",

            "　\x01",
            "超越国家的界限让人们相互交流，加深理解，\x01",
            "共同构筑没有纷争的世界――\x02",
        )
    )

    Jump("loc_B2DF")

    label("loc_B2DF")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #212
        (
            "\x07\x00――对未来理想世界的挑战\x01",
            "现在才刚刚开始。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_59()
    OP_20(0x7D0)
    OP_21()
    OP_C7(0x1, 0xFF, 0x0)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #213
        "\x07\x00Episode『爱普斯泰恩财团』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x15, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B424")
    Sleep(1000)
    OP_28(0x15, 0x4, 0x10)
    OP_28(0x15, 0x4, 0x20)
    OP_3E(0x2EC, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #214
        "\x07\x00得到了\x1F\xEC\x02\x07\x00。\x02",
    )

    Jump("loc_B3ED")

    label("loc_B3ED")

    CloseMessageWindow()
    AddMira(7000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #215
        "\x07\x00得到了\x07\x02７０００米拉\x07\x00。\x02",
    )

    Jump("loc_B418")

    label("loc_B418")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_B424")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_9F9F end

    def Function_18_B431(): pass

    label("Function_18_B431")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    OP_1D(0x38)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS340._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #216
        (
            "\x07\x00　　　　　　　　　　　　　　　　　　　\x01",
            "　\x01",
            "　\x01",
            "#80W《关于帝国游击士协会支部袭击事件的报告》\x02\x01",

            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　\x01",
            "　#20W\x01",
            "Ｓ１２０２年，发生了埃雷波尼亚帝国各地\x01",
            "协会支部相继受到袭击的事件。\x02\x01",

            "　\x01",
            "武装集团实体不明――\x02\x01",

            "帝国内的协会相关人员陷入了混乱。\x02",
        )
    )

    Jump("loc_B618")

    label("loc_B618")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #217
        (
            "\x07\x00　　　　　　　　　　　　　　　　　　　\x01",
            "很快数量众多的导力通信在帝都空中交错――\x02\x01",

            "　　　　　　　　　　使得事态严峻程度急速加剧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0xC3, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #218
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『昨日凌晨，游击士协会帝都支部\x01",
            "　受到高性能炸药攻击而完全破坏――\x02\x01",

            "　根据第二科的分析，\x01",
            "　爆炸物是通过下水道\x01",
            "　设置在该设施正下方的可能性很高。』\x02\x01",

            "『从实行方法、使用的炸药种类看来\x01",
            "　推测为专门组织的作战。\x02\x01",

            "　当前正在咨询对外情报负责人，\x01",
            "　确认国内危险人物的位置――』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #219
        (
            "\x07\x0C《发自：帝国军情报局第三科　寄往：第一科》\x02\x01",

            "『非法入境的嫌疑人中\x01",
            "　发现有人与『猎兵团』有关。\x02\x01",

            "　已查明是『杰斯塔猎兵团』兵站负责人。\x02\x01",

            "　潜伏于国内的该猎兵团动静已受到侦察――』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 20, -1, -1)

    AnonymousTalk(    #220
        (
            "\x07\x04《帝国游击士协会：致利贝尔王国王都支部。》\x02\x01",

            "『本日临晨，帝都支部受到了袭击。\x02\x01",

            "　支部负责人至今联络不上。\x02\x01",

            "　请求高等级游击士的支援。\x01",
            "　至急、至急、至急――』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 240, -1, -1)

    AnonymousTalk(    #221
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『帝国游击士协会发出\x01",
            "　致利贝尔王国王都支部的通信。\x02\x01",

            "　由通信文章内容看来，\x01",
            "　近日预计将会有高等级游击士入境。\x02\x01",

            "　请求相关机关对其进行追踪、监视。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS341._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #222
        (
            "\x07\x00事件发生２日后――\x02\x01",

            "卡西乌斯·布莱特（Ｓ级）到达帝都，\x02\x01",

            "就任该国游击士协会临时代表。\x02\x01",

            "　\x01",
            "临时代表确认了支部的受损状況，\x01",
            "发出指示让分散的游击士到边境集中。\x02\x01",

            "　\x01",
            "同时为防备敌方势力的谍报活动\x01",
            "将导力通信完全封锁。\x02",
        )
    )

    Jump("loc_BC6B")

    label("loc_BC6B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #223
        (
            "\x07\x00已经有６个都市的支部遭受袭击，\x01",
            "帝国内的协会逐渐失去作用。\x02\x01",

            "　\x01",
            "目前还存在的支部\x01",
            "申请了来自帝国军的严密警备――\x02\x01",

            "　\x01",
            "然而，帝国军反应迟钝，\x01",
            "明显无法得到预期的效果。\x02",
        )
    )

    Jump("loc_BD35")

    label("loc_BD35")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #224
        (
            "\x07\x00另一方面临时代表根据敌方势力的动向\x01",
            "推测出了他们的补给据点――\x02\x01",

            "　\x01",
            "选拔出熟悉当地情况的游击士们，\x01",
            "前往其潜伏地点搜索。\x02\x01",

            "　\x01",
            "这是出于在出入境管理严格的帝国进行作战\x01",
            "必定会先设立国内补给据点的判断。\x02\x01",

            "　\x01",
            "『肉斩骨断』作战\x01",
            "取得了立竿见影的成果。\x02",
        )
    )

    Jump("loc_BE54")

    label("loc_BE54")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #225
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『确认增援游击士为卡西乌斯·布莱特。\x02\x01",

            "　卡西乌斯·布莱特（Ｓ级游击士）――\x02\x01",

            "　在本科人物档案的评定中位列仅次于最高级的『ＬＶ４』。\x02\x01",

            "　之前的百日战役中，\x01",
            "　以飞行警备艇\x01",
            "　指挥反攻作战而闻名的人物。\x02\x01",

            "　视情况可能成为安全保障上的障碍――\x02\x01",

            "　现在正在详细追查其动向。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #226
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『对目标Ｃ·Ｂ的跟踪失败。\x02\x01",

            "　至今下落不明……\x02\x01",

            "　但是，按本部指示\x01",
            "　未停止警戒态势，\x01",
            "  继续维持现阶段状况。』\x02\x01",

            "『多名游击士在沿铁路移动中。\x02\x01",

            "　推测是某种作战行动。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #227
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『６名游击士急袭猎兵团据点。\x02\x01",

            "　拘捕内部的武装集团成员。\x02\x01",

            "　根据本科要员的对照\x01",
            "　确定为「杰斯塔猎兵团」成员。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS342._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #228
        (
            "\x07\x00由于据点被揭发，\x01",
            "确定实行犯是『杰斯塔猎兵团』。\x02\x01",

            "　\x01",
            "然而，敌方集团行动变得消极化，\x01",
            "此后演化成相互静观其变的状况。\x02",
        )
    )

    Jump("loc_C2D9")

    label("loc_C2D9")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #229
        (
            "\x07\x00胶着状态持续了两个月左右――\x02\x01",

            "　\x01",
            "临时代表利用这段时间\x01",
            "与帝国军情报部进行接触――\x02\x01",

            "　\x01",
            "――着手进行后来解决事件的\x01",
            "作战准备。\x02",
        )
    )

    Jump("loc_C37C")

    label("loc_C37C")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #230
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『对象Ｃ·Ｂ与本科要员接触。\x02\x01",

            "　现在确认中――』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(20, 240, -1, -1)

    AnonymousTalk(    #231
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『对象Ｃ·Ｂ提出共同作战。\x02\x01",

            "　预定在指定日期再度接触――』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS343._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(2500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x12, 0x0, 0x64)
    OP_C6(0x0, 0x3, -7829368, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #232
        (
            "\x07\x00～游击士协会支部袭击事件的战术性分析～\x02\x01",

            "　　　　　　　　　　　　　　　情报局第二科\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #233
        (
            "\x07\x00　\x01",
            "――打破胶着战局的，\x01",
            "是临时代表Ｃ·Ｂ的巧妙诱导。\x02\x01",

            "　\x01",
            "接触本科要员的Ｃ·Ｂ――\x01",
            "预测敌方势力会进行监听\x01",
            "而向参谋部发来了联络。\x02\x01",

            "　\x01",
            "监听了联络内容的敌方势力\x01",
            "得知下次接触的时间和地点，\x01",
            "计划将Ｃ·Ｂ抹杀――\x02\x01",

            "　\x01",
            "――然而这正是他的目的。\x02",
        )
    )

    Jump("loc_C6C8")

    label("loc_C6C8")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #234
        (
            "\x07\x00与Ｃ·Ｂ接触的本科要员\x01",
            "也收到了经过暗号化的文章――\x02\x01",

            "　\x01",
            "其中周密计划了\x01",
            "以帝国军部队歼灭\x01",
            "受伪装情报诱导的敌方集团的作战。\x02\x01",

            "　\x01",
            "参谋部认可了这个作战计划。\x02\x01",

            "而同游击士协会共同作战的结果――\x02",
        )
    )

    Jump("loc_C7B0")

    label("loc_C7B0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #235
        (
            "\x07\x00就是完全包围了为抹杀Ｃ·Ｂ而集结的\x01",
            "敌方集团――并成功解除其武装。\x02\x01",

            "　\x01",
            "潜伏于其它据点的残存势力，\x01",
            "也在俘虏的协助下各个击破――\x02\x01",

            "　\x01",
            "　\x01",
            "――从事件发生以来经过数月，\x01",
            "『杰斯塔猎兵团』就此解体。\x02",
        )
    )

    Jump("loc_C898")

    label("loc_C898")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0x12, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_20(0x9C4)
    OP_21()
    Sleep(1000)
    SetMessageWindowPos(20, 20, -1, -1)

    AnonymousTalk(    #236
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『卡西乌斯·布莱特（Ｓ级游击士）的\x01",
            "　威胁度评定于本日有所变更――』\x02\x01",

            "『――从『ＬＶ４』类\x01",
            "　更改为最大评定『ＬＶ５』类。\x02\x01",

            "　国家安全保障上的重大威胁――\x02\x01",

            "　入境时需要彻底监视。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(420, 240, -1, -1)

    AnonymousTalk(    #237
        (
            "\x07\x0C《发自：帝国军情报局第一科　寄往：参谋本部》\x02\x01",

            "『本日，确认监视对象出境。\x02\x01",

            "　出境时无任何混乱――\x02\x01",

            "　以后的任务移交至在外机关。\x02\x01",

            "　　　　　――以上，通信完毕。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #238
        (
            "\x07\x05《发自：参谋本部特别调查室　寄往：帝国政府宰相阁下》\x02\x01",

            "『……同样确认Ｃ·Ｂ出境。\x02\x01",

            "  虽有继续追踪，但此时\x01",
            "　尚未出现任何可疑动向。』\x02\x01",

            "『同时，与『演奏家』的接触尚未确认。\x02\x01",

            "　今后两者的动向都将继续详细调查。』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(2000)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #239
        "\x07\x00Episode『帝国游击士协会连续袭击事件』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x16, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC9E")
    Sleep(1000)
    OP_28(0x16, 0x4, 0x10)
    OP_28(0x16, 0x4, 0x20)
    OP_3E(0x61E, 1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #240
        "\x07\x00得到了\x1F\x1E\x06\x07\x00。\x02",
    )

    Jump("loc_CC65")

    label("loc_CC65")

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #241
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_CC92")

    label("loc_CC92")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_CC9E")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5404   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_B431 end

    def Function_19_CCAB(): pass

    label("Function_19_CCAB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(2000)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #242
        "\x07\x05读取中#200W　＞　＞　＞　＞　＞　#20W结束\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0x3D)
    Sleep(1500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS344._CH")
    OP_C5(0x1, 0x0, 0x0, 0x14, 0x19, 0x267, 0x1C2, 0x100, 0x100, 0x0, 0x0, 0x28, 0x32, 0xFFFFFF, 0x0, "C_VIS349._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #243
        (
            "\x07\x00『十三工房』——\x02\x01",

            "极限级战略人形兵器开发计划\x02\x03",

            "代号：『帕蒂尔·玛蒂尔』\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "开发计划概要\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #244
        (
            "\x07\x00开发目标——\x02\x01",

            "沿袭极限级系列的设计理念，\x01",
            "完成搭载更高级控制系统的新型机器。\x02\x03",

            "除过往型号所重视的战略性运用以外，\x01",
            "让精密灵活的战术性运用成为可能\x01",
            "也是本计划核定的目标。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        210,
        280,
        0,
        "作战行动半径\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #245
        (
            "\x07\x00以整个大陆区域为作战范围。\x02\x03",

            "为应对出现无补给的数年持续作战，\x01",
            "而装备主副两个系统的高功率导力引擎。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        3,
        340,
        280,
        0,
        "自动战斗能力\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #246
        (
            "\x07\x00通过装载集成化导力计算机『战神』，\x01",
            "让高级的目标评定及自动战斗能力成为可能——\x02\x03",

            "更在这种控制中\x01",
            "活用操纵者的神经系统，\x01",
            "以实现反射性和本能性动作为目标。\x02\x03",

            "此外，与操纵者的思想沟通为非接触式，\x01",
            "从候补者之中选定和采用合适的素材。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x3)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x2)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x1)
    Sleep(400)
    Sleep(400)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "机体各参数\x01",
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS345._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        30,
        280,
        0,
        "大略尺寸及重量\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(220, 290, 48, 4)

    AnonymousTalk(    #247
        (
            "\x07\x00  总高度：１５．５亚矩\x02\x01",

            "本体重量：５５托里姆\x01",
            "（※完全武装时６８托里姆）\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        30,
        340,
        0,
        "搭载装备\x01",
    )

    Jump("loc_D280")

    label("loc_D280")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #248
        (
            "\x07\x00除以导力能量炮为主体的\x01",
            "各种导力兵器外，\x01",
            "还装备有备用的数种火药兵器。\x02\x03",

            "此外，为了防止操纵者可能发生的危险，\x01",
            "还搭载了运用战术导力器的\x01",
            "治愈和复苏能量产生装置——『复苏系统』。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        3,
        30,
        400,
        0,
        "装甲材料\x01",
    )

    Jump("loc_D376")

    label("loc_D376")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #249
        (
            "\x07\x00装甲板所采用的材质是\x01",
            "一种被称为『导金』的合金。\x02\x03",

            "这种合金在各个方面\x01",
            "都堪称现时性能最高的合金。\x02\x03",

            "有关各种性能强度的详细数据，\x01",
            "请参阅『福音』计划。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x3)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x2)
    Sleep(400)
    OP_22(0x2, 0x0, 0x64)
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(400)
    Sleep(400)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        30,
        280,
        0,
        "计划各部分的进展状况\x01",
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        260,
        310,
        0,
        "新型导力引擎\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(310, 360, -1, -1)

    AnonymousTalk(    #250
        (
            "\x07\x00以诺华提斯博士的设计为基础，\x01",
            "开发进展顺利。\x02\x03",

            "为各部分的促动器提供导力的\x01",
            "测试也已经成功。\x02\x03",

            "然而，对于飞行引擎反应性的糟糕表现，\x01",
            "博士也面露难色。\x01",
            "（※特别是反重力发生引擎的反应性过低。）\x02\x03",

            "据判断，在现状下不可能进行战术性运用。\x01",
            "除使用飞行引擎的飘浮展开方法之外，\x01",
            "是否以助推器追加推进力也在研究之中——\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        40,
        255,
        0,
        "各部分促动器\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(120, 295, -1, -1)

    AnonymousTalk(    #251
        (
            "\x07\x00促动器开发陷入了困境。\x01",
            "因为无法从现有的人形兵器移用。\x02\x03",

            "主兵器装备的大型化使得战斗重量增大，\x01",
            "特别是腿部关节的耐用性测试仍存有问题。\x02\x03",

            "在避免精密控制的负荷过于集中这一方面，\x01",
            "预测可能得到改善——\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        20,
        75,
        0,
        "主兵器装备\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(20, 115, -1, -1)

    AnonymousTalk(    #252
        (
            "\x07\x00主兵器装备导力能量炮\x01",
            "已经完成了实战测试。\x02\x03",

            "然而，根据诺华提斯博士的指示，\x01",
            "同轴化仍在研究中，实际装载将被推迟。\x02\x03",

            "预计随之而来的必要输出功率增加\x01",
            "将被包括在新型导力引擎的输出功率之内。\x02",
        )
    )

    CloseMessageWindow()
    OP_5F(0x1)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        200,
        75,
        0,
        "控制系统\x01",
    )

    Jump("loc_D86D")

    label("loc_D86D")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(220, 115, -1, -1)

    AnonymousTalk(    #253
        (
            "\x07\x00控制系统现时仍在实验之中——\x02\x03",

            "实验结果详情可参阅其它项目。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        2,
        340,
        75,
        0,
        "控制测试结果\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    OP_5F(0x1)
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_A3(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS346._CH")
    OP_22(0x9D, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x4, 0, 0, 0)
    Sleep(1500)
    OP_43(0x0, 0x0, 0x0, 0x14)
    OP_56(0x2)
    OP_44(0x0, 0x0)
    OP_A2(0x0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #254
        (
            "\x07\x00使用神经系统的控制测试\x01",
            "现时仍在持续实施之中——\x02\x03",

            "然而，时至今日\x01",
            "仍未达到理想的精密度。\x02\x03",

            "迄今为止诺华提斯博士小组得到的主要测试结果，\x01",
            "可阅览上述条目。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "测试结果阅览\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    SetMessageWindowPos(310, 40, -1, -1)

    AnonymousTalk(    #255
        (
            "\x07\x00受试者：代号Ａ１　………\x02\x01",

            "　　在连接第２状态时反应异常、丧失意识\x02\x01",

            "受试者：代号Ｂ３　………\x02\x01",

            "　　在连接第３状态时反应异常、心跳停止\x02\x01",

            "受试者：代号Ｃ１　………\x02\x01",

            "　　在连接第１状态时反应异常、心神错乱\x02\x01",

            "受试者：代号Ｄ７　………\x02\x01",

            "　　在连接第２状态时反应异常、丧失意识\x02\x01",

            "受试者：代号Ｅ３　………\x02\x01",

            "　　在连接第２状态时反应异常、心跳停止\x02\x01",

            "受试者：代号Ｆ２　………\x02\x01",

            "　　在连接第２状态时反应异常、丧失意识\x02\x01",

            "受试者：代号Ｇ４　………\x02\x01",

            "　　在连接第３状态时反应异常、丧失意识\x02\x01",

            "受试者：代号Ｈ１　………\x02\x01",

            "　　在连接第２状态时反应异常、丧失意识\x02\x01",

            "受试者：代号Ｉ６　………\x02\x01",

            "　　在连接第４状态时反应异常、精神崩溃\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #256
        (
            "\x07\x00——所有受试者接连以失败告终。\x02\x03",

            "预定今后将由『结社』提供受试者，\x01",
            "继续进行实验——\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x9C, 0x0, 0x64)

    Menu(
        1,
        80,
        280,
        0,
        "今后的开发计划\x01",
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #257
        (
            "\x07\x00——『结社』发来暂时冻结的通知。\x02\x03",

            "理由是不能确认控制系统是否稳定。\x02\x03",

            "今后，参加连接试验的受试者\x01",
            "将限定于『结社』所选拔产生的候选人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS347._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    OP_22(0x9C, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #258
        (
            "\x07\x05受试者：代号Ｒ３——\x02\x01",

            "经过第４状态的连接测试，依然生存。\x02\x01",

            "※然而，存在轻度的神经反射现象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)

    AnonymousTalk(    #259
        (
            "\x07\x05受试者：代号Ｒ３——\x02\x01",

            "与『帕蒂尔·玛蒂尔』的意识沟通成功。\x02\x03",

            "向『结社』建议开发重新开始——\x01",
            "代号Ｒ３已在实际演习中成功。\x02\x03",

            "向『结社』建议开发重新开始——\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    Sleep(3000)
    Sleep(1500)
    OP_E3(0x1, 0x0)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #260
        "\x07\x00Episode『极限级实验计划书』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E118")
    Sleep(1000)
    OP_28(0x17, 0x4, 0x10)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #261
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_E10C")

    label("loc_E10C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_E118")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M5612   ._SN", 130, 0, 0)
    IdleLoop()
    Return()

    # Function_19_CCAB end

    def Function_20_E125(): pass

    label("Function_20_E125")

    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1000)

    label("loc_E148")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E190")
    Sleep(200)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E174")
    Jump("loc_E190")

    label("loc_E174")

    Sleep(200)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    Jump("loc_E148")

    label("loc_E190")

    Return()

    # Function_20_E125 end

    def Function_21_E191(): pass

    label("Function_21_E191")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1C5")
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1A, 0x0, 0x64)
    Sleep(500)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(500)
    Jump("Function_21_E191")

    label("loc_E1C5")

    Return()

    # Function_21_E191 end

    SaveToFile()

Try(main)
