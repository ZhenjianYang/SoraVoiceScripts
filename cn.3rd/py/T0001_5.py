from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0001_5 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        '',                                     # 8
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
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_6E2",          # 01, 1
        "Function_2_6E6",          # 02, 2
        "Function_3_9BA",          # 03, 3
        "Function_4_AC9",          # 04, 4
        "Function_5_C37",          # 05, 5
        "Function_6_D3E",          # 06, 6
        "Function_7_E40",          # 07, 7
        "Function_8_F65",          # 08, 8
        "Function_9_10BB",         # 09, 9
        "Function_10_1330",        # 0A, 10
        "Function_11_1613",        # 0B, 11
        "Function_12_18F7",        # 0C, 12
        "Function_13_1A54",        # 0D, 13
        "Function_14_1B22",        # 0E, 14
        "Function_15_1C2F",        # 0F, 15
        "Function_16_1CC0",        # 10, 16
        "Function_17_1DB2",        # 11, 17
        "Function_18_1EDA",        # 12, 18
        "Function_19_1FEB",        # 13, 19
        "Function_20_2071",        # 14, 20
        "Function_21_2109",        # 15, 21
        "Function_22_220B",        # 16, 22
        "Function_23_2302",        # 17, 23
        "Function_24_242C",        # 18, 24
        "Function_25_24B3",        # 19, 25
        "Function_26_254B",        # 1A, 26
        "Function_27_2641",        # 1B, 27
        "Function_28_26DD",        # 1C, 28
        "Function_29_2850",        # 1D, 29
        "Function_30_2935",        # 1E, 30
        "Function_31_29B1",        # 1F, 31
        "Function_32_2ADF",        # 20, 32
        "Function_33_2B99",        # 21, 33
        "Function_34_2CD6",        # 22, 34
        "Function_35_2DC1",        # 23, 35
        "Function_36_2F1D",        # 24, 36
        "Function_37_2FA8",        # 25, 37
        "Function_38_3144",        # 26, 38
        "Function_39_31C0",        # 27, 39
        "Function_40_323C",        # 28, 40
        "Function_41_32B8",        # 29, 41
        "Function_42_3334",        # 2A, 42
        "Function_43_33B0",        # 2B, 43
        "Function_44_4F16",        # 2C, 44
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        (
            "\x06选择章节。◎＝script调整完毕。\x01",
            "▼有为输入数据。Ａ＝ＡＰＬ。Ｅ＝特效。\x01",
            "Ｐ＝报告。Ｂ＝ＢＧＭ＆ＳＥ。Ｓ＝为输入场景\x02",
        )
    )


    label("loc_120")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D2")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "◎EP00『尤莉亚大人的假日』(短篇级)\x01",                # 0
            "◎EP01『山猫卡普亚的特急便』(迷你游戏)\x01",            # 1
            "◎EP02『旅程的终点』(短篇级)\x01",                      # 2
            "◎EP03『乐园的少女』(短篇级)\x01",                      # 3
            "◎EP05『庆功宴之夜』(短篇级)\x01",                      # 4
            "◎EP06『返回帝都』(短篇级)\x01",                        # 5
            "◎EP07『委托人』(中篇级)\x01",                          # 6
            "◎EP08『飘落的羽翼』(中篇级)\x01",                      # 7
            "◎EP09『幸福之石』(中篇级)\x01",                        # 8
            "◎EP10『轨迹占卜游戏』(迷你游戏)\x01",                  # 9
            "◎EP11『在东方人街』(迷你游戏)\x01",                    # 10
            "◎EP12『钓公师团入团考试』(迷你游戏)\x01",              # 11
            "◎EP13『重剑流特训法』(短篇级)\x01",                    # 12
            "◎EP16『里·武术大会』(迷你游戏)\x01",                  # 13
            "◎EP17『启程的清晨』(中篇级)\x01",                      # 14
            "◎EP18『剑之道』(短篇级)\x01",                          # 15
            "◎EP19『操之过急的父母心』(短篇级)\x01",                # 16
            "◎EP20『谨此接受调查委托』(短篇级)\x01",                # 17
            "◎EP25『导力装甲开发计划·前篇』(中篇级)\x01",          # 18
            "◎EP26『导力装甲开发计划·后篇』(中篇级)\x01",          # 19
            "◎EP29『幻焰计划』(短篇级)\x01",                        # 20
            "◎EP30『盐之桩』（Tips）\x01",                          # 21
            "◎EP31『『怪盗Ｂ』调查报告』（Tips）\x01",              # 22
            "◎EP32『爱普斯泰恩财团』（Tips）\x01",                  # 23
            "◎EP33『帝国游击士协会连续袭击事件』（Tips）\x01",      # 24
            "◎EP34『极限级实验计划书』（Tips）\x01",                # 25
        )
    )

    MenuEnd(0x0)
    Call(5, 1)
    OP_A2(0x2F00)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4FB"),
        (1, "loc_502"),
        (2, "loc_520"),
        (3, "loc_539"),
        (4, "loc_540"),
        (5, "loc_547"),
        (6, "loc_54E"),
        (7, "loc_555"),
        (8, "loc_55C"),
        (9, "loc_563"),
        (10, "loc_577"),
        (11, "loc_58B"),
        (12, "loc_5A9"),
        (13, "loc_5EA"),
        (14, "loc_5F1"),
        (15, "loc_5F8"),
        (16, "loc_619"),
        (17, "loc_632"),
        (18, "loc_639"),
        (19, "loc_640"),
        (20, "loc_647"),
        (21, "loc_65E"),
        (22, "loc_672"),
        (23, "loc_686"),
        (24, "loc_69A"),
        (25, "loc_6AE"),
        (SWITCH_DEFAULT, "loc_6C2"),
    )


    label("loc_4FB")

    Call(5, 3)
    Jump("loc_6CF")

    label("loc_502")

    OP_D6(0x0)
    OP_E3(0x0, 0x1, 1024, 0x0)
    ClearParty()
    AddParty(0xA, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_520")

    OP_D6(0x0)
    OP_E3(0x0, 0x2, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_539")

    Call(5, 4)
    Jump("loc_6CF")

    label("loc_540")

    Call(5, 5)
    Jump("loc_6CF")

    label("loc_547")

    Call(5, 6)
    Jump("loc_6CF")

    label("loc_54E")

    Call(5, 9)
    Jump("loc_6CF")

    label("loc_555")

    Call(5, 10)
    Jump("loc_6CF")

    label("loc_55C")

    Call(5, 11)
    Jump("loc_6CF")

    label("loc_563")

    OP_E3(0x0, 0xA, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_577")

    OP_E3(0x0, 0xB, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_58B")

    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_5A9")

    OP_A3(0x2F90)
    OP_A3(0x2F91)
    OP_A3(0x2F92)
    OP_A3(0x2F93)
    OP_A3(0x2F94)
    OP_A3(0x2F95)
    OP_A3(0x2F96)
    OP_A3(0x2F97)
    OP_D6(0x0)
    OP_E3(0x0, 0xD, 0, 0x0)
    ClearParty()
    AddParty(0x12, 0xF0, 0xFF)
    AddParty(0x10, 0xEE, 0xFF)
    AddParty(0x11, 0xEF, 0xFF)
    OP_C2(0x1, 0x4)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_5EA")

    Call(5, 2)
    Jump("loc_6CF")

    label("loc_5F1")

    Call(5, 12)
    Jump("loc_6CF")

    label("loc_5F8")

    OP_A3(0x2FA6)
    OP_D6(0x0)
    OP_E3(0x0, 0x12, 512, 0x0)
    ClearParty()
    AddParty(0x9, 0xEE, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_619")

    OP_D6(0x0)
    OP_E3(0x0, 0x13, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_632")

    Call(5, 13)
    Jump("loc_6CF")

    label("loc_639")

    Call(5, 7)
    Jump("loc_6CF")

    label("loc_640")

    Call(5, 8)
    Jump("loc_6CF")

    label("loc_647")

    OP_E3(0x0, 0x1D, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_65E")

    OP_E3(0x0, 0x1E, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_672")

    OP_E3(0x0, 0x1F, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_686")

    OP_E3(0x0, 0x20, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_69A")

    OP_E3(0x0, 0x21, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_6AE")

    OP_E3(0x0, 0x22, 0, 0x0)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6CF")

    label("loc_6C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CF")

    label("loc_6CF")

    Jump("loc_120")

    label("loc_6D2")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_6E2(): pass

    label("Function_1_6E2")

    OP_A3(0x2F00)
    Return()

    # Function_1_6E2 end

    def Function_2_6E6(): pass

    label("Function_2_6E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AA")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",                  # 0
            "■从标题开始（为完成）\x01",        # 1
            "■从标题开始（初级完成）\x01",      # 2
            "■从标题开始（中级完成）\x01",      # 3
            "■从标题开始（高级完成）\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78B"),
        (1, "loc_7E3"),
        (2, "loc_84D"),
        (3, "loc_8BC"),
        (4, "loc_930"),
        (SWITCH_DEFAULT, "loc_99A"),
    )


    label("loc_78B")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9A7")

    label("loc_7E3")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x3, 0x20)
    OP_28(0x22, 0x3, 0x20)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9A7")

    label("loc_84D")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x3, 0x20)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9A7")

    label("loc_8BC")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x8)
    OP_28(0x23, 0x3, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9A7")

    label("loc_930")

    OP_DB(0x0, 0xE)
    OP_DB(0x0, 0x6)
    OP_DB(0x0, 0xD)
    OP_DB(0x0, 0x1)
    OP_DB(0x0, 0xC)
    OP_DB(0x0, 0xA)
    OP_DB(0x0, 0x4)
    OP_DB(0x0, 0x9)
    OP_DB(0x0, 0x2)
    OP_DB(0x0, 0x5)
    OP_DB(0x0, 0xB)
    OP_DB(0x0, 0x3)
    OP_DB(0x0, 0x7)
    OP_DB(0x0, 0x0)
    OP_DB(0x0, 0xF)
    OP_DD(0x1, 0x0, 0x0, 0, 0, 0, 0)
    OP_A2(0x2F13)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x23, 0x4, 0x20)
    OP_E3(0x0, 0x10, 0, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9A7")

    label("loc_99A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A7")

    label("loc_9A7")

    Jump("Function_2_6E6")

    label("loc_9AA")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_6E6 end

    def Function_3_9BA(): pass

    label("Function_3_9BA")


    AnonymousTalk(    #1
        "\x06从哪开始？\x02",
    )


    label("loc_9CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB9")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",            # 0
            "■向尤莉亚大人突击\x01",      # 1
            "■修女艾伦登场\x01",          # 2
            "■与穆拉对话\x01",            # 3
            "■城内与科洛丝相会\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x0, 8192, 0x0)
    ClearParty()
    AddParty(0xD, 0xEE, 0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A5E"),
        (1, "loc_A6D"),
        (2, "loc_A7C"),
        (3, "loc_A8B"),
        (4, "loc_A9A"),
        (SWITCH_DEFAULT, "loc_AA9"),
    )


    label("loc_A5E")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AB6")

    label("loc_A6D")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AB6")

    label("loc_A7C")

    OP_A2(0x2506)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AB6")

    label("loc_A8B")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AB6")

    label("loc_A9A")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_AB6")

    label("loc_AA9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB6")

    label("loc_AB6")

    Jump("loc_9CA")

    label("loc_AB9")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_9BA end

    def Function_4_AC9(): pass

    label("Function_4_AC9")


    AnonymousTalk(    #2
        "\x06从哪开始？\x02",
    )


    label("loc_AD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C27")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■１．乐园\x01",                      # 0
            "■２．公主大人\x01",                  # 1
            "■３．游戏\x01",                      # 2
            "■４．玲\x01",                        # 3
            "■～幕間～\x01",                      # 4
            "■５．梦的延续\x01",                  # 5
            "■街道·夜　前往克洛斯贝尔\x01",      # 6
            "■夜天空地图\x01",                    # 7
        )
    )

    Jump("loc_B6B")

    label("loc_B6B")

    MenuEnd(0x0)
    OP_E3(0x0, 0x3, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B9F"),
        (1, "loc_BAE"),
        (2, "loc_BBD"),
        (3, "loc_BCC"),
        (4, "loc_BDB"),
        (5, "loc_BEA"),
        (6, "loc_BF9"),
        (7, "loc_C08"),
        (SWITCH_DEFAULT, "loc_C17"),
    )


    label("loc_B9F")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BAE")

    OP_A2(0x2505)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BBD")

    OP_A2(0x2506)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BCC")

    OP_A2(0x2507)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BDB")

    OP_A2(0x2508)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BEA")

    OP_A2(0x2509)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_BF9")

    OP_A2(0x250A)
    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_C08")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_C24")

    label("loc_C17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C24")

    label("loc_C24")

    Jump("loc_AD9")

    label("loc_C27")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_AC9 end

    def Function_5_C37(): pass

    label("Function_5_C37")

    OP_A3(0x2F9A)
    OP_A3(0x2F9B)
    OP_A3(0x2F9C)
    OP_A3(0x2F9D)
    OP_A3(0x2F9E)
    OP_A3(0x2F9F)
    OP_A3(0x2FA0)
    OP_A3(0x2FA1)
    OP_A3(0x2FA2)
    OP_A3(0x2FA3)

    AnonymousTalk(    #3
        "\x06从哪开始？\x02",
    )


    label("loc_C65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2E")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",        # 0
            "■从自由移动\x01",        # 1
            "■科洛丝的自白\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x5, 2, 0x0)
    ClearParty()
    AddParty(0x1, 0xEE, 0xFF)
    OP_BB(0x1, 0x1, 0x1C)
    OP_BD()
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CD6"),
        (1, "loc_CE5"),
        (2, "loc_CF4"),
        (SWITCH_DEFAULT, "loc_D1E"),
    )


    label("loc_CD6")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_D2B")

    label("loc_CE5")

    OP_A2(0x2F9A)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_D2B")

    label("loc_CF4")

    OP_A2(0x2F9A)
    OP_A2(0x2F9B)
    OP_A2(0x2F9C)
    OP_A2(0x2F9D)
    OP_A2(0x2F9E)
    OP_A2(0x2F9F)
    OP_A2(0x2FA0)
    OP_A2(0x2FA1)
    OP_A2(0x2FA2)
    OP_A2(0x2FA3)
    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_D2B")

    label("loc_D1E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D2B")

    label("loc_D2B")

    Jump("loc_C65")

    label("loc_D2E")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_C37 end

    def Function_6_D3E(): pass

    label("Function_6_D3E")


    AnonymousTalk(    #4
        "\x06从哪开始？\x02",
    )


    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E30")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",        # 0
            "■城·谒见大厅\x01",      # 1
            "■对话×２\x01",          # 2
            "■飞艇坪\x01",            # 3
            "■皇子的祝福\x01",        # 4
        )
    )

    Jump("loc_DAD")

    label("loc_DAD")

    MenuEnd(0x0)
    OP_E3(0x0, 0x6, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DD5"),
        (1, "loc_DE4"),
        (2, "loc_DF3"),
        (3, "loc_E02"),
        (4, "loc_E11"),
        (SWITCH_DEFAULT, "loc_E20"),
    )


    label("loc_DD5")

    OP_A2(0x2504)
    NewScene("ED6_DT21/U4163   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E2D")

    label("loc_DE4")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E2D")

    label("loc_DF3")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E2D")

    label("loc_E02")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E2D")

    label("loc_E11")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E2D")

    label("loc_E20")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E2D")

    label("loc_E2D")

    Jump("loc_D4E")

    label("loc_E30")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_D3E end

    def Function_7_E40(): pass

    label("Function_7_E40")


    AnonymousTalk(    #5
        "\x06从哪开始？\x02",
    )


    label("loc_E50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F55")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",        # 0
            "■傍晚吃饭之后\x01",      # 1
            "■第２日·早晨\x01",      # 2
            "■开发开始\x01",          # 3
            "■ＶＳ艾莉卡\x01",        # 4
            "■导力装甲完成\x01",      # 5
        )
    )

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x19, 64, 0x0)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EEB"),
        (1, "loc_EFA"),
        (2, "loc_F09"),
        (3, "loc_F18"),
        (4, "loc_F27"),
        (5, "loc_F36"),
        (SWITCH_DEFAULT, "loc_F45"),
    )


    label("loc_EEB")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_EFA")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_F09")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_F18")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3115   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_F27")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3116   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_F36")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_F52")

    label("loc_F45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F52")

    label("loc_F52")

    Jump("loc_E50")

    label("loc_F55")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_E40 end

    def Function_8_F65(): pass

    label("Function_8_F65")

    OP_A3(0x2F85)
    OP_A3(0x2F86)
    OP_A3(0x2F87)
    OP_A3(0x2F88)
    OP_A3(0x2F89)
    OP_A3(0x2F8A)
    OP_A3(0x2F8B)
    OP_A3(0x2F8C)
    OP_A3(0x2F8D)

    AnonymousTalk(    #6
        "\x06从哪开始？\x02",
    )


    label("loc_F90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AB")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",            # 0
            "■协会与艾莉卡相会\x01",      # 1
            "■到地下实验场\x01",          # 2
            "■测试开始\x01",              # 3
            "■导力装甲暴走\x01",          # 4
            "■结尾\x01",                  # 5
        )
    )

    Jump("loc_FFF")

    label("loc_FFF")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x1A, 32, 0x0)
    ClearParty()
    AddParty(0x5, 0xEE, 0xFF)
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1035"),
        (1, "loc_1044"),
        (2, "loc_1053"),
        (3, "loc_1065"),
        (4, "loc_1077"),
        (5, "loc_1089"),
        (SWITCH_DEFAULT, "loc_109B"),
    )


    label("loc_1035")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_1044")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_1053")

    OP_A2(0x2F85)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_1065")

    OP_A2(0x2F85)
    OP_A2(0x2507)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_1077")

    OP_A2(0x2F85)
    OP_A2(0x250A)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_1089")

    OP_A2(0x2F85)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_10A8")

    label("loc_109B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10A8")

    label("loc_10A8")

    Jump("loc_F90")

    label("loc_10AB")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_F65 end

    def Function_9_10BB(): pass

    label("Function_9_10BB")


    AnonymousTalk(    #7
        "\x06从哪开始？\x02",
    )

    OP_A3(0x2F4A)
    OP_A3(0x2F4B)
    OP_A3(0x2F4C)
    OP_A3(0x2F4D)
    OP_A3(0x2F4E)
    OP_A3(0x2F4F)
    OP_A3(0x2F50)
    OP_A3(0x2F51)
    OP_A3(0x2F52)
    OP_A3(0x2F53)
    OP_A3(0x2F54)
    OP_A3(0x2F55)
    OP_A3(0x2F56)
    OP_A3(0x2F57)
    OP_A3(0x2F58)
    OP_A3(0x2F59)
    OP_A3(0x2F5A)

    label("loc_10FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1320")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",              # 0
            "■艾德尔百货店\x01",            # 1
            "■酒店前\x01",                  # 2
            "■竞技场前\x01",                # 3
            "■在地下水道回想\x01",          # 4
            "■从地下逃脱\x01",              # 5
            "■翌日进入格兰赛尔城\x01",      # 6
            "■城前，与叔父的对决\x01",      # 7
            "■结尾\x01",                    # 8
        )
    )

    Jump("loc_11A8")

    label("loc_11A8")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x7, 0, 0x0)
    ClearParty()
    AddParty(0x2, 0xEE, 0xFF)
    OP_BB(0x2, 0x1, 0x18)
    OP_BD()
    OP_C2(0x1, 0x4)
    OP_31(0x2, 0x0, 0xA)
    OP_31(0x2, 0xFE, 0x0)
    OP_41(0x2, 0x44E, 0xFF)
    OP_41(0x2, 0x63F, 0xFF)
    OP_41(0x2, 0x7F, 0xFF)
    OP_35(0x2, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_120F"),
        (1, "loc_121B"),
        (2, "loc_122E"),
        (3, "loc_1247"),
        (4, "loc_1263"),
        (5, "loc_127F"),
        (6, "loc_12A1"),
        (7, "loc_12C6"),
        (8, "loc_12EB"),
        (SWITCH_DEFAULT, "loc_1310"),
    )


    label("loc_120F")

    NewScene("ED6_DT21/T0135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_121B")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_122E")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_1247")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_1263")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    NewScene("ED6_DT21/C4201   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_127F")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    NewScene("ED6_DT21/C4200   ._SN", 114, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_12A1")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4102   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_12C6")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_12EB")

    AddParty(0x50, 0xFF, 0xFF)
    OP_A2(0x2F4A)
    OP_A2(0x2F4B)
    OP_A2(0x2F4C)
    OP_A2(0x2F4D)
    OP_A2(0x2F4E)
    OP_A2(0x2F4F)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_131D")

    label("loc_1310")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_131D")

    label("loc_131D")

    Jump("loc_10FE")

    label("loc_1320")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_10BB end

    def Function_10_1330(): pass

    label("Function_10_1330")


    AnonymousTalk(    #8
        "\x06从哪开始？\x02",
    )

    OP_A3(0x2F65)
    OP_A3(0x2F66)
    OP_A3(0x2F67)
    OP_A3(0x2F68)
    OP_A3(0x2F69)
    OP_A3(0x2F6A)
    OP_A3(0x2F6B)
    OP_A3(0x2F6C)
    OP_A3(0x2F6D)
    OP_A3(0x2F6E)
    OP_A3(0x2F6F)
    OP_A3(0x2F70)
    OP_A3(0x2F71)
    OP_A3(0x2F72)
    OP_A3(0x2F73)
    OP_A3(0x2F74)
    OP_A3(0x2F75)
    OP_A3(0x2F76)
    OP_A3(0x2F77)
    OP_A3(0x2F78)
    OP_A3(0x2F79)
    OP_A3(0x2F7A)
    OP_A3(0x2F7B)
    OP_A3(0x2F7C)
    OP_A3(0x2F7D)
    OP_A3(0x2F7E)
    OP_A3(0x2F7F)
    OP_A3(0x2F80)
    OP_A3(0x2F81)
    OP_A3(0x2F82)
    OP_A3(0x2F83)
    OP_A3(0x2FA7)

    label("loc_13A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1603")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",            # 0
            "■发布影印\x01",              # 1
            "■寻找雷克特\x01",            # 2
            "■定期试验\x01",              # 3
            "■前往卢安\x01",              # 4
            "■与克拉姆相会\x01",          # 5
            "■与基库吵嚷\x01",            # 6
            "■与乔儿和汉斯见面\x01",      # 7
            "■乔儿，去孤儿院\x01",        # 8
            "■结尾\x01",                  # 9
        )
    )

    Jump("loc_1441")

    label("loc_1441")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x8, 0, 0x0)
    ClearParty()
    AddParty(0x4, 0xEE, 0xFF)
    OP_BB(0x4, 0x1, 0x4)
    OP_BD()
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_148F"),
        (1, "loc_149B"),
        (2, "loc_14AA"),
        (3, "loc_14CE"),
        (4, "loc_14F2"),
        (5, "loc_1519"),
        (6, "loc_1540"),
        (7, "loc_156A"),
        (8, "loc_1599"),
        (9, "loc_15C3"),
        (SWITCH_DEFAULT, "loc_15F3"),
    )


    label("loc_148F")

    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_149B")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_14AA")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_14CE")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_14F2")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_1519")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    NewScene("ED6_DT21/R2202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_1540")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2800   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_156A")

    ClearParty()
    AddParty(0x3A, 0xEE, 0xFF)
    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    NewScene("ED6_DT21/T2812   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_1599")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_15C3")

    OP_A2(0x2F65)
    OP_A2(0x2F66)
    OP_A2(0x2F67)
    OP_A2(0x2F68)
    OP_A2(0x2F69)
    OP_A2(0x2F6A)
    OP_A2(0x2F6B)
    OP_A2(0x2F6C)
    OP_A2(0x2F6D)
    OP_A2(0x2F6E)
    OP_A2(0x2F6F)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1600")

    label("loc_15F3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1600")

    label("loc_1600")

    Jump("loc_13A0")

    label("loc_1603")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_1330 end

    def Function_11_1613(): pass

    label("Function_11_1613")


    AnonymousTalk(    #9
        "\x06从哪开始？\x02",
    )

    OP_A3(0x2F17)
    OP_A3(0x2F18)
    OP_A3(0x2F19)
    OP_A3(0x2F1A)
    OP_A3(0x2F1B)
    OP_A3(0x2F1C)
    OP_A3(0x2F1D)
    OP_A3(0x2F1E)
    OP_A3(0x2F1F)
    OP_A3(0x2F20)
    OP_A3(0x2F21)
    OP_A3(0x2F22)
    OP_A3(0x2F23)
    OP_A3(0x2F24)
    OP_A3(0x2F25)
    OP_A3(0x2F26)
    OP_A3(0x2F28)
    OP_A3(0x2F29)
    OP_A3(0x2F3A)
    OP_A3(0x2F3B)
    OP_A3(0x2F3C)
    OP_A3(0x2F3D)
    OP_A3(0x2F3E)
    OP_A3(0x2F3F)
    OP_A3(0x2F40)
    OP_A3(0x2F41)
    OP_A3(0x2F42)
    OP_A3(0x2F43)
    OP_A3(0x2F44)
    OP_A3(0x2F45)

    label("loc_167D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E7")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",                        # 0
            "■沙滩收集贝壳\x01",                      # 1
            "■义卖会会场\x01",                        # 2
            "■在玛诺利亚间道成了迷路的孩子\x01",      # 3
            "■在古罗尼山峰成了迷路的孩子\x01",        # 4
            "■捡柴\x01",                              # 5
            "■早晨，没有魔兽\x01",                    # 6
            "■其实可以飞\x01",                        # 7
            "■结尾\x01",                              # 8
        )
    )

    Jump("loc_1736")

    label("loc_1736")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x9, 0, 0x0)
    ClearParty()
    AddParty(0x4D, 0xEE, 0xFF)
    OP_C2(0x1, 0x1F)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1778"),
        (1, "loc_1784"),
        (2, "loc_1797"),
        (3, "loc_17BC"),
        (4, "loc_17E4"),
        (5, "loc_1811"),
        (6, "loc_1835"),
        (7, "loc_186B"),
        (8, "loc_18A1"),
        (SWITCH_DEFAULT, "loc_18D7"),
    )


    label("loc_1778")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_1784")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    NewScene("ED6_DT21/R2200   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_1797")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    NewScene("ED6_DT21/T2310   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_17BC")

    AddParty(0x4E, 0xFF, 0xFF)
    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    NewScene("ED6_DT21/R2101   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_17E4")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_1811")

    OP_A2(0x2F17)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_1835")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_186B")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_18A1")

    OP_A2(0x2F17)
    OP_A2(0x2F1B)
    OP_A2(0x2F1C)
    OP_A2(0x2F1D)
    OP_A2(0x2F1E)
    OP_A2(0x2F1F)
    OP_A2(0x2F20)
    OP_A2(0x2F21)
    OP_A2(0x2F22)
    OP_A2(0x2F23)
    OP_A2(0x2F24)
    OP_A2(0x2F25)
    OP_A2(0x2F26)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_18E4")

    label("loc_18D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18E4")

    label("loc_18E4")

    Jump("loc_167D")

    label("loc_18E7")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_1613 end

    def Function_12_18F7(): pass

    label("Function_12_18F7")


    AnonymousTalk(    #10
        "\x06从哪开始？\x02",
    )

    OP_A3(0x2F60)
    OP_A3(0x2F61)
    OP_A3(0x2F62)

    label("loc_1910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A44")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",              # 0
            "■第２周\x01",                  # 1
            "■夜·与卡西乌斯对话\x01",      # 2
            "■帕赛尔农场\x01",              # 3
            "■芳香剂制作\x01",              # 4
            "■神秘森林\x01",                # 5
            "■结尾\x01",                    # 6
        )
    )

    Jump("loc_1992")

    label("loc_1992")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x11, 0, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_BB(0x0, 0x1, 0x44)
    OP_BD()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_19D1"),
        (1, "loc_19DD"),
        (2, "loc_19EC"),
        (3, "loc_19F8"),
        (4, "loc_1A04"),
        (5, "loc_1A10"),
        (6, "loc_1A22"),
        (SWITCH_DEFAULT, "loc_1A34"),
    )


    label("loc_19D1")

    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_19DD")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_19EC")

    NewScene("ED6_DT21/T0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_19F8")

    NewScene("ED6_DT21/R0201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_1A04")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_1A10")

    OP_A2(0x2F61)
    OP_A2(0x2F62)
    NewScene("ED6_DT21/C0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_1A22")

    OP_A2(0x2F61)
    OP_A2(0x2F62)
    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1A41")

    label("loc_1A34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A41")

    label("loc_1A41")

    Jump("loc_1910")

    label("loc_1A44")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_18F7 end

    def Function_13_1A54(): pass

    label("Function_13_1A54")


    AnonymousTalk(    #11
        "\x06从哪开始？\x02",
    )


    label("loc_1A64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B12")

    Menu(
        4,
        -1,
        32,
        1,
        (
            "■从最初开始\x01",        # 0
            "■夜·向飞艇坪\x01",      # 1
            "■翌日\x01",              # 2
        )
    )

    Jump("loc_1AA6")

    label("loc_1AA6")

    MenuEnd(0x0)
    OP_D6(0x0)
    OP_E3(0x0, 0x14, 2048, 0x0)
    ClearParty()
    AddParty(0xB, 0xEE, 0xFF)
    OP_BB(0xB, 0x1, 0x53)
    OP_BD()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AD5"),
        (1, "loc_1AE4"),
        (2, "loc_1AF3"),
        (SWITCH_DEFAULT, "loc_1B02"),
    )


    label("loc_1AD5")

    OP_A2(0x2504)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B0F")

    label("loc_1AE4")

    OP_A2(0x2506)
    NewScene("ED6_DT21/T2101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B0F")

    label("loc_1AF3")

    OP_A2(0x2505)
    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B0F")

    label("loc_1B02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B0F")

    label("loc_1B0F")

    Jump("loc_1A64")

    label("loc_1B12")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_1A54 end

    def Function_14_1B22(): pass

    label("Function_14_1B22")


    AnonymousTalk(    #12
        "\x06哪里？\x02",
    )

    Jump("loc_1B37")

    label("loc_1B37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C1F")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T3100  工房都市蔡斯外部（街区）\x01",             # 0
            "T3111  工房都市蔡斯内部（工房区）B1/1F\x01",      # 1
            "T3133  拉赛尔工房\x01",                           # 2
            "T3121  (重新规划）地下实验场\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BDF"),
        (1, "loc_1BEB"),
        (2, "loc_1BF7"),
        (3, "loc_1C03"),
        (SWITCH_DEFAULT, "loc_1C0F"),
    )


    label("loc_1BDF")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C1C")

    label("loc_1BEB")

    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C1C")

    label("loc_1BF7")

    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C1C")

    label("loc_1C03")

    NewScene("ED6_DT21/T3121   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C1C")

    label("loc_1C0F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C1C")

    label("loc_1C1C")

    Jump("loc_1B37")

    label("loc_1C1F")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_1B22 end

    def Function_15_1C2F(): pass

    label("Function_15_1C2F")


    AnonymousTalk(    #13
        "\x06哪里？\x02",
    )

    Jump("loc_1C44")

    label("loc_1C44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB0")

    Menu(
        4,
        -1,
        -1,
        1,
        "R1204 （重新规划）西柏斯街道（R1203改造）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C94"),
        (SWITCH_DEFAULT, "loc_1CA0"),
    )


    label("loc_1C94")

    NewScene("ED6_DT21/R1204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1CAD")

    label("loc_1CA0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAD")

    label("loc_1CAD")

    Jump("loc_1C44")

    label("loc_1CB0")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1C2F end

    def Function_16_1CC0(): pass

    label("Function_16_1CC0")


    AnonymousTalk(    #14
        "\x06哪里？\x02",
    )

    Jump("loc_1CD5")

    label("loc_1CD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA2")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C3100  工房都市蔡斯外部（街区）\x01",             # 0
            "C3101  工房都市蔡斯内部（工房区）B1/1F\x01",      # 1
            "C3110  雷斯顿水上要塞内部（司令塔）\x01",         # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D6E"),
        (1, "loc_1D7A"),
        (2, "loc_1D86"),
        (SWITCH_DEFAULT, "loc_1D92"),
    )


    label("loc_1D6E")

    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D9F")

    label("loc_1D7A")

    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D9F")

    label("loc_1D86")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1D9F")

    label("loc_1D92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D9F")

    label("loc_1D9F")

    Jump("loc_1CD5")

    label("loc_1DA2")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1CC0 end

    def Function_17_1DB2(): pass

    label("Function_17_1DB2")


    AnonymousTalk(    #15
        "\x06哪里？\x02",
    )

    Jump("loc_1DC7")

    label("loc_1DC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ECA")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C5400  古罗力亚斯内部（监禁艾丝蒂尔的房间）\x01",      # 0
            "C5407  古罗力亚斯内部　导力梯箱\x01",                  # 1
            "C5401  古罗力亚斯内部（怀斯曼房间）\x01",              # 2
            "C5408  古罗力亚斯外装（甲板）\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E87"),
        (1, "loc_1E96"),
        (2, "loc_1EA2"),
        (3, "loc_1EAE"),
        (SWITCH_DEFAULT, "loc_1EBA"),
    )


    label("loc_1E87")

    OP_A2(0x2504)
    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1EC7")

    label("loc_1E96")

    NewScene("ED6_DT21/C5407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1EC7")

    label("loc_1EA2")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1EC7")

    label("loc_1EAE")

    NewScene("ED6_DT21/C5408   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1EC7")

    label("loc_1EBA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EC7")

    label("loc_1EC7")

    Jump("loc_1DC7")

    label("loc_1ECA")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_1DB2 end

    def Function_18_1EDA(): pass

    label("Function_18_1EDA")


    AnonymousTalk(    #16
        "\x06哪里？\x02",
    )

    Jump("loc_1EEF")

    label("loc_1EEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FDB")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4101  王都格兰赛尔外部（东街区）\x01",      # 0
            "T4138  帝国大使馆内部\x01",                  # 1
            "T4200  格兰赛尔城外部(和大街连接)\x01",      # 2
            "T4220  格兰赛尔城内部(谒见大厅)\x01",        # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F9B"),
        (1, "loc_1FA7"),
        (2, "loc_1FB3"),
        (3, "loc_1FBF"),
        (SWITCH_DEFAULT, "loc_1FCB"),
    )


    label("loc_1F9B")

    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FD8")

    label("loc_1FA7")

    NewScene("ED6_DT21/T4138   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FD8")

    label("loc_1FB3")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FD8")

    label("loc_1FBF")

    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FD8")

    label("loc_1FCB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FD8")

    label("loc_1FD8")

    Jump("loc_1EEF")

    label("loc_1FDB")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_1EDA end

    def Function_19_1FEB(): pass

    label("Function_19_1FEB")


    AnonymousTalk(    #17
        "\x06哪里？\x02",
    )

    Jump("loc_2000")

    label("loc_2000")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2061")

    Menu(
        4,
        -1,
        -1,
        1,
        "R4103  庭院大道王都前（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2042"),
        (SWITCH_DEFAULT, "loc_2051"),
    )


    label("loc_2042")

    OP_A2(0x2504)
    NewScene("ED6_DT21/R4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_205E")

    label("loc_2051")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_205E")

    label("loc_205E")

    Jump("loc_2000")

    label("loc_2061")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_1FEB end

    def Function_20_2071(): pass

    label("Function_20_2071")


    AnonymousTalk(    #18
        "\x06哪里？\x02",
    )

    Jump("loc_2086")

    label("loc_2086")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E4")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4210  格兰赛尔城内部(大厅)\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20C8"),
        (SWITCH_DEFAULT, "loc_20D4"),
    )


    label("loc_20C8")

    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_20E1")

    label("loc_20D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20E1")

    label("loc_20E1")

    Jump("loc_2086")

    label("loc_20E4")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #19
        "\x06哪里？\x02",
    )

    Jump("loc_2108")

    label("loc_2108")

    Return()

    # Function_20_2071 end

    def Function_21_2109(): pass

    label("Function_21_2109")


    AnonymousTalk(    #20
        "\x06哪里？\x02",
    )

    Jump("loc_211E")

    label("loc_211E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FB")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T0100  洛连特外部\x01",                            # 0
            "T0101  (夜)洛连特外部\x01",                        # 1
            "T0121  商店１F·２F、游击士协会１F·２F\x01",      # 2
            "T0135  (夜)酒馆、厨房、２F\x01",                   # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21BB"),
        (1, "loc_21C7"),
        (2, "loc_21D3"),
        (3, "loc_21DF"),
        (SWITCH_DEFAULT, "loc_21EB"),
    )


    label("loc_21BB")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21F8")

    label("loc_21C7")

    NewScene("ED6_DT21/T0101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21F8")

    label("loc_21D3")

    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21F8")

    label("loc_21DF")

    NewScene("ED6_DT21/T0135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_21F8")

    label("loc_21EB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21F8")

    label("loc_21F8")

    Jump("loc_211E")

    label("loc_21FB")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_2109 end

    def Function_22_220B(): pass

    label("Function_22_220B")


    AnonymousTalk(    #21
        "\x06哪里？\x02",
    )

    Jump("loc_2220")

    label("loc_2220")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22F2")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T3200  亚尔摩外部\x01",                # 0
            "T3201  亚尔摩外部（夜）\x01",          # 1
            "T3221  亚尔摩内部（旅馆）\x01",        # 2
            "T3223  亚尔摩内部（旅馆夜）\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22B2"),
        (1, "loc_22BE"),
        (2, "loc_22CA"),
        (3, "loc_22D6"),
        (SWITCH_DEFAULT, "loc_22E2"),
    )


    label("loc_22B2")

    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22EF")

    label("loc_22BE")

    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22EF")

    label("loc_22CA")

    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22EF")

    label("loc_22D6")

    NewScene("ED6_DT21/T3223   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_22EF")

    label("loc_22E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22EF")

    label("loc_22EF")

    Jump("loc_2220")

    label("loc_22F2")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_220B end

    def Function_23_2302(): pass

    label("Function_23_2302")


    AnonymousTalk(    #22
        "\x06哪里？\x02",
    )

    Jump("loc_2317")

    label("loc_2317")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241C")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "E0810  空中盒子（有空心墙）＜前半＞\x01",           # 0
            "E0102 （重新规划）飞船（空贼用）外侧白天\x01",      # 1
            "E0110  飞船（空贼用夜）内部\x01",                   # 2
            "E0810  空中盒子（有空心墙）＜后半＞\x01",           # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23D6"),
        (1, "loc_23E5"),
        (2, "loc_23F1"),
        (3, "loc_23FD"),
        (SWITCH_DEFAULT, "loc_240C"),
    )


    label("loc_23D6")

    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2419")

    label("loc_23E5")

    NewScene("ED6_DT21/E0102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2419")

    label("loc_23F1")

    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2419")

    label("loc_23FD")

    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2419")

    label("loc_240C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2419")

    label("loc_2419")

    Jump("loc_2317")

    label("loc_241C")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_2302 end

    def Function_24_242C(): pass

    label("Function_24_242C")


    AnonymousTalk(    #23
        "\x06哪里？\x02",
    )

    Jump("loc_2441")

    label("loc_2441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24A3")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4142  酒馆　利贝尔通讯社（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2487"),
        (SWITCH_DEFAULT, "loc_2493"),
    )


    label("loc_2487")

    NewScene("ED6_DT21/T4142   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_24A0")

    label("loc_2493")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24A0")

    label("loc_24A0")

    Jump("loc_2441")

    label("loc_24A3")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_242C end

    def Function_25_24B3(): pass

    label("Function_25_24B3")


    AnonymousTalk(    #24
        "\x06哪里？\x02",
    )

    Jump("loc_24C8")

    label("loc_24C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253B")

    Menu(
        4,
        -1,
        -1,
        1,
        "T4206 （重新规划）格兰赛尔城外部(空中庭院)（夜）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_251F"),
        (SWITCH_DEFAULT, "loc_252B"),
    )


    label("loc_251F")

    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2538")

    label("loc_252B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2538")

    label("loc_2538")

    Jump("loc_24C8")

    label("loc_253B")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_24B3 end

    def Function_26_254B(): pass

    label("Function_26_254B")


    AnonymousTalk(    #25
        "\x06哪里？\x02",
    )

    Jump("loc_2560")

    label("loc_2560")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2631")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C5408  古罗力亚斯外装（甲板）\x01",                     # 0
            "C5401  古罗力亚斯内部（怀斯曼房间）\x01",               # 1
            "C5416 （重新规划）古罗力亚斯内部（星辰之间）\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25FD"),
        (1, "loc_2609"),
        (2, "loc_2615"),
        (SWITCH_DEFAULT, "loc_2621"),
    )


    label("loc_25FD")

    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_262E")

    label("loc_2609")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_262E")

    label("loc_2615")

    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_262E")

    label("loc_2621")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_262E")

    label("loc_262E")

    Jump("loc_2560")

    label("loc_2631")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_254B end

    def Function_27_2641(): pass

    label("Function_27_2641")


    AnonymousTalk(    #26
        (
            "\x06！注意！\x01",
            "※为了保留项目不可跳跃。别见怪。\x02",
        )
    )

    Jump("loc_267C")

    label("loc_267C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CD")

    Menu(
        4,
        -1,
        -1,
        1,
        "R2201  梅威海道（中央）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26BA"),
        (SWITCH_DEFAULT, "loc_26BD"),
    )


    label("loc_26BA")

    Jump("loc_26CA")

    label("loc_26BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26CA")

    label("loc_26CA")

    Jump("loc_267C")

    label("loc_26CD")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_2641 end

    def Function_28_26DD(): pass

    label("Function_28_26DD")


    AnonymousTalk(    #27
        "\x06哪里？\x02",
    )

    Jump("loc_26F2")

    label("loc_26F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2840")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "C3101  雷斯顿水上要塞外部(中庭)）\x01",        # 0
            "C3110  雷斯顿水上要塞内部（司令塔）\x01",      # 1
            "C3102  雷斯顿水上要塞外部(飞机库)\x01",        # 2
            "E0610  红色高速飞艇内部\x01",                  # 3
            "E0810  空中盒子（有空心墙）\x01",              # 4
            "T4202  格兰赛尔城外部(女王露台)\x01",          # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27E8"),
        (1, "loc_27F4"),
        (2, "loc_2800"),
        (3, "loc_280C"),
        (4, "loc_2818"),
        (5, "loc_2824"),
        (SWITCH_DEFAULT, "loc_2830"),
    )


    label("loc_27E8")

    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_27F4")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_2800")

    NewScene("ED6_DT21/C3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_280C")

    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_2818")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_2824")

    NewScene("ED6_DT21/T4202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_283D")

    label("loc_2830")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_283D")

    label("loc_283D")

    Jump("loc_26F2")

    label("loc_2840")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_26DD end

    def Function_29_2850(): pass

    label("Function_29_2850")


    AnonymousTalk(    #28
        "\x06哪里？\x02",
    )

    Jump("loc_2865")

    label("loc_2865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2925")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4220  格兰赛尔城内部(谒见大厅)\x01",      # 0
            "T4230  格兰赛尔城内部(女王宫)\x01",        # 1
            "T4202  格兰赛尔城外部(女王露台)\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_28F1"),
        (1, "loc_28FD"),
        (2, "loc_2909"),
        (SWITCH_DEFAULT, "loc_2915"),
    )


    label("loc_28F1")

    NewScene("ED6_DT21/T4220   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2922")

    label("loc_28FD")

    NewScene("ED6_DT21/T4230   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2922")

    label("loc_2909")

    NewScene("ED6_DT21/T4202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2922")

    label("loc_2915")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2922")

    label("loc_2922")

    Jump("loc_2865")

    label("loc_2925")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_2850 end

    def Function_30_2935(): pass

    label("Function_30_2935")


    AnonymousTalk(    #29
        "\x06哪里？\x02",
    )

    Jump("loc_294A")

    label("loc_294A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A1")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_2975")

    label("loc_2975")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2985"),
        (SWITCH_DEFAULT, "loc_2991"),
    )


    label("loc_2985")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_299E")

    label("loc_2991")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_299E")

    label("loc_299E")

    Jump("loc_294A")

    label("loc_29A1")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_2935 end

    def Function_31_29B1(): pass

    label("Function_31_29B1")


    AnonymousTalk(    #30
        "\x06哪里？\x02",
    )

    Jump("loc_29C6")

    label("loc_29C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ACF")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4400  王都格兰赛尔外部（码头１）\x01",                     # 0
            "T4401  王都格兰赛尔外部（码头２）\x01",                     # 1
            "T4106  格兰赛尔飞艇坪(无埃尔赛尤)/(绿)赛希莉亚号\x01",      # 2
            "T4100  王都格兰赛尔外部（南街区）\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A8F"),
        (1, "loc_2A9B"),
        (2, "loc_2AA7"),
        (3, "loc_2AB3"),
        (SWITCH_DEFAULT, "loc_2ABF"),
    )


    label("loc_2A8F")

    NewScene("ED6_DT21/T4400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ACC")

    label("loc_2A9B")

    NewScene("ED6_DT21/T4401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ACC")

    label("loc_2AA7")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ACC")

    label("loc_2AB3")

    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ACC")

    label("loc_2ABF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ACC")

    label("loc_2ACC")

    Jump("loc_29C6")

    label("loc_2ACF")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_29B1 end

    def Function_32_2ADF(): pass

    label("Function_32_2ADF")


    AnonymousTalk(    #31
        "\x06哪里？\x02",
    )

    Jump("loc_2AF4")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B89")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T2402  玛西亚孤儿院外部（再建后）\x01",      # 0
            "T2412  玛西亚孤儿院内部（再建后)\x01",       # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B61"),
        (1, "loc_2B6D"),
        (SWITCH_DEFAULT, "loc_2B79"),
    )


    label("loc_2B61")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B86")

    label("loc_2B6D")

    NewScene("ED6_DT21/T2412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B86")

    label("loc_2B79")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B86")

    label("loc_2B86")

    Jump("loc_2AF4")

    label("loc_2B89")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_2ADF end

    def Function_33_2B99(): pass

    label("Function_33_2B99")


    AnonymousTalk(    #32
        "\x06哪里？\x02",
    )

    Jump("loc_2BAE")

    label("loc_2BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CC6")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T2500  杰尼丝王立学院外部\x01",              # 0
            "T2510  杰尼丝王立学院（主楼）\x01",          # 1
            "T2511  杰尼丝王立学院（社团大楼）\x01",      # 2
            "T2512  杰尼丝王立学院（宿舍）\x01",          # 3
            "T2513  杰尼丝王立学院（礼堂）\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C7A"),
        (1, "loc_2C86"),
        (2, "loc_2C92"),
        (3, "loc_2C9E"),
        (4, "loc_2CAA"),
        (SWITCH_DEFAULT, "loc_2CB6"),
    )


    label("loc_2C7A")

    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CC3")

    label("loc_2C86")

    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CC3")

    label("loc_2C92")

    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CC3")

    label("loc_2C9E")

    NewScene("ED6_DT21/T2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CC3")

    label("loc_2CAA")

    NewScene("ED6_DT21/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2CC3")

    label("loc_2CB6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2CC3")

    label("loc_2CC3")

    Jump("loc_2BAE")

    label("loc_2CC6")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_2B99 end

    def Function_34_2CD6(): pass

    label("Function_34_2CD6")


    AnonymousTalk(    #33
        "\x06哪里？\x02",
    )

    Jump("loc_2CEB")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB1")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T1101  柏斯外部　北\x01",          # 0
            "T1100  柏斯外部　南\x01",          # 1
            "T1122  柏斯超市内部\x01",          # 2
            "T1111  柏斯市长官邸内部\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D71"),
        (1, "loc_2D7D"),
        (2, "loc_2D89"),
        (3, "loc_2D95"),
        (SWITCH_DEFAULT, "loc_2DA1"),
    )


    label("loc_2D71")

    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2DAE")

    label("loc_2D7D")

    NewScene("ED6_DT21/T1100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2DAE")

    label("loc_2D89")

    NewScene("ED6_DT21/T1122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2DAE")

    label("loc_2D95")

    NewScene("ED6_DT21/T1111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2DAE")

    label("loc_2DA1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DAE")

    label("loc_2DAE")

    Jump("loc_2CEB")

    label("loc_2DB1")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2CD6 end

    def Function_35_2DC1(): pass

    label("Function_35_2DC1")


    AnonymousTalk(    #34
        "\x06哪里？\x02",
    )

    Jump("loc_2DD6")

    label("loc_2DD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0D")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "T4200  格兰赛尔城外部(和大街连接)\x01",                   # 0
            "T4106  格兰赛尔飞艇坪(无埃尔赛尤)/(白)埃尔赛尤\x01",      # 1
            "T4213  格兰赛尔城内部(亲卫队办事处)\x01",                 # 2
            "T4214  格兰赛尔城内部(女佣房间)\x01",                     # 3
            "T4201  格兰赛尔城外部(空中庭院)\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EC1"),
        (1, "loc_2ECD"),
        (2, "loc_2ED9"),
        (3, "loc_2EE5"),
        (4, "loc_2EF1"),
        (SWITCH_DEFAULT, "loc_2EFD"),
    )


    label("loc_2EC1")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F0A")

    label("loc_2ECD")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F0A")

    label("loc_2ED9")

    NewScene("ED6_DT21/T4213   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F0A")

    label("loc_2EE5")

    NewScene("ED6_DT21/T4214   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F0A")

    label("loc_2EF1")

    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F0A")

    label("loc_2EFD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F0A")

    label("loc_2F0A")

    Jump("loc_2DD6")

    label("loc_2F0D")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2DC1 end

    def Function_36_2F1D(): pass

    label("Function_36_2F1D")


    AnonymousTalk(    #35
        "\x06哪里？\x02",
    )

    Jump("loc_2F32")

    label("loc_2F32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F98")

    Menu(
        4,
        -1,
        -1,
        1,
        "C3110  雷斯顿水上要塞内部（司令塔）\x01",
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F7C"),
        (SWITCH_DEFAULT, "loc_2F88"),
    )


    label("loc_2F7C")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2F95")

    label("loc_2F88")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F95")

    label("loc_2F95")

    Jump("loc_2F32")

    label("loc_2F98")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_2F1D end

    def Function_37_2FA8(): pass

    label("Function_37_2FA8")


    AnonymousTalk(    #36
        "\x06哪里？\x02",
    )

    Jump("loc_2FBD")

    label("loc_2FBD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3134")

    Menu(
        4,
        -1,
        -1,
        1,
        (
            "R0100  艾利兹街道(洛连特侧、布莱特家)\x01",        # 0
            "T0100  洛连特外部\x01",                            # 1
            "T0120  武器屋１F·２F、工房\x01",                  # 2
            "T0121  商店１F·２F、游击士协会１F·２F\x01",      # 3
            "T0131  酒馆、厨房、２F\x01",                       # 4
            "T0700  洛连特飞艇坪(赛希莉亚号停泊中)\x01",        # 5
            "E0810  空中盒子（有空心墙）\x01",                  # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30D0"),
        (1, "loc_30DC"),
        (2, "loc_30E8"),
        (3, "loc_30F4"),
        (4, "loc_3100"),
        (5, "loc_310C"),
        (6, "loc_3118"),
        (SWITCH_DEFAULT, "loc_3124"),
    )


    label("loc_30D0")

    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_30DC")

    NewScene("ED6_DT21/T0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_30E8")

    NewScene("ED6_DT21/T0120   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_30F4")

    NewScene("ED6_DT21/T0121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_3100")

    NewScene("ED6_DT21/T0131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_310C")

    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_3118")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3131")

    label("loc_3124")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3131")

    label("loc_3131")

    Jump("loc_2FBD")

    label("loc_3134")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_2FA8 end

    def Function_38_3144(): pass

    label("Function_38_3144")


    AnonymousTalk(    #37
        "\x06哪里？\x02",
    )

    Jump("loc_3159")

    label("loc_3159")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B0")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_3184")

    label("loc_3184")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3194"),
        (SWITCH_DEFAULT, "loc_31A0"),
    )


    label("loc_3194")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_31AD")

    label("loc_31A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31AD")

    label("loc_31AD")

    Jump("loc_3159")

    label("loc_31B0")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_3144 end

    def Function_39_31C0(): pass

    label("Function_39_31C0")


    AnonymousTalk(    #38
        "\x06哪里？\x02",
    )

    Jump("loc_31D5")

    label("loc_31D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_322C")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_3200")

    label("loc_3200")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3210"),
        (SWITCH_DEFAULT, "loc_321C"),
    )


    label("loc_3210")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3229")

    label("loc_321C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3229")

    label("loc_3229")

    Jump("loc_31D5")

    label("loc_322C")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_31C0 end

    def Function_40_323C(): pass

    label("Function_40_323C")


    AnonymousTalk(    #39
        "\x06哪里？\x02",
    )

    Jump("loc_3251")

    label("loc_3251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32A8")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_327C")

    label("loc_327C")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_328C"),
        (SWITCH_DEFAULT, "loc_3298"),
    )


    label("loc_328C")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_32A5")

    label("loc_3298")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32A5")

    label("loc_32A5")

    Jump("loc_3251")

    label("loc_32A8")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_323C end

    def Function_41_32B8(): pass

    label("Function_41_32B8")


    AnonymousTalk(    #40
        "\x06哪里？\x02",
    )

    Jump("loc_32CD")

    label("loc_32CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3324")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_32F8")

    label("loc_32F8")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3308"),
        (SWITCH_DEFAULT, "loc_3314"),
    )


    label("loc_3308")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3321")

    label("loc_3314")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3321")

    label("loc_3321")

    Jump("loc_32CD")

    label("loc_3324")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_32B8 end

    def Function_42_3334(): pass

    label("Function_42_3334")


    AnonymousTalk(    #41
        "\x06哪里？\x02",
    )

    Jump("loc_3349")

    label("loc_3349")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A0")

    Menu(
        4,
        -1,
        -1,
        1,
        "？？？？\x01",
    )

    Jump("loc_3374")

    label("loc_3374")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3384"),
        (SWITCH_DEFAULT, "loc_3390"),
    )


    label("loc_3384")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_339D")

    label("loc_3390")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_339D")

    label("loc_339D")

    Jump("loc_3349")

    label("loc_33A0")

    OP_5F(0x4)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_3334 end

    def Function_43_33B0(): pass

    label("Function_43_33B0")

    OP_28(0x1, 0x4, 0x4)
    OP_28(0x1, 0x4, 0x2)
    OP_28(0x1, 0x4, 0x8)
    OP_28(0x1, 0x4, 0x10)
    OP_28(0x1, 0x4, 0x20)
    OP_28(0x1, 0x1, 0x1)
    OP_28(0x1, 0x1, 0x2)
    OP_28(0x1, 0x1, 0x4)
    OP_28(0x1, 0x1, 0x8)
    OP_28(0x1, 0x1, 0x10)
    OP_28(0x1, 0x1, 0x20)
    OP_28(0x1, 0x1, 0x40)
    OP_28(0x1, 0x1, 0x80)
    OP_28(0x1, 0x1, 0x100)
    OP_28(0x1, 0x1, 0x200)
    OP_28(0x1, 0x1, 0x400)
    OP_28(0x1, 0x1, 0x800)
    OP_28(0x1, 0x1, 0x1000)
    OP_28(0x1, 0x1, 0x2000)
    OP_28(0x1, 0x1, 0x4000)
    OP_28(0x1, 0x1, 0x8000)
    OP_28(0x2, 0x4, 0x4)
    OP_28(0x2, 0x4, 0x2)
    OP_28(0x2, 0x4, 0x8)
    OP_28(0x2, 0x4, 0x10)
    OP_28(0x2, 0x4, 0x20)
    OP_28(0x2, 0x1, 0x1)
    OP_28(0x2, 0x1, 0x2)
    OP_28(0x2, 0x1, 0x4)
    OP_28(0x2, 0x1, 0x8)
    OP_28(0x2, 0x1, 0x10)
    OP_28(0x2, 0x1, 0x20)
    OP_28(0x2, 0x1, 0x40)
    OP_28(0x2, 0x1, 0x80)
    OP_28(0x2, 0x1, 0x100)
    OP_28(0x2, 0x1, 0x200)
    OP_28(0x2, 0x1, 0x400)
    OP_28(0x2, 0x1, 0x800)
    OP_28(0x2, 0x1, 0x1000)
    OP_28(0x2, 0x1, 0x2000)
    OP_28(0x2, 0x1, 0x4000)
    OP_28(0x2, 0x1, 0x8000)
    OP_28(0x3, 0x4, 0x4)
    OP_28(0x3, 0x4, 0x2)
    OP_28(0x3, 0x4, 0x8)
    OP_28(0x3, 0x4, 0x10)
    OP_28(0x3, 0x4, 0x20)
    OP_28(0x3, 0x1, 0x1)
    OP_28(0x3, 0x1, 0x2)
    OP_28(0x3, 0x1, 0x4)
    OP_28(0x3, 0x1, 0x8)
    OP_28(0x3, 0x1, 0x10)
    OP_28(0x3, 0x1, 0x20)
    OP_28(0x3, 0x1, 0x40)
    OP_28(0x3, 0x1, 0x80)
    OP_28(0x3, 0x1, 0x100)
    OP_28(0x3, 0x1, 0x200)
    OP_28(0x3, 0x1, 0x400)
    OP_28(0x3, 0x1, 0x800)
    OP_28(0x3, 0x1, 0x1000)
    OP_28(0x3, 0x1, 0x2000)
    OP_28(0x3, 0x1, 0x4000)
    OP_28(0x3, 0x1, 0x8000)
    OP_28(0x4, 0x4, 0x4)
    OP_28(0x4, 0x4, 0x2)
    OP_28(0x4, 0x4, 0x8)
    OP_28(0x4, 0x4, 0x10)
    OP_28(0x4, 0x4, 0x20)
    OP_28(0x4, 0x1, 0x1)
    OP_28(0x4, 0x1, 0x2)
    OP_28(0x4, 0x1, 0x4)
    OP_28(0x4, 0x1, 0x8)
    OP_28(0x4, 0x1, 0x10)
    OP_28(0x4, 0x1, 0x20)
    OP_28(0x4, 0x1, 0x40)
    OP_28(0x4, 0x1, 0x80)
    OP_28(0x4, 0x1, 0x100)
    OP_28(0x4, 0x1, 0x200)
    OP_28(0x4, 0x1, 0x400)
    OP_28(0x4, 0x1, 0x800)
    OP_28(0x4, 0x1, 0x1000)
    OP_28(0x4, 0x1, 0x2000)
    OP_28(0x4, 0x1, 0x4000)
    OP_28(0x4, 0x1, 0x8000)
    OP_28(0x5, 0x4, 0x4)
    OP_28(0x5, 0x4, 0x2)
    OP_28(0x5, 0x4, 0x8)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x20)
    OP_28(0x5, 0x1, 0x1)
    OP_28(0x5, 0x1, 0x2)
    OP_28(0x5, 0x1, 0x4)
    OP_28(0x5, 0x1, 0x8)
    OP_28(0x5, 0x1, 0x10)
    OP_28(0x5, 0x1, 0x20)
    OP_28(0x5, 0x1, 0x40)
    OP_28(0x5, 0x1, 0x80)
    OP_28(0x5, 0x1, 0x100)
    OP_28(0x5, 0x1, 0x200)
    OP_28(0x5, 0x1, 0x400)
    OP_28(0x5, 0x1, 0x800)
    OP_28(0x5, 0x1, 0x1000)
    OP_28(0x5, 0x1, 0x2000)
    OP_28(0x5, 0x1, 0x4000)
    OP_28(0x5, 0x1, 0x8000)
    OP_28(0x6, 0x4, 0x4)
    OP_28(0x6, 0x4, 0x2)
    OP_28(0x6, 0x4, 0x8)
    OP_28(0x6, 0x4, 0x10)
    OP_28(0x6, 0x4, 0x20)
    OP_28(0x6, 0x1, 0x1)
    OP_28(0x6, 0x1, 0x2)
    OP_28(0x6, 0x1, 0x4)
    OP_28(0x6, 0x1, 0x8)
    OP_28(0x6, 0x1, 0x10)
    OP_28(0x6, 0x1, 0x20)
    OP_28(0x6, 0x1, 0x40)
    OP_28(0x6, 0x1, 0x80)
    OP_28(0x6, 0x1, 0x100)
    OP_28(0x6, 0x1, 0x200)
    OP_28(0x6, 0x1, 0x400)
    OP_28(0x6, 0x1, 0x800)
    OP_28(0x6, 0x1, 0x1000)
    OP_28(0x6, 0x1, 0x2000)
    OP_28(0x6, 0x1, 0x4000)
    OP_28(0x6, 0x1, 0x8000)
    OP_28(0x7, 0x4, 0x4)
    OP_28(0x7, 0x4, 0x2)
    OP_28(0x7, 0x4, 0x8)
    OP_28(0x7, 0x4, 0x10)
    OP_28(0x7, 0x4, 0x20)
    OP_28(0x7, 0x1, 0x1)
    OP_28(0x7, 0x1, 0x2)
    OP_28(0x7, 0x1, 0x4)
    OP_28(0x7, 0x1, 0x8)
    OP_28(0x7, 0x1, 0x10)
    OP_28(0x7, 0x1, 0x20)
    OP_28(0x7, 0x1, 0x40)
    OP_28(0x7, 0x1, 0x80)
    OP_28(0x7, 0x1, 0x100)
    OP_28(0x7, 0x1, 0x200)
    OP_28(0x7, 0x1, 0x400)
    OP_28(0x7, 0x1, 0x800)
    OP_28(0x7, 0x1, 0x1000)
    OP_28(0x7, 0x1, 0x2000)
    OP_28(0x7, 0x1, 0x4000)
    OP_28(0x7, 0x1, 0x8000)
    OP_28(0x8, 0x4, 0x4)
    OP_28(0x8, 0x4, 0x2)
    OP_28(0x8, 0x4, 0x8)
    OP_28(0x8, 0x4, 0x10)
    OP_28(0x8, 0x4, 0x20)
    OP_28(0x8, 0x1, 0x1)
    OP_28(0x8, 0x1, 0x2)
    OP_28(0x8, 0x1, 0x4)
    OP_28(0x8, 0x1, 0x8)
    OP_28(0x8, 0x1, 0x10)
    OP_28(0x8, 0x1, 0x20)
    OP_28(0x8, 0x1, 0x40)
    OP_28(0x8, 0x1, 0x80)
    OP_28(0x8, 0x1, 0x100)
    OP_28(0x8, 0x1, 0x200)
    OP_28(0x8, 0x1, 0x400)
    OP_28(0x8, 0x1, 0x800)
    OP_28(0x8, 0x1, 0x1000)
    OP_28(0x8, 0x1, 0x2000)
    OP_28(0x8, 0x1, 0x4000)
    OP_28(0x8, 0x1, 0x8000)
    OP_28(0x9, 0x4, 0x4)
    OP_28(0x9, 0x4, 0x2)
    OP_28(0x9, 0x4, 0x8)
    OP_28(0x9, 0x4, 0x10)
    OP_28(0x9, 0x4, 0x20)
    OP_28(0x9, 0x1, 0x1)
    OP_28(0x9, 0x1, 0x2)
    OP_28(0x9, 0x1, 0x4)
    OP_28(0x9, 0x1, 0x8)
    OP_28(0x9, 0x1, 0x10)
    OP_28(0x9, 0x1, 0x20)
    OP_28(0x9, 0x1, 0x40)
    OP_28(0x9, 0x1, 0x80)
    OP_28(0x9, 0x1, 0x100)
    OP_28(0x9, 0x1, 0x200)
    OP_28(0x9, 0x1, 0x400)
    OP_28(0x9, 0x1, 0x800)
    OP_28(0x9, 0x1, 0x1000)
    OP_28(0x9, 0x1, 0x2000)
    OP_28(0x9, 0x1, 0x4000)
    OP_28(0x9, 0x1, 0x8000)
    OP_28(0xA, 0x4, 0x4)
    OP_28(0xA, 0x4, 0x2)
    OP_28(0xA, 0x4, 0x8)
    OP_28(0xA, 0x4, 0x10)
    OP_28(0xA, 0x4, 0x20)
    OP_28(0xA, 0x1, 0x1)
    OP_28(0xA, 0x1, 0x2)
    OP_28(0xA, 0x1, 0x4)
    OP_28(0xA, 0x1, 0x8)
    OP_28(0xA, 0x1, 0x10)
    OP_28(0xA, 0x1, 0x20)
    OP_28(0xA, 0x1, 0x40)
    OP_28(0xA, 0x1, 0x80)
    OP_28(0xA, 0x1, 0x100)
    OP_28(0xA, 0x1, 0x200)
    OP_28(0xA, 0x1, 0x400)
    OP_28(0xA, 0x1, 0x800)
    OP_28(0xA, 0x1, 0x1000)
    OP_28(0xA, 0x1, 0x2000)
    OP_28(0xA, 0x1, 0x4000)
    OP_28(0xA, 0x1, 0x8000)
    OP_28(0xB, 0x4, 0x4)
    OP_28(0xB, 0x4, 0x2)
    OP_28(0xB, 0x4, 0x8)
    OP_28(0xB, 0x4, 0x10)
    OP_28(0xB, 0x4, 0x20)
    OP_28(0xB, 0x1, 0x1)
    OP_28(0xB, 0x1, 0x2)
    OP_28(0xB, 0x1, 0x4)
    OP_28(0xB, 0x1, 0x8)
    OP_28(0xB, 0x1, 0x10)
    OP_28(0xB, 0x1, 0x20)
    OP_28(0xB, 0x1, 0x40)
    OP_28(0xB, 0x1, 0x80)
    OP_28(0xB, 0x1, 0x100)
    OP_28(0xB, 0x1, 0x200)
    OP_28(0xB, 0x1, 0x400)
    OP_28(0xB, 0x1, 0x800)
    OP_28(0xB, 0x1, 0x1000)
    OP_28(0xB, 0x1, 0x2000)
    OP_28(0xB, 0x1, 0x4000)
    OP_28(0xB, 0x1, 0x8000)
    OP_28(0xC, 0x4, 0x4)
    OP_28(0xC, 0x4, 0x2)
    OP_28(0xC, 0x4, 0x8)
    OP_28(0xC, 0x4, 0x10)
    OP_28(0xC, 0x4, 0x20)
    OP_28(0xC, 0x1, 0x1)
    OP_28(0xC, 0x1, 0x2)
    OP_28(0xC, 0x1, 0x4)
    OP_28(0xC, 0x1, 0x8)
    OP_28(0xC, 0x1, 0x10)
    OP_28(0xC, 0x1, 0x20)
    OP_28(0xC, 0x1, 0x40)
    OP_28(0xC, 0x1, 0x80)
    OP_28(0xC, 0x1, 0x100)
    OP_28(0xC, 0x1, 0x200)
    OP_28(0xC, 0x1, 0x400)
    OP_28(0xC, 0x1, 0x800)
    OP_28(0xC, 0x1, 0x1000)
    OP_28(0xC, 0x1, 0x2000)
    OP_28(0xC, 0x1, 0x4000)
    OP_28(0xC, 0x1, 0x8000)
    OP_28(0xD, 0x4, 0x4)
    OP_28(0xD, 0x4, 0x2)
    OP_28(0xD, 0x4, 0x8)
    OP_28(0xD, 0x4, 0x10)
    OP_28(0xD, 0x4, 0x20)
    OP_28(0xD, 0x1, 0x1)
    OP_28(0xD, 0x1, 0x2)
    OP_28(0xD, 0x1, 0x4)
    OP_28(0xD, 0x1, 0x8)
    OP_28(0xD, 0x1, 0x10)
    OP_28(0xD, 0x1, 0x20)
    OP_28(0xD, 0x1, 0x40)
    OP_28(0xD, 0x1, 0x80)
    OP_28(0xD, 0x1, 0x100)
    OP_28(0xD, 0x1, 0x200)
    OP_28(0xD, 0x1, 0x400)
    OP_28(0xD, 0x1, 0x800)
    OP_28(0xD, 0x1, 0x1000)
    OP_28(0xD, 0x1, 0x2000)
    OP_28(0xD, 0x1, 0x4000)
    OP_28(0xD, 0x1, 0x8000)
    OP_28(0xE, 0x4, 0x4)
    OP_28(0xE, 0x4, 0x2)
    OP_28(0xE, 0x4, 0x8)
    OP_28(0xE, 0x4, 0x10)
    OP_28(0xE, 0x4, 0x20)
    OP_28(0xE, 0x1, 0x1)
    OP_28(0xE, 0x1, 0x2)
    OP_28(0xE, 0x1, 0x4)
    OP_28(0xE, 0x1, 0x8)
    OP_28(0xE, 0x1, 0x10)
    OP_28(0xE, 0x1, 0x20)
    OP_28(0xE, 0x1, 0x40)
    OP_28(0xE, 0x1, 0x80)
    OP_28(0xE, 0x1, 0x100)
    OP_28(0xE, 0x1, 0x200)
    OP_28(0xE, 0x1, 0x400)
    OP_28(0xE, 0x1, 0x800)
    OP_28(0xE, 0x1, 0x1000)
    OP_28(0xE, 0x1, 0x2000)
    OP_28(0xE, 0x1, 0x4000)
    OP_28(0xE, 0x1, 0x8000)
    OP_28(0xF, 0x4, 0x4)
    OP_28(0xF, 0x4, 0x2)
    OP_28(0xF, 0x4, 0x8)
    OP_28(0xF, 0x4, 0x10)
    OP_28(0xF, 0x4, 0x20)
    OP_28(0xF, 0x1, 0x1)
    OP_28(0xF, 0x1, 0x2)
    OP_28(0xF, 0x1, 0x4)
    OP_28(0xF, 0x1, 0x8)
    OP_28(0xF, 0x1, 0x10)
    OP_28(0xF, 0x1, 0x20)
    OP_28(0xF, 0x1, 0x40)
    OP_28(0xF, 0x1, 0x80)
    OP_28(0xF, 0x1, 0x100)
    OP_28(0xF, 0x1, 0x200)
    OP_28(0xF, 0x1, 0x400)
    OP_28(0xF, 0x1, 0x800)
    OP_28(0xF, 0x1, 0x1000)
    OP_28(0xF, 0x1, 0x2000)
    OP_28(0xF, 0x1, 0x4000)
    OP_28(0xF, 0x1, 0x8000)
    OP_28(0x12, 0x4, 0x4)
    OP_28(0x12, 0x4, 0x2)
    OP_28(0x12, 0x4, 0x8)
    OP_28(0x12, 0x4, 0x10)
    OP_28(0x12, 0x4, 0x20)
    OP_28(0x12, 0x1, 0x1)
    OP_28(0x12, 0x1, 0x2)
    OP_28(0x12, 0x1, 0x4)
    OP_28(0x12, 0x1, 0x8)
    OP_28(0x12, 0x1, 0x10)
    OP_28(0x12, 0x1, 0x20)
    OP_28(0x12, 0x1, 0x40)
    OP_28(0x12, 0x1, 0x80)
    OP_28(0x12, 0x1, 0x100)
    OP_28(0x12, 0x1, 0x200)
    OP_28(0x12, 0x1, 0x400)
    OP_28(0x12, 0x1, 0x800)
    OP_28(0x12, 0x1, 0x1000)
    OP_28(0x12, 0x1, 0x2000)
    OP_28(0x12, 0x1, 0x4000)
    OP_28(0x12, 0x1, 0x8000)
    OP_28(0x13, 0x4, 0x4)
    OP_28(0x13, 0x4, 0x2)
    OP_28(0x13, 0x4, 0x8)
    OP_28(0x13, 0x4, 0x10)
    OP_28(0x13, 0x4, 0x20)
    OP_28(0x13, 0x1, 0x1)
    OP_28(0x13, 0x1, 0x2)
    OP_28(0x13, 0x1, 0x4)
    OP_28(0x13, 0x1, 0x8)
    OP_28(0x13, 0x1, 0x10)
    OP_28(0x13, 0x1, 0x20)
    OP_28(0x13, 0x1, 0x40)
    OP_28(0x13, 0x1, 0x80)
    OP_28(0x13, 0x1, 0x100)
    OP_28(0x13, 0x1, 0x200)
    OP_28(0x13, 0x1, 0x400)
    OP_28(0x13, 0x1, 0x800)
    OP_28(0x13, 0x1, 0x1000)
    OP_28(0x13, 0x1, 0x2000)
    OP_28(0x13, 0x1, 0x4000)
    OP_28(0x13, 0x1, 0x8000)
    OP_28(0x14, 0x4, 0x4)
    OP_28(0x14, 0x4, 0x2)
    OP_28(0x14, 0x4, 0x8)
    OP_28(0x14, 0x4, 0x10)
    OP_28(0x14, 0x4, 0x20)
    OP_28(0x14, 0x1, 0x1)
    OP_28(0x14, 0x1, 0x2)
    OP_28(0x14, 0x1, 0x4)
    OP_28(0x14, 0x1, 0x8)
    OP_28(0x14, 0x1, 0x10)
    OP_28(0x14, 0x1, 0x20)
    OP_28(0x14, 0x1, 0x40)
    OP_28(0x14, 0x1, 0x80)
    OP_28(0x14, 0x1, 0x100)
    OP_28(0x14, 0x1, 0x200)
    OP_28(0x14, 0x1, 0x400)
    OP_28(0x14, 0x1, 0x800)
    OP_28(0x14, 0x1, 0x1000)
    OP_28(0x14, 0x1, 0x2000)
    OP_28(0x14, 0x1, 0x4000)
    OP_28(0x14, 0x1, 0x8000)
    OP_28(0x15, 0x4, 0x4)
    OP_28(0x15, 0x4, 0x2)
    OP_28(0x15, 0x4, 0x8)
    OP_28(0x15, 0x4, 0x10)
    OP_28(0x15, 0x4, 0x20)
    OP_28(0x15, 0x1, 0x1)
    OP_28(0x15, 0x1, 0x2)
    OP_28(0x15, 0x1, 0x4)
    OP_28(0x15, 0x1, 0x8)
    OP_28(0x15, 0x1, 0x10)
    OP_28(0x15, 0x1, 0x20)
    OP_28(0x15, 0x1, 0x40)
    OP_28(0x15, 0x1, 0x80)
    OP_28(0x15, 0x1, 0x100)
    OP_28(0x15, 0x1, 0x200)
    OP_28(0x15, 0x1, 0x400)
    OP_28(0x15, 0x1, 0x800)
    OP_28(0x15, 0x1, 0x1000)
    OP_28(0x15, 0x1, 0x2000)
    OP_28(0x15, 0x1, 0x4000)
    OP_28(0x15, 0x1, 0x8000)
    OP_28(0x16, 0x4, 0x4)
    OP_28(0x16, 0x4, 0x2)
    OP_28(0x16, 0x4, 0x8)
    OP_28(0x16, 0x4, 0x10)
    OP_28(0x16, 0x4, 0x20)
    OP_28(0x16, 0x1, 0x1)
    OP_28(0x16, 0x1, 0x2)
    OP_28(0x16, 0x1, 0x4)
    OP_28(0x16, 0x1, 0x8)
    OP_28(0x16, 0x1, 0x10)
    OP_28(0x16, 0x1, 0x20)
    OP_28(0x16, 0x1, 0x40)
    OP_28(0x16, 0x1, 0x80)
    OP_28(0x16, 0x1, 0x100)
    OP_28(0x16, 0x1, 0x200)
    OP_28(0x16, 0x1, 0x400)
    OP_28(0x16, 0x1, 0x800)
    OP_28(0x16, 0x1, 0x1000)
    OP_28(0x16, 0x1, 0x2000)
    OP_28(0x16, 0x1, 0x4000)
    OP_28(0x16, 0x1, 0x8000)
    OP_28(0x17, 0x4, 0x4)
    OP_28(0x17, 0x4, 0x2)
    OP_28(0x17, 0x4, 0x8)
    OP_28(0x17, 0x4, 0x10)
    OP_28(0x17, 0x4, 0x20)
    OP_28(0x17, 0x1, 0x1)
    OP_28(0x17, 0x1, 0x2)
    OP_28(0x17, 0x1, 0x4)
    OP_28(0x17, 0x1, 0x8)
    OP_28(0x17, 0x1, 0x10)
    OP_28(0x17, 0x1, 0x20)
    OP_28(0x17, 0x1, 0x40)
    OP_28(0x17, 0x1, 0x80)
    OP_28(0x17, 0x1, 0x100)
    OP_28(0x17, 0x1, 0x200)
    OP_28(0x17, 0x1, 0x400)
    OP_28(0x17, 0x1, 0x800)
    OP_28(0x17, 0x1, 0x1000)
    OP_28(0x17, 0x1, 0x2000)
    OP_28(0x17, 0x1, 0x4000)
    OP_28(0x17, 0x1, 0x8000)
    OP_28(0x19, 0x4, 0x4)
    OP_28(0x19, 0x4, 0x2)
    OP_28(0x19, 0x4, 0x8)
    OP_28(0x19, 0x4, 0x10)
    OP_28(0x19, 0x4, 0x20)
    OP_28(0x19, 0x1, 0x1)
    OP_28(0x19, 0x1, 0x2)
    OP_28(0x19, 0x1, 0x4)
    OP_28(0x19, 0x1, 0x8)
    OP_28(0x19, 0x1, 0x10)
    OP_28(0x19, 0x1, 0x20)
    OP_28(0x19, 0x1, 0x40)
    OP_28(0x19, 0x1, 0x80)
    OP_28(0x19, 0x1, 0x100)
    OP_28(0x19, 0x1, 0x200)
    OP_28(0x19, 0x1, 0x400)
    OP_28(0x19, 0x1, 0x800)
    OP_28(0x19, 0x1, 0x1000)
    OP_28(0x19, 0x1, 0x2000)
    OP_28(0x19, 0x1, 0x4000)
    OP_28(0x19, 0x1, 0x8000)
    OP_28(0x1A, 0x4, 0x4)
    OP_28(0x1A, 0x4, 0x2)
    OP_28(0x1A, 0x4, 0x8)
    OP_28(0x1A, 0x4, 0x10)
    OP_28(0x1A, 0x4, 0x20)
    OP_28(0x1A, 0x1, 0x1)
    OP_28(0x1A, 0x1, 0x2)
    OP_28(0x1A, 0x1, 0x4)
    OP_28(0x1A, 0x1, 0x8)
    OP_28(0x1A, 0x1, 0x10)
    OP_28(0x1A, 0x1, 0x20)
    OP_28(0x1A, 0x1, 0x40)
    OP_28(0x1A, 0x1, 0x80)
    OP_28(0x1A, 0x1, 0x100)
    OP_28(0x1A, 0x1, 0x200)
    OP_28(0x1A, 0x1, 0x400)
    OP_28(0x1A, 0x1, 0x800)
    OP_28(0x1A, 0x1, 0x1000)
    OP_28(0x1A, 0x1, 0x2000)
    OP_28(0x1A, 0x1, 0x4000)
    OP_28(0x1A, 0x1, 0x8000)
    OP_28(0x1B, 0x4, 0x4)
    OP_28(0x1B, 0x4, 0x2)
    OP_28(0x1B, 0x4, 0x8)
    OP_28(0x1B, 0x4, 0x10)
    OP_28(0x1B, 0x4, 0x20)
    OP_28(0x1B, 0x1, 0x1)
    OP_28(0x1B, 0x1, 0x2)
    OP_28(0x1B, 0x1, 0x4)
    OP_28(0x1B, 0x1, 0x8)
    OP_28(0x1B, 0x1, 0x10)
    OP_28(0x1B, 0x1, 0x20)
    OP_28(0x1B, 0x1, 0x40)
    OP_28(0x1B, 0x1, 0x80)
    OP_28(0x1B, 0x1, 0x100)
    OP_28(0x1B, 0x1, 0x200)
    OP_28(0x1B, 0x1, 0x400)
    OP_28(0x1B, 0x1, 0x800)
    OP_28(0x1B, 0x1, 0x1000)
    OP_28(0x1B, 0x1, 0x2000)
    OP_28(0x1B, 0x1, 0x4000)
    OP_28(0x1B, 0x1, 0x8000)
    OP_28(0x1C, 0x4, 0x4)
    OP_28(0x1C, 0x4, 0x2)
    OP_28(0x1C, 0x4, 0x8)
    OP_28(0x1C, 0x4, 0x10)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1C, 0x1, 0x1)
    OP_28(0x1C, 0x1, 0x2)
    OP_28(0x1C, 0x1, 0x4)
    OP_28(0x1C, 0x1, 0x8)
    OP_28(0x1C, 0x1, 0x10)
    OP_28(0x1C, 0x1, 0x20)
    OP_28(0x1C, 0x1, 0x40)
    OP_28(0x1C, 0x1, 0x80)
    OP_28(0x1C, 0x1, 0x100)
    OP_28(0x1C, 0x1, 0x200)
    OP_28(0x1C, 0x1, 0x400)
    OP_28(0x1C, 0x1, 0x800)
    OP_28(0x1C, 0x1, 0x1000)
    OP_28(0x1C, 0x1, 0x2000)
    OP_28(0x1C, 0x1, 0x4000)
    OP_28(0x1C, 0x1, 0x8000)
    OP_28(0x1D, 0x4, 0x4)
    OP_28(0x1D, 0x4, 0x2)
    OP_28(0x1D, 0x4, 0x8)
    OP_28(0x1D, 0x4, 0x10)
    OP_28(0x1D, 0x4, 0x20)
    OP_28(0x1D, 0x1, 0x1)
    OP_28(0x1D, 0x1, 0x2)
    OP_28(0x1D, 0x1, 0x4)
    OP_28(0x1D, 0x1, 0x8)
    OP_28(0x1D, 0x1, 0x10)
    OP_28(0x1D, 0x1, 0x20)
    OP_28(0x1D, 0x1, 0x40)
    OP_28(0x1D, 0x1, 0x80)
    OP_28(0x1D, 0x1, 0x100)
    OP_28(0x1D, 0x1, 0x200)
    OP_28(0x1D, 0x1, 0x400)
    OP_28(0x1D, 0x1, 0x800)
    OP_28(0x1D, 0x1, 0x1000)
    OP_28(0x1D, 0x1, 0x2000)
    OP_28(0x1D, 0x1, 0x4000)
    OP_28(0x1D, 0x1, 0x8000)
    OP_28(0x1E, 0x4, 0x4)
    OP_28(0x1E, 0x4, 0x2)
    OP_28(0x1E, 0x4, 0x8)
    OP_28(0x1E, 0x4, 0x10)
    OP_28(0x1E, 0x4, 0x20)
    OP_28(0x1E, 0x1, 0x1)
    OP_28(0x1E, 0x1, 0x2)
    OP_28(0x1E, 0x1, 0x4)
    OP_28(0x1E, 0x1, 0x8)
    OP_28(0x1E, 0x1, 0x10)
    OP_28(0x1E, 0x1, 0x20)
    OP_28(0x1E, 0x1, 0x40)
    OP_28(0x1E, 0x1, 0x80)
    OP_28(0x1E, 0x1, 0x100)
    OP_28(0x1E, 0x1, 0x200)
    OP_28(0x1E, 0x1, 0x400)
    OP_28(0x1E, 0x1, 0x800)
    OP_28(0x1E, 0x1, 0x1000)
    OP_28(0x1E, 0x1, 0x2000)
    OP_28(0x1E, 0x1, 0x4000)
    OP_28(0x1E, 0x1, 0x8000)
    OP_28(0x1F, 0x4, 0x4)
    OP_28(0x1F, 0x4, 0x2)
    OP_28(0x1F, 0x4, 0x8)
    OP_28(0x1F, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x20)
    OP_28(0x1F, 0x1, 0x1)
    OP_28(0x1F, 0x1, 0x2)
    OP_28(0x1F, 0x1, 0x4)
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)
    OP_28(0x1F, 0x1, 0x20)
    OP_28(0x1F, 0x1, 0x40)
    OP_28(0x1F, 0x1, 0x80)
    OP_28(0x1F, 0x1, 0x100)
    OP_28(0x1F, 0x1, 0x200)
    OP_28(0x1F, 0x1, 0x400)
    OP_28(0x1F, 0x1, 0x800)
    OP_28(0x1F, 0x1, 0x1000)
    OP_28(0x1F, 0x1, 0x2000)
    OP_28(0x1F, 0x1, 0x4000)
    OP_28(0x1F, 0x1, 0x8000)
    OP_28(0x20, 0x4, 0x4)
    OP_28(0x20, 0x4, 0x2)
    OP_28(0x20, 0x4, 0x8)
    OP_28(0x20, 0x4, 0x10)
    OP_28(0x20, 0x4, 0x20)
    OP_28(0x20, 0x1, 0x1)
    OP_28(0x20, 0x1, 0x2)
    OP_28(0x20, 0x1, 0x4)
    OP_28(0x20, 0x1, 0x8)
    OP_28(0x20, 0x1, 0x10)
    OP_28(0x20, 0x1, 0x20)
    OP_28(0x20, 0x1, 0x40)
    OP_28(0x20, 0x1, 0x80)
    OP_28(0x20, 0x1, 0x100)
    OP_28(0x20, 0x1, 0x200)
    OP_28(0x20, 0x1, 0x400)
    OP_28(0x20, 0x1, 0x800)
    OP_28(0x20, 0x1, 0x1000)
    OP_28(0x20, 0x1, 0x2000)
    OP_28(0x20, 0x1, 0x4000)
    OP_28(0x20, 0x1, 0x8000)
    OP_28(0x21, 0x4, 0x4)
    OP_28(0x21, 0x4, 0x2)
    OP_28(0x21, 0x4, 0x8)
    OP_28(0x21, 0x4, 0x10)
    OP_28(0x21, 0x4, 0x20)
    OP_28(0x21, 0x1, 0x1)
    OP_28(0x21, 0x1, 0x2)
    OP_28(0x21, 0x1, 0x4)
    OP_28(0x21, 0x1, 0x8)
    OP_28(0x21, 0x1, 0x10)
    OP_28(0x21, 0x1, 0x20)
    OP_28(0x21, 0x1, 0x40)
    OP_28(0x21, 0x1, 0x80)
    OP_28(0x21, 0x1, 0x100)
    OP_28(0x21, 0x1, 0x200)
    OP_28(0x21, 0x1, 0x400)
    OP_28(0x21, 0x1, 0x800)
    OP_28(0x21, 0x1, 0x1000)
    OP_28(0x21, 0x1, 0x2000)
    OP_28(0x21, 0x1, 0x4000)
    OP_28(0x21, 0x1, 0x8000)
    OP_28(0x22, 0x4, 0x4)
    OP_28(0x22, 0x4, 0x2)
    OP_28(0x22, 0x4, 0x8)
    OP_28(0x22, 0x4, 0x10)
    OP_28(0x22, 0x4, 0x20)
    OP_28(0x22, 0x1, 0x1)
    OP_28(0x22, 0x1, 0x2)
    OP_28(0x22, 0x1, 0x4)
    OP_28(0x22, 0x1, 0x8)
    OP_28(0x22, 0x1, 0x10)
    OP_28(0x22, 0x1, 0x20)
    OP_28(0x22, 0x1, 0x40)
    OP_28(0x22, 0x1, 0x80)
    OP_28(0x22, 0x1, 0x100)
    OP_28(0x22, 0x1, 0x200)
    OP_28(0x22, 0x1, 0x400)
    OP_28(0x22, 0x1, 0x800)
    OP_28(0x22, 0x1, 0x1000)
    OP_28(0x22, 0x1, 0x2000)
    OP_28(0x22, 0x1, 0x4000)
    OP_28(0x22, 0x1, 0x8000)
    OP_28(0x23, 0x4, 0x4)
    OP_28(0x23, 0x4, 0x2)
    OP_28(0x23, 0x4, 0x8)
    OP_28(0x23, 0x4, 0x10)
    OP_28(0x23, 0x4, 0x20)
    OP_28(0x23, 0x1, 0x1)
    OP_28(0x23, 0x1, 0x2)
    OP_28(0x23, 0x1, 0x4)
    OP_28(0x23, 0x1, 0x8)
    OP_28(0x23, 0x1, 0x10)
    OP_28(0x23, 0x1, 0x20)
    OP_28(0x23, 0x1, 0x40)
    OP_28(0x23, 0x1, 0x80)
    OP_28(0x23, 0x1, 0x100)
    OP_28(0x23, 0x1, 0x200)
    OP_28(0x23, 0x1, 0x400)
    OP_28(0x23, 0x1, 0x800)
    OP_28(0x23, 0x1, 0x1000)
    OP_28(0x23, 0x1, 0x2000)
    OP_28(0x23, 0x1, 0x4000)
    OP_28(0x23, 0x1, 0x8000)
    OP_28(0x24, 0x4, 0x4)
    OP_28(0x24, 0x4, 0x2)
    OP_28(0x24, 0x4, 0x8)
    OP_28(0x24, 0x4, 0x10)
    OP_28(0x24, 0x4, 0x20)
    OP_28(0x24, 0x1, 0x1)
    OP_28(0x24, 0x1, 0x2)
    OP_28(0x24, 0x1, 0x4)
    OP_28(0x24, 0x1, 0x8)
    OP_28(0x24, 0x1, 0x10)
    OP_28(0x24, 0x1, 0x20)
    OP_28(0x24, 0x1, 0x40)
    OP_28(0x24, 0x1, 0x80)
    OP_28(0x24, 0x1, 0x100)
    OP_28(0x24, 0x1, 0x200)
    OP_28(0x24, 0x1, 0x400)
    OP_28(0x24, 0x1, 0x800)
    OP_28(0x24, 0x1, 0x1000)
    OP_28(0x24, 0x1, 0x2000)
    OP_28(0x24, 0x1, 0x4000)
    OP_28(0x24, 0x1, 0x8000)
    OP_28(0x28, 0x4, 0x4)
    OP_28(0x28, 0x4, 0x2)
    OP_28(0x28, 0x4, 0x8)
    OP_28(0x28, 0x4, 0x10)
    OP_28(0x28, 0x4, 0x20)
    OP_28(0x28, 0x1, 0x1)
    OP_28(0x28, 0x1, 0x2)
    OP_28(0x28, 0x1, 0x4)
    OP_28(0x28, 0x1, 0x8)
    OP_28(0x28, 0x1, 0x10)
    OP_28(0x28, 0x1, 0x20)
    OP_28(0x28, 0x1, 0x40)
    OP_28(0x28, 0x1, 0x80)
    OP_28(0x28, 0x1, 0x100)
    OP_28(0x28, 0x1, 0x200)
    OP_28(0x28, 0x1, 0x400)
    OP_28(0x28, 0x1, 0x800)
    OP_28(0x28, 0x1, 0x1000)
    OP_28(0x28, 0x1, 0x2000)
    OP_28(0x28, 0x1, 0x4000)
    OP_28(0x28, 0x1, 0x8000)
    OP_28(0x29, 0x4, 0x4)
    OP_28(0x29, 0x4, 0x2)
    OP_28(0x29, 0x4, 0x8)
    OP_28(0x29, 0x4, 0x10)
    OP_28(0x29, 0x4, 0x20)
    OP_28(0x29, 0x1, 0x1)
    OP_28(0x29, 0x1, 0x2)
    OP_28(0x29, 0x1, 0x4)
    OP_28(0x29, 0x1, 0x8)
    OP_28(0x29, 0x1, 0x10)
    OP_28(0x29, 0x1, 0x20)
    OP_28(0x29, 0x1, 0x40)
    OP_28(0x29, 0x1, 0x80)
    OP_28(0x29, 0x1, 0x100)
    OP_28(0x29, 0x1, 0x200)
    OP_28(0x29, 0x1, 0x400)
    OP_28(0x29, 0x1, 0x800)
    OP_28(0x29, 0x1, 0x1000)
    OP_28(0x29, 0x1, 0x2000)
    OP_28(0x29, 0x1, 0x4000)
    OP_28(0x29, 0x1, 0x8000)
    OP_28(0x2A, 0x4, 0x4)
    OP_28(0x2A, 0x4, 0x2)
    OP_28(0x2A, 0x4, 0x8)
    OP_28(0x2A, 0x4, 0x10)
    OP_28(0x2A, 0x4, 0x20)
    OP_28(0x2A, 0x1, 0x1)
    OP_28(0x2A, 0x1, 0x2)
    OP_28(0x2A, 0x1, 0x4)
    OP_28(0x2A, 0x1, 0x8)
    OP_28(0x2A, 0x1, 0x10)
    OP_28(0x2A, 0x1, 0x20)
    OP_28(0x2A, 0x1, 0x40)
    OP_28(0x2A, 0x1, 0x80)
    OP_28(0x2A, 0x1, 0x100)
    OP_28(0x2A, 0x1, 0x200)
    OP_28(0x2A, 0x1, 0x400)
    OP_28(0x2A, 0x1, 0x800)
    OP_28(0x2A, 0x1, 0x1000)
    OP_28(0x2A, 0x1, 0x2000)
    OP_28(0x2A, 0x1, 0x4000)
    OP_28(0x2A, 0x1, 0x8000)
    OP_28(0x2B, 0x4, 0x4)
    OP_28(0x2B, 0x4, 0x2)
    OP_28(0x2B, 0x4, 0x8)
    OP_28(0x2B, 0x4, 0x10)
    OP_28(0x2B, 0x4, 0x20)
    OP_28(0x2B, 0x1, 0x1)
    OP_28(0x2B, 0x1, 0x2)
    OP_28(0x2B, 0x1, 0x4)
    OP_28(0x2B, 0x1, 0x8)
    OP_28(0x2B, 0x1, 0x10)
    OP_28(0x2B, 0x1, 0x20)
    OP_28(0x2B, 0x1, 0x40)
    OP_28(0x2B, 0x1, 0x80)
    OP_28(0x2B, 0x1, 0x100)
    OP_28(0x2B, 0x1, 0x200)
    OP_28(0x2B, 0x1, 0x400)
    OP_28(0x2B, 0x1, 0x800)
    OP_28(0x2B, 0x1, 0x1000)
    OP_28(0x2B, 0x1, 0x2000)
    OP_28(0x2B, 0x1, 0x4000)
    OP_28(0x2B, 0x1, 0x8000)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x4, 0x2)
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x4, 0x20)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_28(0x2C, 0x1, 0x4)
    OP_28(0x2C, 0x1, 0x8)
    OP_28(0x2C, 0x1, 0x10)
    OP_28(0x2C, 0x1, 0x20)
    OP_28(0x2C, 0x1, 0x40)
    OP_28(0x2C, 0x1, 0x80)
    OP_28(0x2C, 0x1, 0x100)
    OP_28(0x2C, 0x1, 0x200)
    OP_28(0x2C, 0x1, 0x400)
    OP_28(0x2C, 0x1, 0x800)
    OP_28(0x2C, 0x1, 0x1000)
    OP_28(0x2C, 0x1, 0x2000)
    OP_28(0x2C, 0x1, 0x4000)
    OP_28(0x2C, 0x1, 0x8000)
    OP_28(0x2D, 0x4, 0x4)
    OP_28(0x2D, 0x4, 0x2)
    OP_28(0x2D, 0x4, 0x8)
    OP_28(0x2D, 0x4, 0x10)
    OP_28(0x2D, 0x4, 0x20)
    OP_28(0x2D, 0x1, 0x1)
    OP_28(0x2D, 0x1, 0x2)
    OP_28(0x2D, 0x1, 0x4)
    OP_28(0x2D, 0x1, 0x8)
    OP_28(0x2D, 0x1, 0x10)
    OP_28(0x2D, 0x1, 0x20)
    OP_28(0x2D, 0x1, 0x40)
    OP_28(0x2D, 0x1, 0x80)
    OP_28(0x2D, 0x1, 0x100)
    OP_28(0x2D, 0x1, 0x200)
    OP_28(0x2D, 0x1, 0x400)
    OP_28(0x2D, 0x1, 0x800)
    OP_28(0x2D, 0x1, 0x1000)
    OP_28(0x2D, 0x1, 0x2000)
    OP_28(0x2D, 0x1, 0x4000)
    OP_28(0x2D, 0x1, 0x8000)
    OP_28(0x2E, 0x4, 0x4)
    OP_28(0x2E, 0x4, 0x2)
    OP_28(0x2E, 0x4, 0x8)
    OP_28(0x2E, 0x4, 0x10)
    OP_28(0x2E, 0x4, 0x20)
    OP_28(0x2E, 0x1, 0x1)
    OP_28(0x2E, 0x1, 0x2)
    OP_28(0x2E, 0x1, 0x4)
    OP_28(0x2E, 0x1, 0x8)
    OP_28(0x2E, 0x1, 0x10)
    OP_28(0x2E, 0x1, 0x20)
    OP_28(0x2E, 0x1, 0x40)
    OP_28(0x2E, 0x1, 0x80)
    OP_28(0x2E, 0x1, 0x100)
    OP_28(0x2E, 0x1, 0x200)
    OP_28(0x2E, 0x1, 0x400)
    OP_28(0x2E, 0x1, 0x800)
    OP_28(0x2E, 0x1, 0x1000)
    OP_28(0x2E, 0x1, 0x2000)
    OP_28(0x2E, 0x1, 0x4000)
    OP_28(0x2E, 0x1, 0x8000)
    OP_28(0x2F, 0x4, 0x4)
    OP_28(0x2F, 0x4, 0x2)
    OP_28(0x2F, 0x4, 0x8)
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x4, 0x20)
    OP_28(0x2F, 0x1, 0x1)
    OP_28(0x2F, 0x1, 0x2)
    OP_28(0x2F, 0x1, 0x4)
    OP_28(0x2F, 0x1, 0x8)
    OP_28(0x2F, 0x1, 0x10)
    OP_28(0x2F, 0x1, 0x20)
    OP_28(0x2F, 0x1, 0x40)
    OP_28(0x2F, 0x1, 0x80)
    OP_28(0x2F, 0x1, 0x100)
    OP_28(0x2F, 0x1, 0x200)
    OP_28(0x2F, 0x1, 0x400)
    OP_28(0x2F, 0x1, 0x800)
    OP_28(0x2F, 0x1, 0x1000)
    OP_28(0x2F, 0x1, 0x2000)
    OP_28(0x2F, 0x1, 0x4000)
    OP_28(0x2F, 0x1, 0x8000)
    OP_28(0x30, 0x4, 0x4)
    OP_28(0x30, 0x4, 0x2)
    OP_28(0x30, 0x4, 0x8)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x4, 0x20)
    OP_28(0x30, 0x1, 0x1)
    OP_28(0x30, 0x1, 0x2)
    OP_28(0x30, 0x1, 0x4)
    OP_28(0x30, 0x1, 0x8)
    OP_28(0x30, 0x1, 0x10)
    OP_28(0x30, 0x1, 0x20)
    OP_28(0x30, 0x1, 0x40)
    OP_28(0x30, 0x1, 0x80)
    OP_28(0x30, 0x1, 0x100)
    OP_28(0x30, 0x1, 0x200)
    OP_28(0x30, 0x1, 0x400)
    OP_28(0x30, 0x1, 0x800)
    OP_28(0x30, 0x1, 0x1000)
    OP_28(0x30, 0x1, 0x2000)
    OP_28(0x30, 0x1, 0x4000)
    OP_28(0x30, 0x1, 0x8000)
    OP_28(0x31, 0x4, 0x4)
    OP_28(0x31, 0x4, 0x2)
    OP_28(0x31, 0x4, 0x8)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x4, 0x20)
    OP_28(0x31, 0x1, 0x1)
    OP_28(0x31, 0x1, 0x2)
    OP_28(0x31, 0x1, 0x4)
    OP_28(0x31, 0x1, 0x8)
    OP_28(0x31, 0x1, 0x10)
    OP_28(0x31, 0x1, 0x20)
    OP_28(0x31, 0x1, 0x40)
    OP_28(0x31, 0x1, 0x80)
    OP_28(0x31, 0x1, 0x100)
    OP_28(0x31, 0x1, 0x200)
    OP_28(0x31, 0x1, 0x400)
    OP_28(0x31, 0x1, 0x800)
    OP_28(0x31, 0x1, 0x1000)
    OP_28(0x31, 0x1, 0x2000)
    OP_28(0x31, 0x1, 0x4000)
    OP_28(0x31, 0x1, 0x8000)
    OP_28(0x32, 0x4, 0x4)
    OP_28(0x32, 0x4, 0x2)
    OP_28(0x32, 0x4, 0x8)
    OP_28(0x32, 0x4, 0x10)
    OP_28(0x32, 0x4, 0x20)
    OP_28(0x32, 0x1, 0x1)
    OP_28(0x32, 0x1, 0x2)
    OP_28(0x32, 0x1, 0x4)
    OP_28(0x32, 0x1, 0x8)
    OP_28(0x32, 0x1, 0x10)
    OP_28(0x32, 0x1, 0x20)
    OP_28(0x32, 0x1, 0x40)
    OP_28(0x32, 0x1, 0x80)
    OP_28(0x32, 0x1, 0x100)
    OP_28(0x32, 0x1, 0x200)
    OP_28(0x32, 0x1, 0x400)
    OP_28(0x32, 0x1, 0x800)
    OP_28(0x32, 0x1, 0x1000)
    OP_28(0x32, 0x1, 0x2000)
    OP_28(0x32, 0x1, 0x4000)
    OP_28(0x32, 0x1, 0x8000)
    OP_28(0x33, 0x4, 0x4)
    OP_28(0x33, 0x4, 0x2)
    OP_28(0x33, 0x4, 0x8)
    OP_28(0x33, 0x4, 0x10)
    OP_28(0x33, 0x4, 0x20)
    OP_28(0x33, 0x1, 0x1)
    OP_28(0x33, 0x1, 0x2)
    OP_28(0x33, 0x1, 0x4)
    OP_28(0x33, 0x1, 0x8)
    OP_28(0x33, 0x1, 0x10)
    OP_28(0x33, 0x1, 0x20)
    OP_28(0x33, 0x1, 0x40)
    OP_28(0x33, 0x1, 0x80)
    OP_28(0x33, 0x1, 0x100)
    OP_28(0x33, 0x1, 0x200)
    OP_28(0x33, 0x1, 0x400)
    OP_28(0x33, 0x1, 0x800)
    OP_28(0x33, 0x1, 0x1000)
    OP_28(0x33, 0x1, 0x2000)
    OP_28(0x33, 0x1, 0x4000)
    OP_28(0x33, 0x1, 0x8000)
    OP_28(0x34, 0x4, 0x4)
    OP_28(0x34, 0x4, 0x2)
    OP_28(0x34, 0x4, 0x8)
    OP_28(0x34, 0x4, 0x10)
    OP_28(0x34, 0x4, 0x20)
    OP_28(0x34, 0x1, 0x1)
    OP_28(0x34, 0x1, 0x2)
    OP_28(0x34, 0x1, 0x4)
    OP_28(0x34, 0x1, 0x8)
    OP_28(0x34, 0x1, 0x10)
    OP_28(0x34, 0x1, 0x20)
    OP_28(0x34, 0x1, 0x40)
    OP_28(0x34, 0x1, 0x80)
    OP_28(0x34, 0x1, 0x100)
    OP_28(0x34, 0x1, 0x200)
    OP_28(0x34, 0x1, 0x400)
    OP_28(0x34, 0x1, 0x800)
    OP_28(0x34, 0x1, 0x1000)
    OP_28(0x34, 0x1, 0x2000)
    OP_28(0x34, 0x1, 0x4000)
    OP_28(0x34, 0x1, 0x8000)
    OP_28(0x35, 0x4, 0x4)
    OP_28(0x35, 0x4, 0x2)
    OP_28(0x35, 0x4, 0x8)
    OP_28(0x35, 0x4, 0x10)
    OP_28(0x35, 0x4, 0x20)
    OP_28(0x35, 0x1, 0x1)
    OP_28(0x35, 0x1, 0x2)
    OP_28(0x35, 0x1, 0x4)
    OP_28(0x35, 0x1, 0x8)
    OP_28(0x35, 0x1, 0x10)
    OP_28(0x35, 0x1, 0x20)
    OP_28(0x35, 0x1, 0x40)
    OP_28(0x35, 0x1, 0x80)
    OP_28(0x35, 0x1, 0x100)
    OP_28(0x35, 0x1, 0x200)
    OP_28(0x35, 0x1, 0x400)
    OP_28(0x35, 0x1, 0x800)
    OP_28(0x35, 0x1, 0x1000)
    OP_28(0x35, 0x1, 0x2000)
    OP_28(0x35, 0x1, 0x4000)
    OP_28(0x35, 0x1, 0x8000)
    OP_28(0x36, 0x4, 0x4)
    OP_28(0x36, 0x4, 0x2)
    OP_28(0x36, 0x4, 0x8)
    OP_28(0x36, 0x4, 0x10)
    OP_28(0x36, 0x4, 0x20)
    OP_28(0x36, 0x1, 0x1)
    OP_28(0x36, 0x1, 0x2)
    OP_28(0x36, 0x1, 0x4)
    OP_28(0x36, 0x1, 0x8)
    OP_28(0x36, 0x1, 0x10)
    OP_28(0x36, 0x1, 0x20)
    OP_28(0x36, 0x1, 0x40)
    OP_28(0x36, 0x1, 0x80)
    OP_28(0x36, 0x1, 0x100)
    OP_28(0x36, 0x1, 0x200)
    OP_28(0x36, 0x1, 0x400)
    OP_28(0x36, 0x1, 0x800)
    OP_28(0x36, 0x1, 0x1000)
    OP_28(0x36, 0x1, 0x2000)
    OP_28(0x36, 0x1, 0x4000)
    OP_28(0x36, 0x1, 0x8000)
    OP_28(0x37, 0x4, 0x4)
    OP_28(0x37, 0x4, 0x2)
    OP_28(0x37, 0x4, 0x8)
    OP_28(0x37, 0x4, 0x10)
    OP_28(0x37, 0x4, 0x20)
    OP_28(0x37, 0x1, 0x1)
    OP_28(0x37, 0x1, 0x2)
    OP_28(0x37, 0x1, 0x4)
    OP_28(0x37, 0x1, 0x8)
    OP_28(0x37, 0x1, 0x10)
    OP_28(0x37, 0x1, 0x20)
    OP_28(0x37, 0x1, 0x40)
    OP_28(0x37, 0x1, 0x80)
    OP_28(0x37, 0x1, 0x100)
    OP_28(0x37, 0x1, 0x200)
    OP_28(0x37, 0x1, 0x400)
    OP_28(0x37, 0x1, 0x800)
    OP_28(0x37, 0x1, 0x1000)
    OP_28(0x37, 0x1, 0x2000)
    OP_28(0x37, 0x1, 0x4000)
    OP_28(0x37, 0x1, 0x8000)
    OP_28(0x38, 0x4, 0x4)
    OP_28(0x38, 0x4, 0x2)
    OP_28(0x38, 0x4, 0x8)
    OP_28(0x38, 0x4, 0x10)
    OP_28(0x38, 0x4, 0x20)
    OP_28(0x38, 0x1, 0x1)
    OP_28(0x38, 0x1, 0x2)
    OP_28(0x38, 0x1, 0x4)
    OP_28(0x38, 0x1, 0x8)
    OP_28(0x38, 0x1, 0x10)
    OP_28(0x38, 0x1, 0x20)
    OP_28(0x38, 0x1, 0x40)
    OP_28(0x38, 0x1, 0x80)
    OP_28(0x38, 0x1, 0x100)
    OP_28(0x38, 0x1, 0x200)
    OP_28(0x38, 0x1, 0x400)
    OP_28(0x38, 0x1, 0x800)
    OP_28(0x38, 0x1, 0x1000)
    OP_28(0x38, 0x1, 0x2000)
    OP_28(0x38, 0x1, 0x4000)
    OP_28(0x38, 0x1, 0x8000)
    OP_28(0x39, 0x4, 0x4)
    OP_28(0x39, 0x4, 0x2)
    OP_28(0x39, 0x4, 0x8)
    OP_28(0x39, 0x4, 0x10)
    OP_28(0x39, 0x4, 0x20)
    OP_28(0x39, 0x1, 0x1)
    OP_28(0x39, 0x1, 0x2)
    OP_28(0x39, 0x1, 0x4)
    OP_28(0x39, 0x1, 0x8)
    OP_28(0x39, 0x1, 0x10)
    OP_28(0x39, 0x1, 0x20)
    OP_28(0x39, 0x1, 0x40)
    OP_28(0x39, 0x1, 0x80)
    OP_28(0x39, 0x1, 0x100)
    OP_28(0x39, 0x1, 0x200)
    OP_28(0x39, 0x1, 0x400)
    OP_28(0x39, 0x1, 0x800)
    OP_28(0x39, 0x1, 0x1000)
    OP_28(0x39, 0x1, 0x2000)
    OP_28(0x39, 0x1, 0x4000)
    OP_28(0x39, 0x1, 0x8000)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x8)
    OP_28(0x3A, 0x4, 0x10)
    OP_28(0x3A, 0x4, 0x20)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    OP_28(0x3A, 0x1, 0x4)
    OP_28(0x3A, 0x1, 0x8)
    OP_28(0x3A, 0x1, 0x10)
    OP_28(0x3A, 0x1, 0x20)
    OP_28(0x3A, 0x1, 0x40)
    OP_28(0x3A, 0x1, 0x80)
    OP_28(0x3A, 0x1, 0x100)
    OP_28(0x3A, 0x1, 0x200)
    OP_28(0x3A, 0x1, 0x400)
    OP_28(0x3A, 0x1, 0x800)
    OP_28(0x3A, 0x1, 0x1000)
    OP_28(0x3A, 0x1, 0x2000)
    OP_28(0x3A, 0x1, 0x4000)
    OP_28(0x3A, 0x1, 0x8000)
    OP_28(0x3B, 0x4, 0x4)
    OP_28(0x3B, 0x4, 0x2)
    OP_28(0x3B, 0x4, 0x8)
    OP_28(0x3B, 0x4, 0x10)
    OP_28(0x3B, 0x4, 0x20)
    OP_28(0x3B, 0x1, 0x1)
    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    OP_28(0x3B, 0x1, 0x8)
    OP_28(0x3B, 0x1, 0x10)
    OP_28(0x3B, 0x1, 0x20)
    OP_28(0x3B, 0x1, 0x40)
    OP_28(0x3B, 0x1, 0x80)
    OP_28(0x3B, 0x1, 0x100)
    OP_28(0x3B, 0x1, 0x200)
    OP_28(0x3B, 0x1, 0x400)
    OP_28(0x3B, 0x1, 0x800)
    OP_28(0x3B, 0x1, 0x1000)
    OP_28(0x3B, 0x1, 0x2000)
    OP_28(0x3B, 0x1, 0x4000)
    OP_28(0x3B, 0x1, 0x8000)
    OP_28(0x3C, 0x4, 0x2)
    OP_28(0x3C, 0x4, 0x8)
    OP_28(0x3C, 0x4, 0x10)
    OP_28(0x3C, 0x4, 0x20)
    OP_28(0x3C, 0x1, 0x1)
    OP_28(0x3C, 0x1, 0x2)
    OP_28(0x3C, 0x1, 0x4)
    OP_28(0x3C, 0x1, 0x8)
    OP_28(0x3C, 0x1, 0x10)
    OP_28(0x3C, 0x1, 0x20)
    OP_28(0x3C, 0x1, 0x40)
    OP_28(0x3C, 0x1, 0x80)
    OP_28(0x3C, 0x1, 0x100)
    OP_28(0x3C, 0x1, 0x200)
    OP_28(0x3C, 0x1, 0x400)
    OP_28(0x3C, 0x1, 0x800)
    OP_28(0x3C, 0x1, 0x1000)
    OP_28(0x3C, 0x1, 0x2000)
    OP_28(0x3C, 0x1, 0x4000)
    OP_28(0x3C, 0x1, 0x8000)
    OP_28(0x3D, 0x4, 0x4)
    OP_28(0x3D, 0x4, 0x2)
    OP_28(0x3D, 0x4, 0x8)
    OP_28(0x3D, 0x4, 0x10)
    OP_28(0x3D, 0x4, 0x20)
    OP_28(0x3D, 0x1, 0x1)
    OP_28(0x3D, 0x1, 0x2)
    OP_28(0x3D, 0x1, 0x4)
    OP_28(0x3D, 0x1, 0x8)
    OP_28(0x3D, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_28(0x3D, 0x1, 0x80)
    OP_28(0x3D, 0x1, 0x100)
    OP_28(0x3D, 0x1, 0x200)
    OP_28(0x3D, 0x1, 0x400)
    OP_28(0x3D, 0x1, 0x800)
    OP_28(0x3D, 0x1, 0x1000)
    OP_28(0x3D, 0x1, 0x2000)
    OP_28(0x3D, 0x1, 0x4000)
    OP_28(0x3D, 0x1, 0x8000)
    OP_28(0x3E, 0x4, 0x4)
    OP_28(0x3E, 0x4, 0x2)
    OP_28(0x3E, 0x4, 0x8)
    OP_28(0x3E, 0x4, 0x10)
    OP_28(0x3E, 0x4, 0x20)
    OP_28(0x3E, 0x1, 0x1)
    OP_28(0x3E, 0x1, 0x2)
    OP_28(0x3E, 0x1, 0x4)
    OP_28(0x3E, 0x1, 0x8)
    OP_28(0x3E, 0x1, 0x10)
    OP_28(0x3E, 0x1, 0x20)
    OP_28(0x3E, 0x1, 0x40)
    OP_28(0x3E, 0x1, 0x80)
    OP_28(0x3E, 0x1, 0x100)
    OP_28(0x3E, 0x1, 0x200)
    OP_28(0x3E, 0x1, 0x400)
    OP_28(0x3E, 0x1, 0x800)
    OP_28(0x3E, 0x1, 0x1000)
    OP_28(0x3E, 0x1, 0x2000)
    OP_28(0x3E, 0x1, 0x4000)
    OP_28(0x3E, 0x1, 0x8000)
    OP_28(0x3F, 0x4, 0x4)
    OP_28(0x3F, 0x4, 0x2)
    OP_28(0x3F, 0x4, 0x8)
    OP_28(0x3F, 0x4, 0x10)
    OP_28(0x3F, 0x4, 0x20)
    OP_28(0x3F, 0x1, 0x1)
    OP_28(0x3F, 0x1, 0x2)
    OP_28(0x3F, 0x1, 0x4)
    OP_28(0x3F, 0x1, 0x8)
    OP_28(0x3F, 0x1, 0x10)
    OP_28(0x3F, 0x1, 0x20)
    OP_28(0x3F, 0x1, 0x40)
    OP_28(0x3F, 0x1, 0x80)
    OP_28(0x3F, 0x1, 0x100)
    OP_28(0x3F, 0x1, 0x200)
    OP_28(0x3F, 0x1, 0x400)
    OP_28(0x3F, 0x1, 0x800)
    OP_28(0x3F, 0x1, 0x1000)
    OP_28(0x3F, 0x1, 0x2000)
    OP_28(0x3F, 0x1, 0x4000)
    OP_28(0x3F, 0x1, 0x8000)
    OP_28(0x40, 0x4, 0x4)
    OP_28(0x40, 0x4, 0x2)
    OP_28(0x40, 0x4, 0x8)
    OP_28(0x40, 0x4, 0x10)
    OP_28(0x40, 0x4, 0x20)
    OP_28(0x40, 0x1, 0x1)
    OP_28(0x40, 0x1, 0x2)
    OP_28(0x40, 0x1, 0x4)
    OP_28(0x40, 0x1, 0x8)
    OP_28(0x40, 0x1, 0x10)
    OP_28(0x40, 0x1, 0x20)
    OP_28(0x40, 0x1, 0x40)
    OP_28(0x40, 0x1, 0x80)
    OP_28(0x40, 0x1, 0x100)
    OP_28(0x40, 0x1, 0x200)
    OP_28(0x40, 0x1, 0x400)
    OP_28(0x40, 0x1, 0x800)
    OP_28(0x40, 0x1, 0x1000)
    OP_28(0x40, 0x1, 0x2000)
    OP_28(0x40, 0x1, 0x4000)
    OP_28(0x40, 0x1, 0x8000)
    Return()

    # Function_43_33B0 end

    def Function_44_4F16(): pass

    label("Function_44_4F16")

    OP_AC(0x1)
    OP_AC(0x2)
    OP_AC(0x3)
    OP_AC(0x4)
    OP_AC(0x5)
    OP_AC(0x6)
    OP_AC(0x7)
    OP_AC(0x8)
    OP_AC(0x9)
    OP_AC(0xA)
    OP_AC(0xB)
    OP_AC(0xC)
    OP_AC(0x14)
    OP_AC(0x15)
    OP_AC(0x16)
    OP_AC(0x17)
    OP_AC(0x18)
    OP_AC(0x19)
    OP_AC(0x1A)
    OP_AC(0x1B)
    OP_AC(0x1C)
    OP_AC(0x1D)
    OP_AC(0x1E)
    OP_AC(0x1F)
    OP_AC(0x20)
    OP_AC(0x21)
    OP_AC(0x22)
    OP_AC(0x23)
    OP_AC(0x24)
    OP_AC(0x25)
    OP_AC(0x26)
    OP_AC(0x27)
    OP_AC(0x28)
    OP_AC(0x29)
    OP_AC(0x2A)
    OP_AC(0x2B)
    OP_AC(0x2C)
    OP_AC(0x2D)
    OP_AC(0x2E)
    OP_AC(0x2F)
    OP_AC(0x30)
    OP_AC(0x31)
    OP_AC(0x32)
    OP_AC(0x33)
    OP_AC(0x34)
    OP_AC(0x35)
    OP_AC(0x36)
    OP_AC(0x37)
    OP_AC(0x38)
    OP_AC(0x39)
    OP_AC(0x3A)
    OP_AC(0x3B)
    OP_AC(0x3C)
    OP_AC(0x3D)
    OP_AC(0x3E)
    OP_AC(0x3F)
    OP_AC(0x40)
    OP_AC(0x41)
    OP_AC(0x42)
    OP_AC(0x43)
    OP_AC(0x44)
    OP_AC(0x45)
    OP_AC(0x46)
    OP_AC(0x47)
    OP_AC(0x48)
    OP_AC(0x49)
    OP_AC(0x4A)
    OP_AC(0x4B)
    OP_AC(0x4C)
    Return()

    # Function_44_4F16 end

    SaveToFile()

Try(main)
