from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_3 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0001   ._SN',
            'ED6_DT21/T0001_1 ._SN',
            'ED6_DT21/T0001_2 ._SN',
            'ED6_DT21/T0001_3 ._SN',
            'ED6_DT21/T0001_4 ._SN',
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
        "Function_1_140",          # 01, 1
        "Function_2_357",          # 02, 2
        "Function_3_54D",          # 03, 3
        "Function_4_6A6",          # 04, 4
        "Function_5_73C",          # 05, 5
        "Function_6_76F",          # 06, 6
        "Function_7_7A2",          # 07, 7
        "Function_8_8A5",          # 08, 8
        "Function_9_95E",          # 09, 9
        "Function_10_A90",         # 0A, 10
        "Function_11_103E",        # 0B, 11
        "Function_12_122C",        # 0C, 12
        "Function_13_13DF",        # 0D, 13
        "Function_14_1615",        # 0E, 14
        "Function_15_1944",        # 0F, 15
        "Function_16_1B90",        # 10, 16
        "Function_17_2829",        # 11, 17
        "Function_18_29D3",        # 12, 18
        "Function_19_2D46",        # 13, 19
        "Function_20_2EEA",        # 14, 20
        "Function_21_3855",        # 15, 21
        "Function_22_3B15",        # 16, 22
        "Function_23_3FEC",        # 17, 23
        "Function_24_4098",        # 18, 24
        "Function_25_4099",        # 19, 25
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06哪个？\x02",
    )

    Jump("loc_BF")

    label("loc_BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_130")

    Menu(
        1,
        10,
        32,
        1,
        (
            "ＡＣ\x01",      # 0
            "后篇\x01",      # 1
            "前篇\x01",      # 2
        )
    )

    Jump("loc_F6")

    label("loc_F6")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10E"),
        (1, "loc_115"),
        (2, "loc_11C"),
        (SWITCH_DEFAULT, "loc_123"),
    )


    label("loc_10E")

    Call(3, 3)
    Jump("loc_12D")

    label("loc_115")

    Call(3, 1)
    Jump("loc_12D")

    label("loc_11C")

    Call(3, 2)
    Jump("loc_12D")

    label("loc_123")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12D")

    Jump("loc_BF")

    label("loc_130")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_140(): pass

    label("Function_1_140")


    AnonymousTalk(    #1
        "\x06哪个？\x02",
    )

    Jump("loc_155")

    label("loc_155")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_347")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0020 队伍与专用ＮＰＬ\x01",                             # 0
            "A0021战斗艾丝蒂尔 约修亚 金 阿加特 奥利维尔\x01",        # 1
            "A0022 战斗雪拉、提妲、科洛丝、科洛丝礼服\x01",           # 2
            "A0023 战斗凯文,莉丝,克鲁茨,亚,乔\x01",                   # 3
            "A0024 战斗尤莉亚,穆拉,基德,凯诺娜\x01",                  # 4
            "A0025 战斗瓦鲁塔,玲,露茜奥拉,布卢布兰\x01",              # 5
            "A0026 战斗莱恩哈特,怀斯曼,猎兵约修亚、乌猫蝶\x01",       # 6
            "A0027 战斗猎兵A,猎兵Ｂ,克鲁茨,卡露娜,基尔巴特\x01",      # 7
            "A0039 后篇座位一览\x01",                                 # 8
            "取消\x01",                                               # 9
        )
    )

    Jump("loc_2B9")

    label("loc_2B9")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E9"),
        (1, "loc_2F2"),
        (2, "loc_2FB"),
        (3, "loc_304"),
        (4, "loc_30D"),
        (5, "loc_316"),
        (6, "loc_31F"),
        (7, "loc_328"),
        (8, "loc_331"),
        (SWITCH_DEFAULT, "loc_33A"),
    )


    label("loc_2E9")

    NewScene("ED6_DT21/A0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2F2")

    NewScene("ED6_DT21/A0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2FB")

    NewScene("ED6_DT21/A0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_304")

    NewScene("ED6_DT21/A0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_30D")

    NewScene("ED6_DT21/A0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_316")

    NewScene("ED6_DT21/A0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_31F")

    NewScene("ED6_DT21/A0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_328")

    NewScene("ED6_DT21/A0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_331")

    NewScene("ED6_DT21/A0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_33A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_155")

    label("loc_347")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_140 end

    def Function_2_357(): pass

    label("Function_2_357")


    AnonymousTalk(    #2
        "\x06哪个？\x02",
    )

    Jump("loc_36C")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53D")

    Menu(
        2,
        10,
        100,
        1,
        (
            "30泛用ＮＰＬ\x01",                                                 # 0
            "31队伍与专用ＮＰＬ\x01",                                           # 1
            "32泛用ＮＰＬ与专用ＮＰＬ２＿ＡＰＬ\x01",                           # 2
            "33PT战斗艾丝蒂尔、约修亚、金、阿加特、奥利维尔\x01",               # 3
            "34PT战斗约修亚、雪拉扎德、提妲、科洛丝\x01",                       # 4
            "35NPC战斗男女游击士、小流氓、空贼们\x01",                          # 5
            "36NPC战斗小流氓团伙、男女游击士２\x01",                            # 6
            "37NPC战斗王国兵士、士官、特务兵、洛伦斯、理查德、凯诺娜\x01",      # 7
            "39座位角色\x01",                                                   # 8
            "取消\x01",                                                         # 9
        )
    )

    Jump("loc_4AF")

    label("loc_4AF")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4DF"),
        (1, "loc_4E8"),
        (2, "loc_4F1"),
        (3, "loc_4FA"),
        (4, "loc_503"),
        (5, "loc_50C"),
        (6, "loc_515"),
        (7, "loc_51E"),
        (8, "loc_527"),
        (SWITCH_DEFAULT, "loc_530"),
    )


    label("loc_4DF")

    NewScene("ED6_DT21/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4E8")

    NewScene("ED6_DT21/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4F1")

    NewScene("ED6_DT21/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_4FA")

    NewScene("ED6_DT21/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_503")

    NewScene("ED6_DT21/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_50C")

    NewScene("ED6_DT21/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_515")

    NewScene("ED6_DT21/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_51E")

    NewScene("ED6_DT21/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_527")

    NewScene("ED6_DT21/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_530")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36C")

    label("loc_53D")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_357 end

    def Function_3_54D(): pass

    label("Function_3_54D")


    AnonymousTalk(    #3
        "\x06哪个？\x02",
    )

    Jump("loc_562")

    label("loc_562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_696")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0040卡西乌斯、雾香、菲利普(战斗)\x01",            # 0
            "A0041摩尔根、护卫、黑猎兵、黑莱维(战斗)\x01",      # 1
            "A0042专用NPC(普通)之１\x01",                       # 2
            "A0045专用NPC(普通)之２\x01",                       # 3
            "A0043主要角色新服装(普通)\x01",                    # 4
            "A0044主要角色新服装(战斗)\x01",                    # 5
            "取消\x01",                                         # 6
        )
    )

    Jump("loc_62F")

    label("loc_62F")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_653"),
        (1, "loc_65C"),
        (2, "loc_665"),
        (3, "loc_66E"),
        (4, "loc_677"),
        (5, "loc_680"),
        (SWITCH_DEFAULT, "loc_689"),
    )


    label("loc_653")

    NewScene("ED6_DT21/A0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_65C")

    NewScene("ED6_DT21/A0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_665")

    NewScene("ED6_DT21/A0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_66E")

    NewScene("ED6_DT21/A0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_677")

    NewScene("ED6_DT21/A0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_680")

    NewScene("ED6_DT21/A0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_689")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_562")

    label("loc_696")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_54D end

    def Function_4_6A6(): pass

    label("Function_4_6A6")


    AnonymousTalk(    #4
        "\x06哪个？\x02",
    )

    Jump("loc_6BB")

    label("loc_6BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72C")

    Menu(
        1,
        10,
        32,
        1,
        (
            "ＡＣ\x01",      # 0
            "后篇\x01",      # 1
            "前篇\x01",      # 2
        )
    )

    Jump("loc_6F2")

    label("loc_6F2")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_70A"),
        (1, "loc_711"),
        (2, "loc_718"),
        (SWITCH_DEFAULT, "loc_71F"),
    )


    label("loc_70A")

    Call(3, 7)
    Jump("loc_729")

    label("loc_711")

    Call(3, 6)
    Jump("loc_729")

    label("loc_718")

    Call(3, 5)
    Jump("loc_729")

    label("loc_71F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_729")

    Jump("loc_6BB")

    label("loc_72C")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_6A6 end

    def Function_5_73C(): pass

    label("Function_5_73C")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05注）请在ＳＣ中确认。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_5_73C end

    def Function_6_76F(): pass

    label("Function_6_76F")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05注）请在ＳＣ中确认。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_6_76F end

    def Function_7_7A2(): pass

    label("Function_7_7A2")


    AnonymousTalk(    #7
        "\x06哪个？\x02",
    )

    Jump("loc_7B7")

    label("loc_7B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_895")

    Menu(
        2,
        10,
        32,
        1,
        (
            "T0040 魔兽清单(14000-14250)\x01",      # 0
            "T0041 魔兽清单(14260-14500)\x01",      # 1
            "T0042 魔兽清单(14510-14750)\x01",      # 2
            "T0043 魔兽清单(14760-14890)\x01",      # 3
            "取消\x01",                             # 4
        )
    )

    Jump("loc_848")

    label("loc_848")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_864"),
        (1, "loc_86D"),
        (2, "loc_876"),
        (3, "loc_87F"),
        (SWITCH_DEFAULT, "loc_888"),
    )


    label("loc_864")

    NewScene("ED6_DT21/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_86D")

    NewScene("ED6_DT21/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_876")

    NewScene("ED6_DT21/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_87F")

    NewScene("ED6_DT21/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_888")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B7")

    label("loc_895")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_7A2 end

    def Function_8_8A5(): pass

    label("Function_8_8A5")


    AnonymousTalk(    #8
        "\x06哪里？\x02",
    )

    Jump("loc_8BA")

    label("loc_8BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94E")

    Menu(
        1,
        -1,
        32,
        1,
        (
            "■主要\x01",          # 0
            "■章节\x01",          # 1
            "■跳到石碑\x01",      # 2
            "■石碑旗子\x01",      # 3
        )
    )

    Jump("loc_906")

    label("loc_906")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_922"),
        (1, "loc_929"),
        (2, "loc_930"),
        (3, "loc_937"),
        (SWITCH_DEFAULT, "loc_93E"),
    )


    label("loc_922")

    Call(3, 12)
    Jump("loc_94B")

    label("loc_929")

    Call(3, 11)
    Jump("loc_94B")

    label("loc_930")

    Call(3, 10)
    Jump("loc_94B")

    label("loc_937")

    Call(3, 9)
    Jump("loc_94B")

    label("loc_93E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_94B")

    label("loc_94B")

    Jump("loc_8BA")

    label("loc_94E")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_8A5 end

    def Function_9_95E(): pass

    label("Function_9_95E")

    OP_3E(0x211, 1)

    label("loc_963")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A80")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "▼全石碑解除\x01",      # 0
            "▼全石碑有效\x01",      # 1
            "▼全石碑无效\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B8"),
        (1, "loc_A60"),
        (2, "loc_A68"),
        (SWITCH_DEFAULT, "loc_A70"),
    )


    label("loc_9B8")

    OP_AA(0)
    OP_AA(256)
    OP_AA(512)
    OP_AA(768)
    OP_AA(1024)
    OP_AA(1280)
    OP_AA(1536)
    OP_AA(1792)
    OP_AA(2048)
    OP_AA(2304)
    OP_AA(2560)
    OP_AA(2816)
    OP_AA(3072)
    OP_AA(3328)
    OP_AA(3584)
    OP_AA(3840)
    OP_AA(4096)
    OP_AA(4352)
    OP_AA(4608)
    OP_AA(4864)
    OP_AA(5120)
    OP_AA(5376)
    OP_AA(5632)
    OP_AA(5888)
    OP_AA(6144)
    OP_AA(6400)
    OP_AA(6912)
    OP_AA(7168)
    OP_AA(7424)
    OP_AA(7680)
    OP_AA(6656)
    OP_AA(7936)
    OP_AA(8192)
    Jump("loc_A7D")

    label("loc_A60")

    OP_AA(65281)
    Jump("loc_A7D")

    label("loc_A68")

    OP_AA(65282)
    Jump("loc_A7D")

    label("loc_A70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A7D")

    label("loc_A7D")

    Jump("loc_963")

    label("loc_A80")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_95E end

    def Function_10_A90(): pass

    label("Function_10_A90")

    OP_3E(0x211, 1)

    AnonymousTalk(    #9
        "\x06哪里？\x02",
    )

    Jump("loc_AAA")

    label("loc_AAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_102E")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "U7000 隐者之庭院\x01",                       # 0
            "M7002 翡翠回廊②\x01",                       # 1
            "M7005 翡翠回廊⑤\x01",                       # 2
            "U4100 格兰赛尔·南街区(白天/傍晚)\x01",      # 3
            "U4150 格兰赛尔·南街区(夜)\x01",             # 4
            "U4165 格兰竞技场/左控制室\x01",              # 5
            "U4250 格兰赛尔城内部/大厅\x01",              # 6
            "M4302 封印区域·最下层\x01",                 # 7
            "M7100 金之道、银之道·分支\x01",             # 8
            "M7104 金之道地区１·BOSS前\x01",             # 9
            "M7103 银之道地区１·BOSS前\x01",             # 10
            "M7107 金之道、银之道·会合\x01",             # 11
            "U5110 卢·洛克尔宿舍内部（白天）\x01",       # 12
            "U5111 卢·洛克尔宿舍内部（夜）\x01",         # 13
            "M5503 巴斯塔尔水道\x01",                     # 14
            "M5504 圣科洛瓦森林\x01",                     # 15
            "M5513 格林姆瑟尔小要塞\x01",                 # 16
            "M7200 光迷宫１-１\x01",                      # 17
            "M7201 光迷宫１-２\x01",                      # 18
            "M7203 影迷宫２\x01",                         # 19
            "M7206 光迷宫/BOSS通路前\x01",                # 20
            "M4113 艾尔贝周游道/罗马尔池\x01",            # 21
            "U2500 杰尼丝王立学院外部\x01",               # 22
            "M5610 湖畔的研究所/１层\x01",                # 23
            "M5611 湖畔的研究所/２层\x01",                # 24
            "M5612 湖畔的研究所/３层\x01",                # 25
            "M5613 湖畔的研究所/４层\x01",                # 26
            "M3100 雷斯顿要塞/外部\x01",                  # 27
            "M3203 雷斯顿要塞/司令部2F\x01",              # 28
            "M3204 雷斯顿要塞/司令部3F\x01",              # 29
            "M5408 古罗力亚斯/甲板\x01",                  # 30
            "M5412 古罗力亚斯/飞机库前\x01",              # 31
            "M5400 古罗力亚斯/圣堂前\x01",                # 32
            "M7310 深渊·入口\x01",                       # 33
            "取消\x01",                                   # 34
        )
    )

    Jump("loc_DF2")

    label("loc_DF2")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E86"),
        (1, "loc_E92"),
        (2, "loc_E9E"),
        (3, "loc_EAA"),
        (4, "loc_EB6"),
        (5, "loc_EC2"),
        (6, "loc_ECE"),
        (7, "loc_EDA"),
        (8, "loc_EE6"),
        (9, "loc_EF2"),
        (10, "loc_EFE"),
        (11, "loc_F0A"),
        (12, "loc_F16"),
        (13, "loc_F22"),
        (14, "loc_F2E"),
        (15, "loc_F3A"),
        (16, "loc_F46"),
        (17, "loc_F52"),
        (18, "loc_F5E"),
        (19, "loc_F6A"),
        (20, "loc_F76"),
        (21, "loc_F82"),
        (22, "loc_F8E"),
        (23, "loc_F9A"),
        (24, "loc_FA6"),
        (25, "loc_FB2"),
        (26, "loc_FBE"),
        (27, "loc_FCA"),
        (28, "loc_FD6"),
        (29, "loc_FE2"),
        (30, "loc_FEE"),
        (31, "loc_FFA"),
        (32, "loc_1006"),
        (33, "loc_1012"),
        (SWITCH_DEFAULT, "loc_101E"),
    )


    label("loc_E86")

    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_E92")

    NewScene("ED6_DT21/M7002   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_E9E")

    NewScene("ED6_DT21/M7005   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EAA")

    NewScene("ED6_DT21/U4100   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EB6")

    NewScene("ED6_DT21/U4150   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EC2")

    NewScene("ED6_DT21/U4165   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_ECE")

    NewScene("ED6_DT21/U4250   ._SN", 109, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EDA")

    NewScene("ED6_DT21/M4302   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EE6")

    NewScene("ED6_DT21/M7100   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EF2")

    NewScene("ED6_DT21/M7104   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_EFE")

    NewScene("ED6_DT21/M7103   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F0A")

    NewScene("ED6_DT21/M7107   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F16")

    NewScene("ED6_DT21/U5110   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F22")

    NewScene("ED6_DT21/U5111   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F2E")

    NewScene("ED6_DT21/M5503   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F3A")

    NewScene("ED6_DT21/M5504   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F46")

    NewScene("ED6_DT21/M5513   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F52")

    NewScene("ED6_DT21/M7200   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F5E")

    NewScene("ED6_DT21/M7201   ._SN", 107, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F6A")

    NewScene("ED6_DT21/M7203   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F76")

    NewScene("ED6_DT21/M7206   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F82")

    NewScene("ED6_DT21/M4113   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F8E")

    NewScene("ED6_DT21/U2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_F9A")

    NewScene("ED6_DT21/M5610   ._SN", 136, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FA6")

    NewScene("ED6_DT21/M5611   ._SN", 137, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FB2")

    NewScene("ED6_DT21/M5612   ._SN", 129, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FBE")

    NewScene("ED6_DT21/M5613   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FCA")

    NewScene("ED6_DT21/M3100   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FD6")

    NewScene("ED6_DT21/M3203   ._SN", 130, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FE2")

    NewScene("ED6_DT21/M3204   ._SN", 127, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FEE")

    NewScene("ED6_DT21/M5408   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_FFA")

    NewScene("ED6_DT21/M5412   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_1006")

    NewScene("ED6_DT21/M5400   ._SN", 129, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_1012")

    NewScene("ED6_DT21/M7310   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_102B")

    label("loc_101E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_102B")

    label("loc_102B")

    Jump("loc_AAA")

    label("loc_102E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_A90 end

    def Function_11_103E(): pass

    label("Function_11_103E")


    AnonymousTalk(    #10
        "\x06哪里？\x02",
    )

    Jump("loc_1053")

    label("loc_1053")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121C")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "T3121 地下实验场\x01",                    # 0
            "E0102 飞船（空贼)\x01",                   # 1
            "T4206 格兰赛尔城外部(舞会会场)\x01",      # 2
            "C5416 古罗力亚斯　星辰之间\x01",          # 3
            "P9000 章节部屋\x01",                      # 4
            "P9001 章节部屋\x01",                      # 5
            "P9002 章节部屋\x01",                      # 6
            "T1500 钓鱼１\x01",                        # 7
            "C4203 钓鱼２\x01",                        # 8
            "R2201 钓鱼３\x01",                        # 9
            "R2201 梅威街道\x01",                      # 10
            "E1001 格兰竞技场（夜）\x01",              # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_117C"),
        (1, "loc_1188"),
        (2, "loc_1194"),
        (3, "loc_11A0"),
        (4, "loc_11AC"),
        (5, "loc_11B8"),
        (6, "loc_11C4"),
        (7, "loc_11D0"),
        (8, "loc_11DC"),
        (9, "loc_11E8"),
        (10, "loc_11F4"),
        (11, "loc_1200"),
        (SWITCH_DEFAULT, "loc_120C"),
    )


    label("loc_117C")

    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_1188")

    NewScene("ED6_DT21/E0102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_1194")

    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11A0")

    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11AC")

    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11B8")

    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11C4")

    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11D0")

    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11DC")

    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11E8")

    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_11F4")

    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_1200")

    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1219")

    label("loc_120C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1219")

    label("loc_1219")

    Jump("loc_1053")

    label("loc_121C")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_103E end

    def Function_12_122C(): pass

    label("Function_12_122C")


    AnonymousTalk(    #11
        "\x06哪里？\x02",
    )

    Jump("loc_1241")

    label("loc_1241")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CF")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "据点、济贫院\x01",                       # 0
            "序章\x01",                               # 1
            "第１星层（翡翠回廊）\x01",               # 2
            "第２星层 (异界化王都格兰赛尔)\x01",      # 3
            "第３星层（金之道、银之道）\x01",         # 4
            "第４星层 (异界化卢·洛克尔)\x01",        # 5
            "第５星层（光与影之迷宫）\x01",           # 6
            "第６星层 (异界化各种地图)\x01",          # 7
            "第７星层（炼狱）\x01",                   # 8
            "幻影之城中枢\x01",                       # 9
            "最终章\x01",                             # 10
        )
    )

    Jump("loc_133A")

    label("loc_133A")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1372"),
        (1, "loc_1379"),
        (2, "loc_1380"),
        (3, "loc_1387"),
        (4, "loc_138E"),
        (5, "loc_1395"),
        (6, "loc_139C"),
        (7, "loc_13A3"),
        (8, "loc_13AA"),
        (9, "loc_13B1"),
        (10, "loc_13B8"),
        (SWITCH_DEFAULT, "loc_13BF"),
    )


    label("loc_1372")

    Call(3, 13)
    Jump("loc_13CC")

    label("loc_1379")

    Call(3, 14)
    Jump("loc_13CC")

    label("loc_1380")

    Call(3, 15)
    Jump("loc_13CC")

    label("loc_1387")

    Call(3, 16)
    Jump("loc_13CC")

    label("loc_138E")

    Call(3, 17)
    Jump("loc_13CC")

    label("loc_1395")

    Call(3, 18)
    Jump("loc_13CC")

    label("loc_139C")

    Call(3, 19)
    Jump("loc_13CC")

    label("loc_13A3")

    Call(3, 20)
    Jump("loc_13CC")

    label("loc_13AA")

    Call(3, 21)
    Jump("loc_13CC")

    label("loc_13B1")

    Call(3, 22)
    Jump("loc_13CC")

    label("loc_13B8")

    Call(3, 23)
    Jump("loc_13CC")

    label("loc_13BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13CC")

    label("loc_13CC")

    Jump("loc_1241")

    label("loc_13CF")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_122C end

    def Function_13_13DF(): pass

    label("Function_13_13DF")


    AnonymousTalk(    #12
        "\x06哪里？\x02",
    )

    Jump("loc_13F4")

    label("loc_13F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1605")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U7000 隐者之庭院（据点）\x01",               # 0
            "U7001 隐者之庭院（据点）中央通路\x01",       # 1
            "U7002 隐者之庭院（据点）左通路\x01",         # 2
            "U7003 隐者之庭院（据点）右通路\x01",         # 3
            "U7004 隐者之庭院（据点）全地图\x01",         # 4
            "P7000 紫苑之家（雪之济贫院）外\x01",         # 5
            "P7010 紫苑之家（雪之济贫院）内\x01",         # 6
            "P7011 紫苑之家（雪之济贫院）内\x01",         # 7
            "P7012 紫苑之家/螺旋阶梯·通路\x01",          # 8
            "P7013 紫苑之家/开始之地（圆天棚）\x01",      # 9
            "取消\x01",                                   # 10
        )
    )

    Jump("loc_1549")

    label("loc_1549")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_157D"),
        (1, "loc_1589"),
        (2, "loc_1595"),
        (3, "loc_15A1"),
        (4, "loc_15AD"),
        (5, "loc_15B9"),
        (6, "loc_15C5"),
        (7, "loc_15D1"),
        (8, "loc_15DD"),
        (9, "loc_15E9"),
        (SWITCH_DEFAULT, "loc_15F5"),
    )


    label("loc_157D")

    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_1589")

    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_1595")

    NewScene("ED6_DT21/U7002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15A1")

    NewScene("ED6_DT21/U7003   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15AD")

    NewScene("ED6_DT21/U7004   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15B9")

    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15C5")

    NewScene("ED6_DT21/P7010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15D1")

    NewScene("ED6_DT21/P7011   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15DD")

    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15E9")

    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1602")

    label("loc_15F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1602")

    label("loc_1602")

    Jump("loc_13F4")

    label("loc_1605")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_13DF end

    def Function_14_1615(): pass

    label("Function_14_1615")


    AnonymousTalk(    #13
        "\x06哪里？\x02",
    )

    Jump("loc_162A")

    label("loc_162A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1934")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "E1100 露西塔尼亚号外部\x01",                      # 0
            "E1110 露西塔尼亚号内部（化妆舞会会场）\x01",      # 1
            "E1111 露西塔尼亚号内部（私用地区）\x01",          # 2
            "E1200 梅尔卡瓦外部\x01",                          # 3
            "E1210 梅尔卡瓦内部\x01",                          # 4
            "E0811 天空地图（夜）\x01",                        # 5
            "E0700 国际定期船『格雷特纳号』外部\x01",          # 6
            "E0710 国际定期船『格雷特纳号』内部\x01",          # 7
            "T4105 格兰赛尔飞艇坪(埃尔赛尤在场)\x01",          # 8
            "T4131 大圣堂\x01",                                # 9
            "T4144 大圣堂地下（圆天棚）\x01",                  # 10
            "T4145 大圣堂地下（螺旋阶梯/通路）\x01",           # 11
            "E0900 水上地图\x01",                              # 12
            "T4152 王都格兰赛尔外部（西街区、夜）\x01",        # 13
            "T4151 王都格兰赛尔外部（东街区、夜）\x01",        # 14
            "T4404 王都格兰赛尔外部（码头２、夜）\x01",        # 15
            "取消\x01",                                        # 16
        )
    )

    Jump("loc_1818")

    label("loc_1818")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1864"),
        (1, "loc_1870"),
        (2, "loc_187C"),
        (3, "loc_1888"),
        (4, "loc_1894"),
        (5, "loc_18A0"),
        (6, "loc_18AC"),
        (7, "loc_18B8"),
        (8, "loc_18C4"),
        (9, "loc_18D0"),
        (10, "loc_18DC"),
        (11, "loc_18E8"),
        (12, "loc_18F4"),
        (13, "loc_1900"),
        (14, "loc_190C"),
        (15, "loc_1918"),
        (SWITCH_DEFAULT, "loc_1924"),
    )


    label("loc_1864")

    NewScene("ED6_DT21/E1100   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1870")

    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_187C")

    NewScene("ED6_DT21/E1111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1888")

    NewScene("ED6_DT21/E1200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1894")

    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18A0")

    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18AC")

    NewScene("ED6_DT21/E0700   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18B8")

    NewScene("ED6_DT21/E0710   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18C4")

    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18D0")

    NewScene("ED6_DT21/T4131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18DC")

    NewScene("ED6_DT21/T4144   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18E8")

    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_18F4")

    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1900")

    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_190C")

    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1918")

    NewScene("ED6_DT21/T4404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1931")

    label("loc_1924")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1931")

    label("loc_1931")

    Jump("loc_162A")

    label("loc_1934")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_1615 end

    def Function_15_1944(): pass

    label("Function_15_1944")


    AnonymousTalk(    #14
        "\x06哪里？\x02",
    )

    Jump("loc_1959")

    label("loc_1959")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B80")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7001 翡翠回廊①(提妲)\x01",                 # 0
            "M7002 翡翠回廊②(埃尔赛尤)\x01",             # 1
            "M7003 翡翠回廊③(螺旋阶梯１)\x01",           # 2
            "M7004 翡翠回廊④(螺旋阶梯２)\x01",           # 3
            "M7005 翡翠回廊⑤(BOSS部屋)\x01",             # 4
            "M7006 翡翠回廊⑥(导力梯)\x01",               # 5
            "M7007 翡翠回廊⑦(辟静瞻k進餐掭挠?\x01",      # 6
            "P0310 埃尔赛尤内部　甲板联络通路\x01",       # 7
            "P0311 埃尔赛尤内部　联络通路１\x01",         # 8
            "P0312 埃尔赛尤内部　联络通路２\x01",         # 9
            "P0313 埃尔赛尤内部　船舱\x01",               # 10
            "取消\x01",                                   # 11
        )
    )

    Jump("loc_1AB4")

    label("loc_1AB4")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AEC"),
        (1, "loc_1AF8"),
        (2, "loc_1B04"),
        (3, "loc_1B10"),
        (4, "loc_1B1C"),
        (5, "loc_1B28"),
        (6, "loc_1B34"),
        (7, "loc_1B40"),
        (8, "loc_1B4C"),
        (9, "loc_1B58"),
        (10, "loc_1B64"),
        (SWITCH_DEFAULT, "loc_1B70"),
    )


    label("loc_1AEC")

    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1AF8")

    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B04")

    NewScene("ED6_DT21/M7003   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B10")

    NewScene("ED6_DT21/M7004   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B1C")

    NewScene("ED6_DT21/M7005   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B28")

    NewScene("ED6_DT21/M7006   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B34")

    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B40")

    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B4C")

    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B58")

    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B64")

    NewScene("ED6_DT21/P0313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1B7D")

    label("loc_1B70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B7D")

    label("loc_1B7D")

    Jump("loc_1959")

    label("loc_1B80")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_1944 end

    def Function_16_1B90(): pass

    label("Function_16_1B90")


    AnonymousTalk(    #15
        "\x06哪里？\x02",
    )

    Jump("loc_1BA5")

    label("loc_1BA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2819")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U4406 王都格兰赛尔外部（码头山猫号在场)\x01",                   # 0
            "U4100 王都格兰赛尔外部（南街区）\x01",                          # 1
            "U4101 王都格兰赛尔外部（东街区）\x01",                          # 2
            "U4102 王都格兰赛尔外部（西街区）\x01",                          # 3
            "U4103 王都格兰赛尔外部（北街区）\x01",                          # 4
            "U4104 王都格兰赛尔外部（竞技场内侧）\x01",                      # 5
            "U4106 格兰赛尔飞艇坪(无埃尔赛尤)\x01",                          # 6
            "U4110 民家１.２.６.７.８\x01",                                  # 7
            "U4111 民家３.４.５\x01",                                        # 8
            "U4120 武器屋、工房\x01",                                        # 9
            "U4121 协会、钓公师团本部\x01",                                  # 10
            "U4122 艾德尔百货店、空港服务台\x01",                            # 11
            "U4130 酒馆、咖啡厅、利贝尔通讯社\x01",                          # 12
            "U4131 大圣堂\x01",                                              # 13
            "U4132 酒店\x01",                                                # 14
            "U4135 历史资料馆\x01",                                          # 15
            "U4136 格兰竞技场\x01",                                          # 16
            "U4138 帝国大使馆内部\x01",                                      # 17
            "U4139 共和国大使馆内部\x01",                                    # 18
            "U4143 幕后商人之店内部\x01",                                    # 19
            "U4400 王都格兰赛尔外部（码头１）\x01",                          # 20
            "U4401 王都格兰赛尔外部（码头２）\x01",                          # 21
            "U4402 王都格兰赛尔外部（码头仓库内部）\x01",                    # 22
            "U4403 王都格兰赛尔外部（码头蒂皋舱仓库内部）\x01",              # 23
            "U4150 王都格兰赛尔外部（南街区、夜）\x01",                      # 24
            "U4151 王都格兰赛尔外部（东街区、夜）\x01",                      # 25
            "U4152 王都格兰赛尔外部（西街区、夜）\x01",                      # 26
            "U4153 王都格兰赛尔外部（北街区、夜）\x01",                      # 27
            "U4203 格兰赛尔城外部(大街和相连)（夜）\x01",                    # 28
            "U4204 格兰赛尔城外部(空中庭院)（夜）\x01",                      # 29
            "U4205 格兰赛尔城外部(女王的露台)（夜）\x01",                    # 30
            "U4250 格兰赛尔城内部(大厅)（夜）\x01",                          # 31
            "U4251 格兰赛尔城内部(宴会大厅)（夜）\x01",                      # 32
            "U4252 格兰赛尔城内部(行政区域)（夜）\x01",                      # 33
            "U4253 格兰赛尔城内部(亲卫队办事处)（夜）\x01",                  # 34
            "U4254 格兰赛尔城内部(女佣房间)（夜）\x01",                      # 35
            "U4255 格兰赛尔城内部(厨房)（夜）\x01",                          # 36
            "U4260 格兰赛尔城内部(谒见大厅)（夜）\x01",                      # 37
            "U4261 格兰赛尔城内部(二层右翼)（夜）\x01",                      # 38
            "U4262 格兰赛尔城内部(二层左翼)（夜）\x01",                      # 39
            "U4270 格兰赛尔城内部(女王宫)（夜）\x01",                        # 40
            "U4280 格兰赛尔城内部(地下仓库)（夜）\x01",                      # 41
            "U4241 格兰赛尔城内部(封印区域)\x01",                            # 42
            "M4300 封印区域（最上层）\x01",                                  # 43
            "M4302 封印区域（最下层）\x01",                                  # 44
            "M4303 封印区域（BOSS部屋）\x01",                                # 45
            "M4308 封印区域（导力梯部屋）\x01",                              # 46
            "U4123 游击士协会（夜）\x01",                                    # 47
            "U4133 酒店（夜）\x01",                                          # 48
            "U4134 大圣堂（夜）\x01",                                        # 49
            "U4137 咖啡厅（夜）\x01",                                        # 50
            "U4404 王都格兰赛尔外部（码头２夜）\x01",                        # 51
            "U4405 王都格兰赛尔外部（码头仓库内部夜）\x01",                  # 52
            "U4156 格兰赛尔飞艇坪(无夜埃尔赛尤)\x01",                        # 53
            "U4160 民家１.２.６.７.８（夜）\x01",                            # 54
            "U4161 民家３.４.５（夜）\x01",                                  # 55
            "U4162 历史资料馆（夜）\x01",                                    # 56
            "U4163 帝国大使馆内部（夜）\x01",                                # 57
            "U4164 幕后商人的店内部（夜）\x01",                              # 58
            "U4165 格兰竞技场(服务台、控制室)（夜）\x01",                    # 59
            "U4166 格兰竞技场（竞技场内侧）（夜）\x01",                      # 60
            "U4167 码头仓库内部（奥尔杰尤仓库内部）（夜）\x01",              # 61
            "U4168 王都格兰赛尔外部（有码头山猫号）（夜）\x01",              # 62
            "U4169 王都格兰赛尔·飞艇坪服务台、钓公师团本部（夜）\x01",      # 63
            "E0110 飞船（空贼用）内部\x01",                                  # 64
            "U4200 格兰赛尔城外部(大街和相连)\x01",                          # 65
            "取消\x01",                                                      # 66
        )
    )

    Jump("loc_23DD")

    label("loc_23DD")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24F1"),
        (1, "loc_24FD"),
        (2, "loc_2509"),
        (3, "loc_2515"),
        (4, "loc_2521"),
        (5, "loc_252D"),
        (6, "loc_2539"),
        (7, "loc_2545"),
        (8, "loc_2551"),
        (9, "loc_255D"),
        (10, "loc_2569"),
        (11, "loc_2575"),
        (12, "loc_2581"),
        (13, "loc_258D"),
        (14, "loc_2599"),
        (15, "loc_25A5"),
        (16, "loc_25B1"),
        (17, "loc_25BD"),
        (18, "loc_25C9"),
        (19, "loc_25D5"),
        (20, "loc_25E1"),
        (21, "loc_25ED"),
        (22, "loc_25F9"),
        (23, "loc_2605"),
        (24, "loc_2611"),
        (25, "loc_261D"),
        (26, "loc_2629"),
        (27, "loc_2635"),
        (28, "loc_2641"),
        (29, "loc_264D"),
        (30, "loc_2659"),
        (31, "loc_2665"),
        (32, "loc_2671"),
        (33, "loc_267D"),
        (34, "loc_2689"),
        (35, "loc_2695"),
        (36, "loc_26A1"),
        (37, "loc_26AD"),
        (38, "loc_26B9"),
        (39, "loc_26C5"),
        (40, "loc_26D1"),
        (41, "loc_26DD"),
        (42, "loc_26E9"),
        (43, "loc_26F5"),
        (44, "loc_2701"),
        (45, "loc_270D"),
        (46, "loc_2719"),
        (47, "loc_2725"),
        (48, "loc_2731"),
        (49, "loc_273D"),
        (50, "loc_2749"),
        (51, "loc_2755"),
        (52, "loc_2761"),
        (53, "loc_276D"),
        (54, "loc_2779"),
        (55, "loc_2785"),
        (56, "loc_2791"),
        (57, "loc_279D"),
        (58, "loc_27A9"),
        (59, "loc_27B5"),
        (60, "loc_27C1"),
        (61, "loc_27CD"),
        (62, "loc_27D9"),
        (63, "loc_27E5"),
        (64, "loc_27F1"),
        (65, "loc_27FD"),
        (SWITCH_DEFAULT, "loc_2809"),
    )


    label("loc_24F1")

    NewScene("ED6_DT21/U4406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_24FD")

    NewScene("ED6_DT21/U4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2509")

    NewScene("ED6_DT21/U4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2515")

    NewScene("ED6_DT21/U4102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2521")

    NewScene("ED6_DT21/U4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_252D")

    NewScene("ED6_DT21/U4104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2539")

    NewScene("ED6_DT21/U4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2545")

    NewScene("ED6_DT21/U4110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2551")

    NewScene("ED6_DT21/U4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_255D")

    NewScene("ED6_DT21/U4120   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2569")

    NewScene("ED6_DT21/U4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2575")

    NewScene("ED6_DT21/U4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2581")

    NewScene("ED6_DT21/U4130   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_258D")

    NewScene("ED6_DT21/U4131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2599")

    NewScene("ED6_DT21/U4132   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25A5")

    NewScene("ED6_DT21/U4135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25B1")

    NewScene("ED6_DT21/U4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25BD")

    NewScene("ED6_DT21/U4138   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25C9")

    NewScene("ED6_DT21/U4139   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25D5")

    NewScene("ED6_DT21/U4143   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25E1")

    NewScene("ED6_DT21/U4400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25ED")

    NewScene("ED6_DT21/U4401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_25F9")

    NewScene("ED6_DT21/U4402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2605")

    NewScene("ED6_DT21/U4403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2611")

    NewScene("ED6_DT21/U4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_261D")

    NewScene("ED6_DT21/U4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2629")

    NewScene("ED6_DT21/U4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2635")

    NewScene("ED6_DT21/U4153   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2641")

    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_264D")

    NewScene("ED6_DT21/U4204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2659")

    NewScene("ED6_DT21/U4205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2665")

    NewScene("ED6_DT21/U4250   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2671")

    NewScene("ED6_DT21/U4251   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_267D")

    NewScene("ED6_DT21/U4252   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2689")

    NewScene("ED6_DT21/U4253   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2695")

    NewScene("ED6_DT21/U4254   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26A1")

    NewScene("ED6_DT21/U4255   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26AD")

    NewScene("ED6_DT21/U4260   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26B9")

    NewScene("ED6_DT21/U4261   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26C5")

    NewScene("ED6_DT21/U4262   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26D1")

    NewScene("ED6_DT21/U4270   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26DD")

    NewScene("ED6_DT21/U4280   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26E9")

    NewScene("ED6_DT21/U4241   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_26F5")

    NewScene("ED6_DT21/M4300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2701")

    NewScene("ED6_DT21/M4302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_270D")

    NewScene("ED6_DT21/M4303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2719")

    NewScene("ED6_DT21/M4308   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2725")

    NewScene("ED6_DT21/U4123   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2731")

    NewScene("ED6_DT21/U4133   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_273D")

    NewScene("ED6_DT21/U4134   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2749")

    NewScene("ED6_DT21/U4137   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2755")

    NewScene("ED6_DT21/U4404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2761")

    NewScene("ED6_DT21/U4405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_276D")

    NewScene("ED6_DT21/U4156   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2779")

    NewScene("ED6_DT21/U4160   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2785")

    NewScene("ED6_DT21/U4161   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2791")

    NewScene("ED6_DT21/U4162   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_279D")

    NewScene("ED6_DT21/U4163   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27A9")

    NewScene("ED6_DT21/U4164   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27B5")

    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27C1")

    NewScene("ED6_DT21/U4166   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27CD")

    NewScene("ED6_DT21/U4167   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27D9")

    NewScene("ED6_DT21/U4168   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27E5")

    NewScene("ED6_DT21/U4169   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27F1")

    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_27FD")

    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2816")

    label("loc_2809")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2816")

    label("loc_2816")

    Jump("loc_1BA5")

    label("loc_2819")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1B90 end

    def Function_17_2829(): pass

    label("Function_17_2829")


    AnonymousTalk(    #16
        "\x06哪里？\x02",
    )

    Jump("loc_283E")

    label("loc_283E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29C3")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7100 金之道·银之道　分支地图\x01",      # 0
            "M7101 银之道地区①\x01",                  # 1
            "M7102 金之道地区①\x01",                  # 2
            "M7103 银之道地区②\x01",                  # 3
            "M7104 金之道地区②\x01",                  # 4
            "M7105 银之道地区③(银BOSS部屋)\x01",      # 5
            "M7106 金之道地区③(金BOSS部屋)\x01",      # 6
            "M7107 金之道·银之道　会合地图\x01",      # 7
            "取消\x01",                                # 8
        )
    )

    Jump("loc_2927")

    label("loc_2927")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2953"),
        (1, "loc_295F"),
        (2, "loc_296B"),
        (3, "loc_2977"),
        (4, "loc_2983"),
        (5, "loc_298F"),
        (6, "loc_299B"),
        (7, "loc_29A7"),
        (SWITCH_DEFAULT, "loc_29B3"),
    )


    label("loc_2953")

    NewScene("ED6_DT21/M7100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_295F")

    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_296B")

    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_2977")

    NewScene("ED6_DT21/M7103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_2983")

    NewScene("ED6_DT21/M7104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_298F")

    NewScene("ED6_DT21/M7105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_299B")

    NewScene("ED6_DT21/M7106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_29A7")

    NewScene("ED6_DT21/M7107   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_29C0")

    label("loc_29B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_29C0")

    label("loc_29C0")

    Jump("loc_283E")

    label("loc_29C3")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_2829 end

    def Function_18_29D3(): pass

    label("Function_18_29D3")


    AnonymousTalk(    #17
        "\x06哪里？\x02",
    )

    Jump("loc_29E8")

    label("loc_29E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D36")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U5100 卢·洛克尔训练场外部\x01",                  # 0
            "U5102 卢·洛克尔训练场外部（夜异次元）\x01",      # 1
            "U5110 卢·洛克尔训练场内部\x01",                  # 2
            "U5111 卢·洛克尔训练场内部（夜）\x01",            # 3
            "M5503 巴斯塔尔水道入口\x01",                      # 4
            "M5500 巴斯塔尔水道①\x01",                        # 5
            "M5501 巴斯塔尔水道②\x01",                        # 6
            "M5502 巴斯塔尔水道③\x01",                        # 7
            "M5503 巴斯塔尔水道BOSS部屋\x01",                  # 8
            "M5504 圣科洛瓦森林①\x01",                        # 9
            "M5505 圣科洛瓦森林②\x01",                        # 10
            "M5506 圣科洛瓦森林③\x01",                        # 11
            "M5512 圣科洛瓦森林④\x01",                        # 12
            "M5507 圣科洛瓦森林BOSS部屋\x01",                  # 13
            "M5508 格林姆瑟尔小要塞①\x01",                    # 14
            "M5509 格林姆瑟尔小要塞②\x01",                    # 15
            "M5510 格林姆瑟尔小要塞③\x01",                    # 16
            "M5511 格林姆瑟尔小要塞④\x01",                    # 17
            "M5513 格林姆瑟尔小要塞BOSS部屋\x01",              # 18
            "取消\x01",                                        # 19
        )
    )

    Jump("loc_2BEA")

    label("loc_2BEA")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C42"),
        (1, "loc_2C4E"),
        (2, "loc_2C5A"),
        (3, "loc_2C66"),
        (4, "loc_2C72"),
        (5, "loc_2C7E"),
        (6, "loc_2C8A"),
        (7, "loc_2C96"),
        (8, "loc_2CA2"),
        (9, "loc_2CAE"),
        (10, "loc_2CBA"),
        (11, "loc_2CC6"),
        (12, "loc_2CD2"),
        (13, "loc_2CDE"),
        (14, "loc_2CEA"),
        (15, "loc_2CF6"),
        (16, "loc_2D02"),
        (17, "loc_2D0E"),
        (18, "loc_2D1A"),
        (SWITCH_DEFAULT, "loc_2D26"),
    )


    label("loc_2C42")

    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C4E")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C5A")

    NewScene("ED6_DT21/U5110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C66")

    NewScene("ED6_DT21/U5111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C72")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C7E")

    NewScene("ED6_DT21/M5500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C8A")

    NewScene("ED6_DT21/M5501   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2C96")

    NewScene("ED6_DT21/M5502   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CA2")

    NewScene("ED6_DT21/M5503   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CAE")

    NewScene("ED6_DT21/M5504   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CBA")

    NewScene("ED6_DT21/M5505   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CC6")

    NewScene("ED6_DT21/M5506   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CD2")

    NewScene("ED6_DT21/M5512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CDE")

    NewScene("ED6_DT21/M5507   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CEA")

    NewScene("ED6_DT21/M5508   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2CF6")

    NewScene("ED6_DT21/M5509   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2D02")

    NewScene("ED6_DT21/M5510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2D0E")

    NewScene("ED6_DT21/M5511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2D1A")

    NewScene("ED6_DT21/M5513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D33")

    label("loc_2D26")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D33")

    label("loc_2D33")

    Jump("loc_29E8")

    label("loc_2D36")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_29D3 end

    def Function_19_2D46(): pass

    label("Function_19_2D46")


    AnonymousTalk(    #18
        "\x06哪里？\x02",
    )

    Jump("loc_2D5B")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EDA")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7200 光地区地图　１－１\x01",        # 0
            "M7201 光地区地图　１－２\x01",        # 1
            "M7202 影地区地图　１\x01",            # 2
            "M7203 影地区地图　２\x01",            # 3
            "M7204 光地区地图　２－１\x01",        # 4
            "M7205 光地区地图　２－２\x01",        # 5
            "M7206 光地区地图BOSS前通路\x01",      # 6
            "M7207 光地区地图BOSS部屋\x01",        # 7
            "取消\x01",                            # 8
        )
    )

    Jump("loc_2E3E")

    label("loc_2E3E")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E6A"),
        (1, "loc_2E76"),
        (2, "loc_2E82"),
        (3, "loc_2E8E"),
        (4, "loc_2E9A"),
        (5, "loc_2EA6"),
        (6, "loc_2EB2"),
        (7, "loc_2EBE"),
        (SWITCH_DEFAULT, "loc_2ECA"),
    )


    label("loc_2E6A")

    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2E76")

    NewScene("ED6_DT21/M7201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2E82")

    NewScene("ED6_DT21/M7202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2E8E")

    NewScene("ED6_DT21/M7203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2E9A")

    NewScene("ED6_DT21/M7204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2EA6")

    NewScene("ED6_DT21/M7205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2EB2")

    NewScene("ED6_DT21/M7206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2EBE")

    NewScene("ED6_DT21/M7207   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2ED7")

    label("loc_2ECA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2ED7")

    label("loc_2ED7")

    Jump("loc_2D5B")

    label("loc_2EDA")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_2D46 end

    def Function_20_2EEA(): pass

    label("Function_20_2EEA")


    AnonymousTalk(    #19
        "\x06哪里？\x02",
    )

    Jump("loc_2EFF")

    label("loc_2EFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3845")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M4110 艾尔贝周游道①\x01",                                # 0
            "M4111 艾尔贝周游道②\x01",                                # 1
            "M4112 艾尔贝周游道③\x01",                                # 2
            "M4113 艾尔贝周游道④\x01",                                # 3
            "U2500 杰尼丝王立学院外部\x01",                            # 4
            "U2501 前往杰尼丝王立学院旧校舍的道路\x01",                # 5
            "U2510 杰尼丝王立学院（主馆）\x01",                        # 6
            "U2511 杰尼丝王立学院（课外俱乐部房）\x01",                # 7
            "U2512 杰尼丝王立学院（宿舍）\x01",                        # 8
            "U2513 杰尼丝王立学院（讲堂）\x01",                        # 9
            "U2600 王立学院旧校舍外部\x01",                            # 10
            "U2610 王立学院旧校舍内部\x01",                            # 11
            "M5400 古罗力亚斯内部（监禁艾丝蒂尔的房间）\x01",          # 12
            "M5401 古罗力亚斯内部（怀斯曼的房间）\x01",                # 13
            "M5402 古罗力亚斯内部（甲板方向通路）\x01",                # 14
            "M5403 古罗力亚斯内部（甲板～出入口方向通路）\x01",        # 15
            "M5404 古罗力亚斯内部（出入口～飞机库方向通路）\x01",      # 16
            "M5405 古罗力亚斯内部（飞机库远处）\x01",                  # 17
            "M5406 古罗力亚斯内部（正对飞机库）\x01",                  # 18
            "M5407 古罗力亚斯内部（导力梯箱）\x01",                    # 19
            "M5408 古罗力亚斯外装（甲板）\x01",                        # 20
            "M5409 古罗力亚斯外装（出入口）\x01",                      # 21
            "M5410 古罗力亚斯内部（飞机库入口）\x01",                  # 22
            "M5412 古罗力亚斯内部（飞机库远处）\x01",                  # 23
            "M5413 古罗力亚斯外装（甲板·夜）\x01",                    # 24
            "M5600 研究所外部\x01",                                    # 25
            "M5610 研究所内部（１层）\x01",                            # 26
            "M5611 研究所内部（２层）\x01",                            # 27
            "M5612 研究所内部（３层）\x01",                            # 28
            "M5613 研究所内部（４层）\x01",                            # 29
            "M5614 研究所内电梯\x01",                                  # 30
            "M5615 研究所内部（仅有３层BOSS房间）\x01",                # 31
            "M3100 雷斯顿水上要塞外部(正门)\x01",                      # 32
            "M3101 雷斯顿水上要塞外部(中庭)\x01",                      # 33
            "M3102 雷斯顿水上要塞外部(飞机库)\x01",                    # 34
            "M3103 雷斯顿水上要塞外部(研究设施)\x01",                  # 35
            "M3110 雷斯顿水上要塞外部(司令塔)\x01",                    # 36
            "M3112 雷斯顿水上要塞外部(研究设施)\x01",                  # 37
            "M3116 雷斯顿水上要塞外部(夜司令室)\x01",                  # 38
            "M3200 雷斯顿水上要塞内部(兵舍1F)\x01",                    # 39
            "M3201 雷斯顿水上要塞内部(兵舍2F)\x01",                    # 40
            "M3202 雷斯顿水上要塞内部(司令部1F)\x01",                  # 41
            "M3203 雷斯顿水上要塞内部(司令部2F)\x01",                  # 42
            "M3204 雷斯顿水上要塞内部(司令部3F)\x01",                  # 43
            "M3205 雷斯顿水上要塞内部(司令部2F延长)\x01",              # 44
            "M3206 雷斯顿水上要塞内部(司令部3F延长)\x01",              # 45
            "M5414 异次元的舞台(开始)\x01",                            # 46
            "M5415 异次元的舞台(终端)\x01",                            # 47
            "H3300 佐达特军用道　通行禁止\x01",                        # 48
            "取消\x01",                                                # 49
        )
    )

    Jump("loc_3519")

    label("loc_3519")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35E9"),
        (1, "loc_35F5"),
        (2, "loc_3601"),
        (3, "loc_360D"),
        (4, "loc_3619"),
        (5, "loc_3625"),
        (6, "loc_3631"),
        (7, "loc_363D"),
        (8, "loc_3649"),
        (9, "loc_3655"),
        (10, "loc_3661"),
        (11, "loc_366D"),
        (12, "loc_3679"),
        (13, "loc_3685"),
        (14, "loc_3691"),
        (15, "loc_369D"),
        (16, "loc_36A9"),
        (17, "loc_36B5"),
        (18, "loc_36C1"),
        (19, "loc_36CD"),
        (20, "loc_36D9"),
        (21, "loc_36E5"),
        (22, "loc_36F1"),
        (23, "loc_36FD"),
        (24, "loc_3709"),
        (25, "loc_3715"),
        (26, "loc_3721"),
        (27, "loc_372D"),
        (28, "loc_3739"),
        (29, "loc_3745"),
        (30, "loc_3751"),
        (31, "loc_375D"),
        (32, "loc_3769"),
        (33, "loc_3775"),
        (34, "loc_3781"),
        (35, "loc_378D"),
        (36, "loc_3799"),
        (37, "loc_37A5"),
        (38, "loc_37B1"),
        (39, "loc_37BD"),
        (40, "loc_37C9"),
        (41, "loc_37D5"),
        (42, "loc_37E1"),
        (43, "loc_37ED"),
        (44, "loc_37F9"),
        (45, "loc_3805"),
        (46, "loc_3811"),
        (47, "loc_381D"),
        (48, "loc_3829"),
        (SWITCH_DEFAULT, "loc_3835"),
    )


    label("loc_35E9")

    NewScene("ED6_DT21/M4110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_35F5")

    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3601")

    NewScene("ED6_DT21/M4112   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_360D")

    NewScene("ED6_DT21/M4113   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3619")

    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3625")

    NewScene("ED6_DT21/U2501   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3631")

    NewScene("ED6_DT21/U2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_363D")

    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3649")

    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3655")

    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3661")

    NewScene("ED6_DT21/U2600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_366D")

    NewScene("ED6_DT21/U2610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3679")

    NewScene("ED6_DT21/M5400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3685")

    NewScene("ED6_DT21/M5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3691")

    NewScene("ED6_DT21/M5402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_369D")

    NewScene("ED6_DT21/M5403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36A9")

    NewScene("ED6_DT21/M5404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36B5")

    NewScene("ED6_DT21/M5405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36C1")

    NewScene("ED6_DT21/M5406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36CD")

    NewScene("ED6_DT21/M5407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36D9")

    NewScene("ED6_DT21/M5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36E5")

    NewScene("ED6_DT21/M5409   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36F1")

    NewScene("ED6_DT21/M5410   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_36FD")

    NewScene("ED6_DT21/M5412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3709")

    NewScene("ED6_DT21/M5413   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3715")

    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3721")

    NewScene("ED6_DT21/M5610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_372D")

    NewScene("ED6_DT21/M5611   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3739")

    NewScene("ED6_DT21/M5612   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3745")

    NewScene("ED6_DT21/M5613   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3751")

    NewScene("ED6_DT21/M5614   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_375D")

    NewScene("ED6_DT21/M5615   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3769")

    NewScene("ED6_DT21/M3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3775")

    NewScene("ED6_DT21/M3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3781")

    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_378D")

    NewScene("ED6_DT21/M3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3799")

    NewScene("ED6_DT21/M3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37A5")

    NewScene("ED6_DT21/M3112   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37B1")

    NewScene("ED6_DT21/M3116   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37BD")

    NewScene("ED6_DT21/M3200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37C9")

    NewScene("ED6_DT21/M3201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37D5")

    NewScene("ED6_DT21/M3202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37E1")

    NewScene("ED6_DT21/M3203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37ED")

    NewScene("ED6_DT21/M3204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_37F9")

    NewScene("ED6_DT21/M3205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3805")

    NewScene("ED6_DT21/M3206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3811")

    NewScene("ED6_DT21/M5414   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_381D")

    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3829")

    NewScene("ED6_DT21/H3300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3842")

    label("loc_3835")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3842")

    label("loc_3842")

    Jump("loc_2EFF")

    label("loc_3845")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_2EEA end

    def Function_21_3855(): pass

    label("Function_21_3855")


    AnonymousTalk(    #20
        "\x06哪里？\x02",
    )

    Jump("loc_386A")

    label("loc_386A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B05")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7300 炼狱（第７星层）①\x01",              # 0
            "M7301 炼狱（第７星层）②\x01",              # 1
            "M7302 炼狱（第７星层）③\x01",              # 2
            "M7303 炼狱（第７星层）④\x01",              # 3
            "M7304 炼狱（第７星层）⑤\x01",              # 4
            "M7305 炼狱（第７星层）⑥\x01",              # 5
            "M7306 炼狱（第７星层）⑦\x01",              # 6
            "M7307 炼狱（第７星层）⑧\x01",              # 7
            "M7308 炼狱（第７星层）⑨\x01",              # 8
            "M7309 炼狱（第７星层）⑩\x01",              # 9
            "M7310 炼狱（第７星层）无限①开始\x01",      # 10
            "M7311 炼狱（第７星层）无限②螺旋\x01",      # 11
            "M7312 炼狱（第７星层）无限③中继\x01",      # 12
            "M7313 炼狱（第７星层）无限④BOSS\x01",      # 13
            "取消\x01",                                  # 14
        )
    )

    Jump("loc_3A09")

    label("loc_3A09")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A4D"),
        (1, "loc_3A59"),
        (2, "loc_3A65"),
        (3, "loc_3A71"),
        (4, "loc_3A7D"),
        (5, "loc_3A89"),
        (6, "loc_3A95"),
        (7, "loc_3AA1"),
        (8, "loc_3AAD"),
        (9, "loc_3AB9"),
        (10, "loc_3AC5"),
        (11, "loc_3AD1"),
        (12, "loc_3ADD"),
        (13, "loc_3AE9"),
        (SWITCH_DEFAULT, "loc_3AF5"),
    )


    label("loc_3A4D")

    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A59")

    NewScene("ED6_DT21/M7301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A65")

    NewScene("ED6_DT21/M7302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A71")

    NewScene("ED6_DT21/M7303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A7D")

    NewScene("ED6_DT21/M7304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A89")

    NewScene("ED6_DT21/M7305   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3A95")

    NewScene("ED6_DT21/M7306   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AA1")

    NewScene("ED6_DT21/M7307   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AAD")

    NewScene("ED6_DT21/M7308   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AB9")

    NewScene("ED6_DT21/M7309   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AC5")

    NewScene("ED6_DT21/M7310   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AD1")

    NewScene("ED6_DT21/M7311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3ADD")

    NewScene("ED6_DT21/M7312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AE9")

    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3B02")

    label("loc_3AF5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B02")

    label("loc_3B02")

    Jump("loc_386A")

    label("loc_3B05")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_3855 end

    def Function_22_3B15(): pass

    label("Function_22_3B15")


    AnonymousTalk(    #21
        "\x06哪里？\x02",
    )

    Jump("loc_3B2A")

    label("loc_3B2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FDC")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7400 中枢广场/埃尔赛尤号停泊地\x01",      # 0
            "M7401 中枢Ａ临近BOSS前的房间\x01",         # 1
            "M7402 中枢ＡBOSS房间\x01",                 # 2
            "M7403 中枢Ｂ临近BOSS前的房间\x01",         # 3
            "M7404 中枢ＢBOSS房间\x01",                 # 4
            "M7405 中枢Ｃ临近BOSS前的房间\x01",         # 5
            "M7406 中枢ＣBOSS房间\x01",                 # 6
            "M7407 中枢临近最终BOSS前的房间\x01",       # 7
            "M7408 中枢最终BOSS房间\x01",               # 8
            "M7409 中枢Ａ通道①\x01",                   # 9
            "M7410 中枢Ａ通道②\x01",                   # 10
            "M7411 中枢Ａ通道③\x01",                   # 11
            "M7412 中枢Ａ通道④\x01",                   # 12
            "M7413 中枢Ｂ通道①\x01",                   # 13
            "M7414 中枢Ｂ通道②\x01",                   # 14
            "M7415 中枢Ｂ通道③\x01",                   # 15
            "M7416 中枢Ｂ通道④\x01",                   # 16
            "M7417 中枢Ｂ通道⑤\x01",                   # 17
            "M7418 中枢Ｃ通道①\x01",                   # 18
            "M7419 中枢Ｃ通道②\x01",                   # 19
            "M7420 中枢Ｃ通道③\x01",                   # 20
            "M7421 中枢Ｃ通道④\x01",                   # 21
            "M7422 中枢最后通道①\x01",                 # 22
            "M7423 中枢最后通道②\x01",                 # 23
            "M7424 中枢最后通道③\x01",                 # 24
            "M7425 中枢最后通道④\x01",                 # 25
            "M7426 中枢最后通道⑤\x01",                 # 26
            "M7427 中枢最后通道⑥\x01",                 # 27
            "P0800 蕉参薤附荒野(辟静胀蝗胗?\x01",       # 28
            "M7499 最终BOSS事件用\x01",                 # 29
            "取消\x01",                                 # 30
        )
    )

    Jump("loc_3DE0")

    label("loc_3DE0")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E64"),
        (1, "loc_3E70"),
        (2, "loc_3E7C"),
        (3, "loc_3E88"),
        (4, "loc_3E94"),
        (5, "loc_3EA0"),
        (6, "loc_3EAC"),
        (7, "loc_3EB8"),
        (8, "loc_3EC4"),
        (9, "loc_3ED0"),
        (10, "loc_3EDC"),
        (11, "loc_3EE8"),
        (12, "loc_3EF4"),
        (13, "loc_3F00"),
        (14, "loc_3F0C"),
        (15, "loc_3F18"),
        (16, "loc_3F24"),
        (17, "loc_3F30"),
        (18, "loc_3F3C"),
        (19, "loc_3F48"),
        (20, "loc_3F54"),
        (21, "loc_3F60"),
        (22, "loc_3F6C"),
        (23, "loc_3F78"),
        (24, "loc_3F84"),
        (25, "loc_3F90"),
        (26, "loc_3F9C"),
        (27, "loc_3FA8"),
        (28, "loc_3FB4"),
        (29, "loc_3FC0"),
        (SWITCH_DEFAULT, "loc_3FCC"),
    )


    label("loc_3E64")

    NewScene("ED6_DT21/M7400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3E70")

    NewScene("ED6_DT21/M7401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3E7C")

    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3E88")

    NewScene("ED6_DT21/M7403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3E94")

    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EA0")

    NewScene("ED6_DT21/M7405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EAC")

    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EB8")

    NewScene("ED6_DT21/M7407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EC4")

    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3ED0")

    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EDC")

    NewScene("ED6_DT21/M7410   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EE8")

    NewScene("ED6_DT21/M7411   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3EF4")

    NewScene("ED6_DT21/M7412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F00")

    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F0C")

    NewScene("ED6_DT21/M7414   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F18")

    NewScene("ED6_DT21/M7415   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F24")

    NewScene("ED6_DT21/M7416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F30")

    NewScene("ED6_DT21/M7417   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F3C")

    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F48")

    NewScene("ED6_DT21/M7419   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F54")

    NewScene("ED6_DT21/M7420   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F60")

    NewScene("ED6_DT21/M7421   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F6C")

    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F78")

    NewScene("ED6_DT21/M7423   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F84")

    NewScene("ED6_DT21/M7424   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F90")

    NewScene("ED6_DT21/M7425   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3F9C")

    NewScene("ED6_DT21/M7426   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3FA8")

    NewScene("ED6_DT21/M7427   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3FB4")

    NewScene("ED6_DT21/P0800   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3FC0")

    NewScene("ED6_DT21/M7499   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_3FD9")

    label("loc_3FCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FD9")

    label("loc_3FD9")

    Jump("loc_3B2A")

    label("loc_3FDC")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_3B15 end

    def Function_23_3FEC(): pass

    label("Function_23_3FEC")


    AnonymousTalk(    #22
        "\x06哪里？\x02",
    )

    Jump("loc_4001")

    label("loc_4001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4088")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "E0810 天空地图（白天）\x01",      # 0
            "E1210 梅尔卡瓦内部\x01",          # 1
            "取消\x01",                        # 2
        )
    )

    Jump("loc_404C")

    label("loc_404C")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4060"),
        (1, "loc_406C"),
        (SWITCH_DEFAULT, "loc_4078"),
    )


    label("loc_4060")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4085")

    label("loc_406C")

    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_4085")

    label("loc_4078")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4085")

    label("loc_4085")

    Jump("loc_4001")

    label("loc_4088")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_3FEC end

    def Function_24_4098(): pass

    label("Function_24_4098")

    Return()

    # Function_24_4098 end

    def Function_25_4099(): pass

    label("Function_25_4099")

    EventBegin(0x0)
    OP_DA()
    OP_56(0x0)
    OP_5F(0x0)
    OP_5F(0x1)

    AnonymousTalk(    #23
        "\x06哪个？\x02",
    )

    Jump("loc_40B9")

    label("loc_40B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4318")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        10,
        100,
        1,
        (
            "片头\x01",                                # 0
            "古罗力亚斯登场\x01",                      # 1
            "辉之环出现\x01",                          # 2
            "古罗力亚斯战、辉之环上空、击落\x01",      # 3
            "辉之环崩溃\x01",                          # 4
            "取消\x01",                                # 5
        )
    )

    Jump("loc_413C")

    label("loc_413C")

    MenuEnd(0x0)
    OP_5F(0x2)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4167")
    Jump("loc_4318")

    label("loc_4167")

    FadeToDark(2000, 0, -1)
    OP_20(0x3E8)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41A5"),
        (1, "loc_41BB"),
        (2, "loc_41D8"),
        (3, "loc_422D"),
        (4, "loc_42C4"),
        (SWITCH_DEFAULT, "loc_42E1"),
    )


    label("loc_41A5")

    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Jump("loc_42E1")

    label("loc_41BB")

    OP_1D(0x1C)
    Sleep(5000)
    PlayMovie(0x0, "ED6_DT40.dat", 0x0, 0x0)
    Jump("loc_42E1")

    label("loc_41D8")

    OP_1D(0x23)
    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4217")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_4217")

    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x0)
    Jump("loc_42E1")

    label("loc_422D")

    OP_1D(0x77)
    Sleep(2000)
    PlayMovie(0x0, "ED6_DT43.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4271")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_4271")

    PlayMovie(0x0, "ED6_DT44.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42AE")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_42AE")

    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x0)
    Jump("loc_42E1")

    label("loc_42C4")

    OP_1D(0x50)
    Sleep(5000)
    PlayMovie(0x0, "ED6_DT46.dat", 0x0, 0x0)
    Jump("loc_42E1")

    label("loc_42E1")

    Sleep(1000)
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    OP_20(0x7D0)
    OP_21()
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(500)
    OP_C4(0x1, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Jump("loc_40C3")

    label("loc_4318")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_4099 end

    SaveToFile()

Try(main)
