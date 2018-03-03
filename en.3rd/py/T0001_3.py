from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '@FileName',                            # 8
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
        "Function_1_11E",          # 01, 1
        "Function_2_36E",          # 02, 2
        "Function_3_591",          # 03, 3
        "Function_4_706",          # 04, 4
        "Function_5_77A",          # 05, 5
        "Function_6_7BC",          # 06, 6
        "Function_7_7FE",          # 07, 7
        "Function_8_906",          # 08, 8
        "Function_9_9BC",          # 09, 9
        "Function_10_B0B",         # 0A, 10
        "Function_11_10C9",        # 0B, 11
        "Function_12_12DA",        # 0C, 12
        "Function_13_148A",        # 0D, 13
        "Function_14_16B7",        # 0E, 14
        "Function_15_19F1",        # 0F, 15
        "Function_16_1C41",        # 10, 16
        "Function_17_294B",        # 11, 17
        "Function_18_2AF6",        # 12, 18
        "Function_19_2E8A",        # 13, 19
        "Function_20_303F",        # 14, 20
        "Function_21_39F3",        # 15, 21
        "Function_22_3CA8",        # 16, 22
        "Function_23_4171",        # 17, 23
        "Function_24_4210",        # 18, 24
        "Function_25_4211",        # 19, 25
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06Which?\x02",
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E")

    Menu(
        1,
        10,
        32,
        1,
        (
            "3rd\x01",      # 0
            "SC\x01",       # 1
            "FC\x01",       # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EC"),
        (1, "loc_F3"),
        (2, "loc_FA"),
        (SWITCH_DEFAULT, "loc_101"),
    )


    label("loc_EC")

    Call(3, 3)
    Jump("loc_10B")

    label("loc_F3")

    Call(3, 1)
    Jump("loc_10B")

    label("loc_FA")

    Call(3, 2)
    Jump("loc_10B")

    label("loc_101")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10B")

    Jump("loc_B4")

    label("loc_10E")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_11E(): pass

    label("Function_1_11E")


    AnonymousTalk(    #1
        "\x06Which?\x02",
    )


    label("loc_128")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35E")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0020 Party and Dedicated NPL\x01",                              # 0
            "A0021 Battle Estelle, Joshua, Zin, Agate, Olivier\x01",          # 1
            "A0022 Battle Scherazard, Tita, Kloe, Kloe Formal\x01",           # 2
            "A0023 Battle Kevin, Anelace, Josette, Kurt, Ries\x01",           # 3
            "A0024 Battle Julia, Mueller, Cid, Kanone\x01",                   # 4
            "A0025 Battle Walter, Renne, Lucciola, Blueblanc\x01",            # 5
            "A0026 Battle Loewe, Weissman, Robo Joshua, Clown\x01",           # 6
            "A0027 Battle Jaeger A, Jaeger B, Kurt, Carna, Gilbert\x01",      # 7
            "A0039 SC Sitting Sprites\x01",                                   # 8
            "Cancel\x01",                                                     # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_300"),
        (1, "loc_309"),
        (2, "loc_312"),
        (3, "loc_31B"),
        (4, "loc_324"),
        (5, "loc_32D"),
        (6, "loc_336"),
        (7, "loc_33F"),
        (8, "loc_348"),
        (SWITCH_DEFAULT, "loc_351"),
    )


    label("loc_300")

    NewScene("ED6_DT21/A0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_309")

    NewScene("ED6_DT21/A0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_312")

    NewScene("ED6_DT21/A0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_31B")

    NewScene("ED6_DT21/A0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_324")

    NewScene("ED6_DT21/A0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_32D")

    NewScene("ED6_DT21/A0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_336")

    NewScene("ED6_DT21/A0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_33F")

    NewScene("ED6_DT21/A0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_348")

    NewScene("ED6_DT21/A0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_351")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_128")

    label("loc_35E")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_11E end

    def Function_2_36E(): pass

    label("Function_2_36E")


    AnonymousTalk(    #2
        "\x06Which?\x02",
    )


    label("loc_378")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_581")

    Menu(
        2,
        10,
        100,
        1,
        (
            "30 General Purpose NPL\x01",                                             # 0
            "31 Party and Dedicated NPL\x01",                                         # 1
            "32 General Purpose and dedicated NPL2/APL\x01",                          # 2
            "33 PT battle Estelle, Joshua, Zin, Agate, Olivier\x01",                  # 3
            "34 PT battle Joshua, Scherazard, Tita, Kloe\x01",                        # 4
            "35 NPC Battle Bracer Female, Thug, Sky Pirate\x01",                      # 5
            "36 NPC Battle Thin Pirate, Bracer Female 2\x01",                         # 6
            "37 NPC Battle Royal Guard, OFficer, Agent, Lola, Risha, Kanoe\x01",      # 7
            "39座りキャラ\x01",                                                       # 8
            "Cancel\x01",                                                             # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_523"),
        (1, "loc_52C"),
        (2, "loc_535"),
        (3, "loc_53E"),
        (4, "loc_547"),
        (5, "loc_550"),
        (6, "loc_559"),
        (7, "loc_562"),
        (8, "loc_56B"),
        (SWITCH_DEFAULT, "loc_574"),
    )


    label("loc_523")

    NewScene("ED6_DT21/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_52C")

    NewScene("ED6_DT21/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_535")

    NewScene("ED6_DT21/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_53E")

    NewScene("ED6_DT21/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_547")

    NewScene("ED6_DT21/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_550")

    NewScene("ED6_DT21/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_559")

    NewScene("ED6_DT21/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_562")

    NewScene("ED6_DT21/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_56B")

    NewScene("ED6_DT21/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_574")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_378")

    label("loc_581")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_36E end

    def Function_3_591(): pass

    label("Function_3_591")


    AnonymousTalk(    #3
        "\x06Which?\x02",
    )


    label("loc_59B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F6")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0040 Cassius, Kilika, Phillip (Battle)\x01",                          # 0
            "A0041 Morgan, Bodyguard, Black Hunter, Black Loewe (Battle)\x01",      # 1
            "A0042 Dedicated NPCs 1\x01",                                           # 2
            "A0045 Dedicated NPCs 2\x01",                                           # 3
            "A0043 Main Character Costumes\x01",                                    # 4
            "A0044 Main Character Costumes (Battle)\x01",                           # 5
            "Cancel\x01",                                                           # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6B3"),
        (1, "loc_6BC"),
        (2, "loc_6C5"),
        (3, "loc_6CE"),
        (4, "loc_6D7"),
        (5, "loc_6E0"),
        (SWITCH_DEFAULT, "loc_6E9"),
    )


    label("loc_6B3")

    NewScene("ED6_DT21/A0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6BC")

    NewScene("ED6_DT21/A0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6C5")

    NewScene("ED6_DT21/A0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6CE")

    NewScene("ED6_DT21/A0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6D7")

    NewScene("ED6_DT21/A0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6E0")

    NewScene("ED6_DT21/A0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59B")

    label("loc_6F6")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_591 end

    def Function_4_706(): pass

    label("Function_4_706")


    AnonymousTalk(    #4
        "\x06Which?\x02",
    )


    label("loc_710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76A")

    Menu(
        1,
        10,
        32,
        1,
        (
            "3rd\x01",      # 0
            "SC\x01",       # 1
            "FC\x01",       # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_748"),
        (1, "loc_74F"),
        (2, "loc_756"),
        (SWITCH_DEFAULT, "loc_75D"),
    )


    label("loc_748")

    Call(3, 7)
    Jump("loc_767")

    label("loc_74F")

    Call(3, 6)
    Jump("loc_767")

    label("loc_756")

    Call(3, 5)
    Jump("loc_767")

    label("loc_75D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_767")

    Jump("loc_710")

    label("loc_76A")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_706 end

    def Function_5_77A(): pass

    label("Function_5_77A")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Disabled. Please check in SC instead.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_5_77A end

    def Function_6_7BC(): pass

    label("Function_6_7BC")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Disabled. Please check in SC instead.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Return()

    # Function_6_7BC end

    def Function_7_7FE(): pass

    label("Function_7_7FE")


    AnonymousTalk(    #7
        "\x06Which?\x02",
    )


    label("loc_808")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F6")

    Menu(
        2,
        10,
        32,
        1,
        (
            "T0040 Monster List (14000-14250)\x01",      # 0
            "T0041 Monster List (14260-14500)\x01",      # 1
            "T0042 Monster List (14510-14750)\x01",      # 2
            "T0043 Monster List (14760-14890)\x01",      # 3
            "Cancel\x01",                                # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8C5"),
        (1, "loc_8CE"),
        (2, "loc_8D7"),
        (3, "loc_8E0"),
        (SWITCH_DEFAULT, "loc_8E9"),
    )


    label("loc_8C5")

    NewScene("ED6_DT21/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8CE")

    NewScene("ED6_DT21/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8D7")

    NewScene("ED6_DT21/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8E0")

    NewScene("ED6_DT21/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_8E9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_808")

    label("loc_8F6")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_7FE end

    def Function_8_906(): pass

    label("Function_8_906")


    AnonymousTalk(    #8
        "\x06Where?\x02",
    )


    label("loc_910")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AC")

    Menu(
        1,
        -1,
        32,
        1,
        (
            "■Main\x01",                     # 0
            "■Episodes\x01",                 # 1
            "■Stone Monument Jump\x01",      # 2
            "■Stone Monument Flag\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_980"),
        (1, "loc_987"),
        (2, "loc_98E"),
        (3, "loc_995"),
        (SWITCH_DEFAULT, "loc_99C"),
    )


    label("loc_980")

    Call(3, 12)
    Jump("loc_9A9")

    label("loc_987")

    Call(3, 11)
    Jump("loc_9A9")

    label("loc_98E")

    Call(3, 10)
    Jump("loc_9A9")

    label("loc_995")

    Call(3, 9)
    Jump("loc_9A9")

    label("loc_99C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A9")

    label("loc_9A9")

    Jump("loc_910")

    label("loc_9AC")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_906 end

    def Function_9_9BC(): pass

    label("Function_9_9BC")

    OP_3E(0x211, 1)

    label("loc_9C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFB")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "▼Open All Monuments\x01",         # 0
            "▼Enable All Monuments\x01",       # 1
            "▼Disable All Monuments\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A33"),
        (1, "loc_ADB"),
        (2, "loc_AE3"),
        (SWITCH_DEFAULT, "loc_AEB"),
    )


    label("loc_A33")

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
    Jump("loc_AF8")

    label("loc_ADB")

    OP_AA(65281)
    Jump("loc_AF8")

    label("loc_AE3")

    OP_AA(65282)
    Jump("loc_AF8")

    label("loc_AEB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF8")

    label("loc_AF8")

    Jump("loc_9C1")

    label("loc_AFB")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_9BC end

    def Function_10_B0B(): pass

    label("Function_10_B0B")

    OP_3E(0x211, 1)

    AnonymousTalk(    #9
        "\x06Where?\x02",
    )


    label("loc_B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B9")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "U7000 Hermit's Garden\x01",                 # 0
            "M7002 Jade Corridor 1\x01",                 # 1
            "M7005 Jade Corridor 2\x01",                 # 2
            "U4100 Grancel (Day)\x01",                   # 3
            "U4150 Grancel (Night)\x01",                 # 4
            "U4165 Grand Arena\x01",                     # 5
            "U4250 Grancel Castle\x01",                  # 6
            "M4302 Sealed Area\x01",                     # 7
            "M7100 Golden Road, Silver Road 1\x01",      # 8
            "M7104 Golden Road Boss\x01",                # 9
            "M7103 Silver Road Boss\x01",                # 10
            "M7107 Golden Road, Silver Road 2\x01",      # 11
            "U5110 Le-Locle Lodge (Day)\x01",            # 12
            "U5111 Le-Locle Lodge (Night)\x01",          # 13
            "M5503 Balstar Channel\x01",                 # 14
            "M5504 Saint-Croix Forest\x01",              # 15
            "M5513 Grimsel Fortress\x01",                # 16
            "M7200 Labyrinth of Light 1\x01",            # 17
            "M7201 Labyrinth of Light 2\x01",            # 18
            "M7203 Labyrinth of Shadow\x01",             # 19
            "M7206 Labyrinth of Light Boss\x01",         # 20
            "M4113 Erbe Scenic Route\x01",               # 21
            "U2500 Jenis Royal Academy\x01",             # 22
            "M5610 Lakeside Laboratory 1\x01",           # 23
            "M5611 Lakeside Laboratory 2\x01",           # 24
            "M5612 Lakeside Laboratory 3\x01",           # 25
            "M5613 Lakeside Laboratory 4\x01",           # 26
            "M3100 Leiston Fortress 1\x01",              # 27
            "M3203 Leiston Fortress 2\x01",              # 28
            "M3204 Leiston Fortress 3\x01",              # 29
            "M5408 Glorious Deck\x01",                   # 30
            "M5412 Glorious Hangar\x01",                 # 31
            "M5400 Glorious Sanctuary\x01",              # 32
            "M7310 Abyss Entrance\x01",                  # 33
            "Cancel\x01",                                # 34
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F11"),
        (1, "loc_F1D"),
        (2, "loc_F29"),
        (3, "loc_F35"),
        (4, "loc_F41"),
        (5, "loc_F4D"),
        (6, "loc_F59"),
        (7, "loc_F65"),
        (8, "loc_F71"),
        (9, "loc_F7D"),
        (10, "loc_F89"),
        (11, "loc_F95"),
        (12, "loc_FA1"),
        (13, "loc_FAD"),
        (14, "loc_FB9"),
        (15, "loc_FC5"),
        (16, "loc_FD1"),
        (17, "loc_FDD"),
        (18, "loc_FE9"),
        (19, "loc_FF5"),
        (20, "loc_1001"),
        (21, "loc_100D"),
        (22, "loc_1019"),
        (23, "loc_1025"),
        (24, "loc_1031"),
        (25, "loc_103D"),
        (26, "loc_1049"),
        (27, "loc_1055"),
        (28, "loc_1061"),
        (29, "loc_106D"),
        (30, "loc_1079"),
        (31, "loc_1085"),
        (32, "loc_1091"),
        (33, "loc_109D"),
        (SWITCH_DEFAULT, "loc_10A9"),
    )


    label("loc_F11")

    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F1D")

    NewScene("ED6_DT21/M7002   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F29")

    NewScene("ED6_DT21/M7005   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F35")

    NewScene("ED6_DT21/U4100   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F41")

    NewScene("ED6_DT21/U4150   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F4D")

    NewScene("ED6_DT21/U4165   ._SN", 113, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F59")

    NewScene("ED6_DT21/U4250   ._SN", 109, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F65")

    NewScene("ED6_DT21/M4302   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F71")

    NewScene("ED6_DT21/M7100   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F7D")

    NewScene("ED6_DT21/M7104   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F89")

    NewScene("ED6_DT21/M7103   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_F95")

    NewScene("ED6_DT21/M7107   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FA1")

    NewScene("ED6_DT21/U5110   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FAD")

    NewScene("ED6_DT21/U5111   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FB9")

    NewScene("ED6_DT21/M5503   ._SN", 103, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FC5")

    NewScene("ED6_DT21/M5504   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FD1")

    NewScene("ED6_DT21/M5513   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FDD")

    NewScene("ED6_DT21/M7200   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FE9")

    NewScene("ED6_DT21/M7201   ._SN", 107, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_FF5")

    NewScene("ED6_DT21/M7203   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1001")

    NewScene("ED6_DT21/M7206   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_100D")

    NewScene("ED6_DT21/M4113   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1019")

    NewScene("ED6_DT21/U2500   ._SN", 131, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1025")

    NewScene("ED6_DT21/M5610   ._SN", 136, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1031")

    NewScene("ED6_DT21/M5611   ._SN", 137, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_103D")

    NewScene("ED6_DT21/M5612   ._SN", 129, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1049")

    NewScene("ED6_DT21/M5613   ._SN", 112, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1055")

    NewScene("ED6_DT21/M3100   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1061")

    NewScene("ED6_DT21/M3203   ._SN", 130, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_106D")

    NewScene("ED6_DT21/M3204   ._SN", 127, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1079")

    NewScene("ED6_DT21/M5408   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1085")

    NewScene("ED6_DT21/M5412   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_1091")

    NewScene("ED6_DT21/M5400   ._SN", 129, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_109D")

    NewScene("ED6_DT21/M7310   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_10B6")

    label("loc_10A9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10B6")

    label("loc_10B6")

    Jump("loc_B1A")

    label("loc_10B9")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_B0B end

    def Function_11_10C9(): pass

    label("Function_11_10C9")


    AnonymousTalk(    #10
        "\x06Where?\x02",
    )


    label("loc_10D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12CA")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "T3121 地下実験場\x01",                          # 0
            "E0102 飛行船（空賊)\x01",                       # 1
            "T4206 グランセル城外部(パーティ会場)\x01",      # 2
            "C5416 グロリアス　星辰の間\x01",                # 3
            "P9000 Episode Room 1\x01",                      # 4
            "P9001 Episode Room 2\x01",                      # 5
            "P9002 Episode Room 3\x01",                      # 6
            "T1500 Fishing 1\x01",                           # 7
            "C4203 Fishing 2\x01",                           # 8
            "R2201 Fishing 3\x01",                           # 9
            "R2201 Gull Seaside Way\x01",                    # 10
            "E1001 Grand Arena (Night)\x01",                 # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_122A"),
        (1, "loc_1236"),
        (2, "loc_1242"),
        (3, "loc_124E"),
        (4, "loc_125A"),
        (5, "loc_1266"),
        (6, "loc_1272"),
        (7, "loc_127E"),
        (8, "loc_128A"),
        (9, "loc_1296"),
        (10, "loc_12A2"),
        (11, "loc_12AE"),
        (SWITCH_DEFAULT, "loc_12BA"),
    )


    label("loc_122A")

    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_1236")

    NewScene("ED6_DT21/E0102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_1242")

    NewScene("ED6_DT21/T4206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_124E")

    NewScene("ED6_DT21/C5416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_125A")

    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_1266")

    NewScene("ED6_DT21/P9001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_1272")

    NewScene("ED6_DT21/P9002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_127E")

    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_128A")

    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_1296")

    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_12A2")

    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_12AE")

    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_12C7")

    label("loc_12BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12C7")

    label("loc_12C7")

    Jump("loc_10D3")

    label("loc_12CA")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_10C9 end

    def Function_12_12DA(): pass

    label("Function_12_12DA")


    AnonymousTalk(    #11
        "\x06Where?\x02",
    )


    label("loc_12E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_147A")

    Menu(
        2,
        -1,
        32,
        1,
        (
            "Base, Clinic\x01",                                    # 0
            "Prologue\x01",                                        # 1
            "1st Plane (Jade Corridor)\x01",                       # 2
            "2nd Plane (Grancel)\x01",                             # 3
            "3rd Plane (Golden Road, Silver Road)\x01",            # 4
            "4th Plane (Le-Locle)\x01",                            # 5
            "5th Plane (Labyrinth of Light and Shadows)\x01",      # 6
            "6th Plane (Various)\x01",                             # 7
            "7th Plane (Purgatory)\x01",                           # 8
            "Phantasmagoria\x01",                                  # 9
            "Epilogue\x01",                                        # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_141D"),
        (1, "loc_1424"),
        (2, "loc_142B"),
        (3, "loc_1432"),
        (4, "loc_1439"),
        (5, "loc_1440"),
        (6, "loc_1447"),
        (7, "loc_144E"),
        (8, "loc_1455"),
        (9, "loc_145C"),
        (10, "loc_1463"),
        (SWITCH_DEFAULT, "loc_146A"),
    )


    label("loc_141D")

    Call(3, 13)
    Jump("loc_1477")

    label("loc_1424")

    Call(3, 14)
    Jump("loc_1477")

    label("loc_142B")

    Call(3, 15)
    Jump("loc_1477")

    label("loc_1432")

    Call(3, 16)
    Jump("loc_1477")

    label("loc_1439")

    Call(3, 17)
    Jump("loc_1477")

    label("loc_1440")

    Call(3, 18)
    Jump("loc_1477")

    label("loc_1447")

    Call(3, 19)
    Jump("loc_1477")

    label("loc_144E")

    Call(3, 20)
    Jump("loc_1477")

    label("loc_1455")

    Call(3, 21)
    Jump("loc_1477")

    label("loc_145C")

    Call(3, 22)
    Jump("loc_1477")

    label("loc_1463")

    Call(3, 23)
    Jump("loc_1477")

    label("loc_146A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1477")

    label("loc_1477")

    Jump("loc_12E4")

    label("loc_147A")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_12DA end

    def Function_13_148A(): pass

    label("Function_13_148A")


    AnonymousTalk(    #12
        "\x06Where?\x02",
    )


    label("loc_1494")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A7")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U7000 隠者の庭園（拠点）\x01",                 # 0
            "U7001 隠者の庭園（拠点）中央通路\x01",         # 1
            "U7002 隠者の庭園（拠点）左通路\x01",           # 2
            "U7003 隠者の庭園（拠点）右通路\x01",           # 3
            "U7004 隠者の庭園（拠点）全体マップ\x01",       # 4
            "P7000 紫苑の家（雪の救貧院）外\x01",           # 5
            "P7010 紫苑の家（雪の救貧院）内\x01",           # 6
            "P7011 紫苑の家（雪の救貧院）内\x01",           # 7
            "P7012 紫苑の家/螺旋階段・通路\x01",            # 8
            "P7013 紫苑の家/始まりの地（ドーム）\x01",      # 9
            "Cancel\x01",                                   # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_161F"),
        (1, "loc_162B"),
        (2, "loc_1637"),
        (3, "loc_1643"),
        (4, "loc_164F"),
        (5, "loc_165B"),
        (6, "loc_1667"),
        (7, "loc_1673"),
        (8, "loc_167F"),
        (9, "loc_168B"),
        (SWITCH_DEFAULT, "loc_1697"),
    )


    label("loc_161F")

    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_162B")

    NewScene("ED6_DT21/U7001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_1637")

    NewScene("ED6_DT21/U7002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_1643")

    NewScene("ED6_DT21/U7003   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_164F")

    NewScene("ED6_DT21/U7004   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_165B")

    NewScene("ED6_DT21/P7000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_1667")

    NewScene("ED6_DT21/P7010   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_1673")

    NewScene("ED6_DT21/P7011   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_167F")

    NewScene("ED6_DT21/P7012   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_168B")

    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16A4")

    label("loc_1697")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16A4")

    label("loc_16A4")

    Jump("loc_1494")

    label("loc_16A7")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_148A end

    def Function_14_16B7(): pass

    label("Function_14_16B7")


    AnonymousTalk(    #13
        "\x06Where?\x02",
    )


    label("loc_16C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E1")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "E1100 ルシタニア号外部\x01",                            # 0
            "E1110 ルシタニア号内部（舞踏会会場）\x01",              # 1
            "E1111 ルシタニア号内部（プライベートエリア）\x01",      # 2
            "E1200 メルカバ外部\x01",                                # 3
            "E1210 メルカバ内部\x01",                                # 4
            "E0811 スカイマップ（夜）\x01",                          # 5
            "E0700 国際定期船《グレトナ号》外部\x01",                # 6
            "E0710 国際定期船《グレトナ号》内部\x01",                # 7
            "T4105 グランセル飛行場(アルセイユ有り)\x01",            # 8
            "T4131 大聖堂\x01",                                      # 9
            "T4144 大聖堂地下（ドーム）\x01",                        # 10
            "T4145 大聖堂地下（螺旋階段/通路）\x01",                 # 11
            "E0900 水上マップ\x01",                                  # 12
            "T4152 王都グランセル外部（西街区、夜）\x01",            # 13
            "T4151 王都グランセル外部（東街区、夜）\x01",            # 14
            "T4404 王都グランセル外部（波止場２、夜）\x01",          # 15
            "Cancel\x01",                                            # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1911"),
        (1, "loc_191D"),
        (2, "loc_1929"),
        (3, "loc_1935"),
        (4, "loc_1941"),
        (5, "loc_194D"),
        (6, "loc_1959"),
        (7, "loc_1965"),
        (8, "loc_1971"),
        (9, "loc_197D"),
        (10, "loc_1989"),
        (11, "loc_1995"),
        (12, "loc_19A1"),
        (13, "loc_19AD"),
        (14, "loc_19B9"),
        (15, "loc_19C5"),
        (SWITCH_DEFAULT, "loc_19D1"),
    )


    label("loc_1911")

    NewScene("ED6_DT21/E1100   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_191D")

    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1929")

    NewScene("ED6_DT21/E1111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1935")

    NewScene("ED6_DT21/E1200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1941")

    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_194D")

    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1959")

    NewScene("ED6_DT21/E0700   ._SN", 104, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1965")

    NewScene("ED6_DT21/E0710   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1971")

    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_197D")

    NewScene("ED6_DT21/T4131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1989")

    NewScene("ED6_DT21/T4144   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_1995")

    NewScene("ED6_DT21/T4145   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_19A1")

    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_19AD")

    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_19B9")

    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_19C5")

    NewScene("ED6_DT21/T4404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_19DE")

    label("loc_19D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19DE")

    label("loc_19DE")

    Jump("loc_16C1")

    label("loc_19E1")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_16B7 end

    def Function_15_19F1(): pass

    label("Function_15_19F1")


    AnonymousTalk(    #14
        "\x06Where?\x02",
    )


    label("loc_19FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C31")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7001 翡翠回廊①(ティータ)\x01",                        # 0
            "M7002 翡翠回廊②(アルセイユ)\x01",                      # 1
            "M7003 翡翠回廊③(螺旋階段１)\x01",                      # 2
            "M7004 翡翠回廊④(螺旋階段２)\x01",                      # 3
            "M7005 翡翠回廊⑤(ボス部屋)\x01",                        # 4
            "M7006 翡翠回廊⑥(エレベータ)\x01",                      # 5
            "M7007 翡翠回廊⑦(ｱﾙｾｲﾕ発進ｲﾍﾞﾝﾄ用)\x01",      # 6
            "P0310 アルセイユ内部　甲板連絡通路\x01",                # 7
            "P0311 アルセイユ内部　連絡通路１\x01",                  # 8
            "P0312 アルセイユ内部　連絡通路２\x01",                  # 9
            "P0313 アルセイユ内部　船倉\x01",                        # 10
            "Cancel\x01",                                            # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B9D"),
        (1, "loc_1BA9"),
        (2, "loc_1BB5"),
        (3, "loc_1BC1"),
        (4, "loc_1BCD"),
        (5, "loc_1BD9"),
        (6, "loc_1BE5"),
        (7, "loc_1BF1"),
        (8, "loc_1BFD"),
        (9, "loc_1C09"),
        (10, "loc_1C15"),
        (SWITCH_DEFAULT, "loc_1C21"),
    )


    label("loc_1B9D")

    NewScene("ED6_DT21/M7001   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BA9")

    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BB5")

    NewScene("ED6_DT21/M7003   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BC1")

    NewScene("ED6_DT21/M7004   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BCD")

    NewScene("ED6_DT21/M7005   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BD9")

    NewScene("ED6_DT21/M7006   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BE5")

    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BF1")

    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1BFD")

    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1C09")

    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1C15")

    NewScene("ED6_DT21/P0313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2E")

    label("loc_1C21")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C2E")

    label("loc_1C2E")

    Jump("loc_19FB")

    label("loc_1C31")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_19F1 end

    def Function_16_1C41(): pass

    label("Function_16_1C41")


    AnonymousTalk(    #15
        "\x06Where?\x02",
    )


    label("loc_1C4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_293B")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U4406 王都グランセル外部（波止場山猫号あり)\x01",                 # 0
            "U4100 王都グランセル外部（南街区）\x01",                          # 1
            "U4101 王都グランセル外部（東街区）\x01",                          # 2
            "U4102 王都グランセル外部（西街区）\x01",                          # 3
            "U4103 王都グランセル外部（北街区）\x01",                          # 4
            "U4104 王都グランセル外部（闘技場内側）\x01",                      # 5
            "U4106 グランセル飛行場(アルセイユなし)\x01",                      # 6
            "U4110 民家１.２.６.７.８\x01",                                    # 7
            "U4111 民家３.４.５\x01",                                          # 8
            "U4120 武器屋、工房\x01",                                          # 9
            "U4121 ギルド、釣公師団本部\x01",                                  # 10
            "U4122 エーデル百貨店、空港受付\x01",                              # 11
            "U4130 酒場、コーヒーハウス、リベール通信社\x01",                  # 12
            "U4131 大聖堂\x01",                                                # 13
            "U4132 ホテル\x01",                                                # 14
            "U4135 歴史資料館\x01",                                            # 15
            "U4136 グランアリーナ\x01",                                        # 16
            "U4138 帝國大使館内部\x01",                                        # 17
            "U4139 共和国大使館内部\x01",                                      # 18
            "U4143 闇商人の店内部\x01",                                        # 19
            "U4400 王都グランセル外部（波止場１）\x01",                        # 20
            "U4401 王都グランセル外部（波止場２）\x01",                        # 21
            "U4402 王都グランセル外部（波止場倉庫内部）\x01",                  # 22
            "U4403 王都グランセル外部（波止場ｵﾙｸﾞｲﾕ倉庫内部）\x01",      # 23
            "U4150 王都グランセル外部（南街区、夜）\x01",                      # 24
            "U4151 王都グランセル外部（東街区、夜）\x01",                      # 25
            "U4152 王都グランセル外部（西街区、夜）\x01",                      # 26
            "U4153 王都グランセル外部（北街区、夜）\x01",                      # 27
            "U4203 グランセル城外部(町と接続)（夜）\x01",                      # 28
            "U4204 グランセル城外部(空中庭園)（夜）\x01",                      # 29
            "U4205 グランセル城外部(女王のテラス)（夜）\x01",                  # 30
            "U4250 グランセル城内部(広間)（夜）\x01",                          # 31
            "U4251 グランセル城内部(饗応の間)（夜）\x01",                      # 32
            "U4252 グランセル城内部(行政区)（夜）\x01",                        # 33
            "U4253 グランセル城内部(親衛隊詰所)（夜）\x01",                    # 34
            "U4254 グランセル城内部(メイド部屋)（夜）\x01",                    # 35
            "U4255 グランセル城内部(厨房)（夜）\x01",                          # 36
            "U4260 グランセル城内部(謁見の間)（夜）\x01",                      # 37
            "U4261 グランセル城内部(二階右翼)（夜）\x01",                      # 38
            "U4262 グランセル城内部(二階左翼)（夜）\x01",                      # 39
            "U4270 グランセル城内部(女王宮)（夜）\x01",                        # 40
            "U4280 グランセル城内部(地下倉庫)（夜）\x01",                      # 41
            "U4241 グランセル城内部(封印の間)\x01",                            # 42
            "M4300 封印区画（最上層）\x01",                                    # 43
            "M4302 封印区画（最下層）\x01",                                    # 44
            "M4303 封印区画（ボス部屋）\x01",                                  # 45
            "M4308 封印区画（エレベータ部屋）\x01",                            # 46
            "U4123 ギルド（夜）\x01",                                          # 47
            "U4133 ホテル（夜）\x01",                                          # 48
            "U4134 大聖堂（夜）\x01",                                          # 49
            "U4137 コーヒーハウス（夜）\x01",                                  # 50
            "U4404 王都グランセル外部（波止場２夜）\x01",                      # 51
            "U4405 王都グランセル外部（波止場倉庫内部夜）\x01",                # 52
            "U4156 グランセル飛行場(夜アルセイユ無し)\x01",                    # 53
            "U4160 民家１.２.６.７.８（夜）\x01",                              # 54
            "U4161 民家３.４.５（夜）\x01",                                    # 55
            "U4162 歴史資料館（夜）\x01",                                      # 56
            "U4163 帝國大使館内部（夜）\x01",                                  # 57
            "U4164 闇商人の店内部（夜）\x01",                                  # 58
            "U4165 グランアリーナ(受付、控え室)（夜）\x01",                    # 59
            "U4166 グランアリーナ（闘技場内側）（夜）\x01",                    # 60
            "U4167 波止場倉庫内部（オルグイユ倉庫内部）（夜）\x01",            # 61
            "U4168 王都グランセル外部（波止場山猫号あり）（夜）\x01",          # 62
            "U4169 王都グランセル・発着場受付、釣公師団本部（夜）\x01",        # 63
            "E0110 飛行船（空賊用）内部\x01",                                  # 64
            "U4200 グランセル城外部(町と接続)\x01",                            # 65
            "Cancel\x01",                                                      # 66
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2613"),
        (1, "loc_261F"),
        (2, "loc_262B"),
        (3, "loc_2637"),
        (4, "loc_2643"),
        (5, "loc_264F"),
        (6, "loc_265B"),
        (7, "loc_2667"),
        (8, "loc_2673"),
        (9, "loc_267F"),
        (10, "loc_268B"),
        (11, "loc_2697"),
        (12, "loc_26A3"),
        (13, "loc_26AF"),
        (14, "loc_26BB"),
        (15, "loc_26C7"),
        (16, "loc_26D3"),
        (17, "loc_26DF"),
        (18, "loc_26EB"),
        (19, "loc_26F7"),
        (20, "loc_2703"),
        (21, "loc_270F"),
        (22, "loc_271B"),
        (23, "loc_2727"),
        (24, "loc_2733"),
        (25, "loc_273F"),
        (26, "loc_274B"),
        (27, "loc_2757"),
        (28, "loc_2763"),
        (29, "loc_276F"),
        (30, "loc_277B"),
        (31, "loc_2787"),
        (32, "loc_2793"),
        (33, "loc_279F"),
        (34, "loc_27AB"),
        (35, "loc_27B7"),
        (36, "loc_27C3"),
        (37, "loc_27CF"),
        (38, "loc_27DB"),
        (39, "loc_27E7"),
        (40, "loc_27F3"),
        (41, "loc_27FF"),
        (42, "loc_280B"),
        (43, "loc_2817"),
        (44, "loc_2823"),
        (45, "loc_282F"),
        (46, "loc_283B"),
        (47, "loc_2847"),
        (48, "loc_2853"),
        (49, "loc_285F"),
        (50, "loc_286B"),
        (51, "loc_2877"),
        (52, "loc_2883"),
        (53, "loc_288F"),
        (54, "loc_289B"),
        (55, "loc_28A7"),
        (56, "loc_28B3"),
        (57, "loc_28BF"),
        (58, "loc_28CB"),
        (59, "loc_28D7"),
        (60, "loc_28E3"),
        (61, "loc_28EF"),
        (62, "loc_28FB"),
        (63, "loc_2907"),
        (64, "loc_2913"),
        (65, "loc_291F"),
        (SWITCH_DEFAULT, "loc_292B"),
    )


    label("loc_2613")

    NewScene("ED6_DT21/U4406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_261F")

    NewScene("ED6_DT21/U4100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_262B")

    NewScene("ED6_DT21/U4101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2637")

    NewScene("ED6_DT21/U4102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2643")

    NewScene("ED6_DT21/U4103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_264F")

    NewScene("ED6_DT21/U4104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_265B")

    NewScene("ED6_DT21/U4106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2667")

    NewScene("ED6_DT21/U4110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2673")

    NewScene("ED6_DT21/U4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_267F")

    NewScene("ED6_DT21/U4120   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_268B")

    NewScene("ED6_DT21/U4121   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2697")

    NewScene("ED6_DT21/U4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26A3")

    NewScene("ED6_DT21/U4130   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26AF")

    NewScene("ED6_DT21/U4131   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26BB")

    NewScene("ED6_DT21/U4132   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26C7")

    NewScene("ED6_DT21/U4135   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26D3")

    NewScene("ED6_DT21/U4136   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26DF")

    NewScene("ED6_DT21/U4138   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26EB")

    NewScene("ED6_DT21/U4139   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_26F7")

    NewScene("ED6_DT21/U4143   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2703")

    NewScene("ED6_DT21/U4400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_270F")

    NewScene("ED6_DT21/U4401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_271B")

    NewScene("ED6_DT21/U4402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2727")

    NewScene("ED6_DT21/U4403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2733")

    NewScene("ED6_DT21/U4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_273F")

    NewScene("ED6_DT21/U4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_274B")

    NewScene("ED6_DT21/U4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2757")

    NewScene("ED6_DT21/U4153   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2763")

    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_276F")

    NewScene("ED6_DT21/U4204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_277B")

    NewScene("ED6_DT21/U4205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2787")

    NewScene("ED6_DT21/U4250   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2793")

    NewScene("ED6_DT21/U4251   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_279F")

    NewScene("ED6_DT21/U4252   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27AB")

    NewScene("ED6_DT21/U4253   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27B7")

    NewScene("ED6_DT21/U4254   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27C3")

    NewScene("ED6_DT21/U4255   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27CF")

    NewScene("ED6_DT21/U4260   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27DB")

    NewScene("ED6_DT21/U4261   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27E7")

    NewScene("ED6_DT21/U4262   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27F3")

    NewScene("ED6_DT21/U4270   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_27FF")

    NewScene("ED6_DT21/U4280   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_280B")

    NewScene("ED6_DT21/U4241   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2817")

    NewScene("ED6_DT21/M4300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2823")

    NewScene("ED6_DT21/M4302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_282F")

    NewScene("ED6_DT21/M4303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_283B")

    NewScene("ED6_DT21/M4308   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2847")

    NewScene("ED6_DT21/U4123   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2853")

    NewScene("ED6_DT21/U4133   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_285F")

    NewScene("ED6_DT21/U4134   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_286B")

    NewScene("ED6_DT21/U4137   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2877")

    NewScene("ED6_DT21/U4404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2883")

    NewScene("ED6_DT21/U4405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_288F")

    NewScene("ED6_DT21/U4156   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_289B")

    NewScene("ED6_DT21/U4160   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28A7")

    NewScene("ED6_DT21/U4161   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28B3")

    NewScene("ED6_DT21/U4162   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28BF")

    NewScene("ED6_DT21/U4163   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28CB")

    NewScene("ED6_DT21/U4164   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28D7")

    NewScene("ED6_DT21/U4165   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28E3")

    NewScene("ED6_DT21/U4166   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28EF")

    NewScene("ED6_DT21/U4167   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_28FB")

    NewScene("ED6_DT21/U4168   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2907")

    NewScene("ED6_DT21/U4169   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_2913")

    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_291F")

    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2938")

    label("loc_292B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2938")

    label("loc_2938")

    Jump("loc_1C4B")

    label("loc_293B")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_1C41 end

    def Function_17_294B(): pass

    label("Function_17_294B")


    AnonymousTalk(    #16
        "\x06Where?\x02",
    )


    label("loc_2955")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AE6")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7100 金の道・銀の道　分岐マップ\x01",      # 0
            "M7101 銀の道エリア①\x01",                  # 1
            "M7102 金の道エリア①\x01",                  # 2
            "M7103 銀の道エリア②\x01",                  # 3
            "M7104 金の道エリア②\x01",                  # 4
            "M7105 銀の道エリア③(銀ボス部屋)\x01",      # 5
            "M7106 金の道エリア③(金ボス部屋)\x01",      # 6
            "M7107 金の道・銀の道　合流マップ\x01",      # 7
            "Cancel\x01",                                # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A76"),
        (1, "loc_2A82"),
        (2, "loc_2A8E"),
        (3, "loc_2A9A"),
        (4, "loc_2AA6"),
        (5, "loc_2AB2"),
        (6, "loc_2ABE"),
        (7, "loc_2ACA"),
        (SWITCH_DEFAULT, "loc_2AD6"),
    )


    label("loc_2A76")

    NewScene("ED6_DT21/M7100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2A82")

    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2A8E")

    NewScene("ED6_DT21/M7102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2A9A")

    NewScene("ED6_DT21/M7103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2AA6")

    NewScene("ED6_DT21/M7104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2AB2")

    NewScene("ED6_DT21/M7105   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2ABE")

    NewScene("ED6_DT21/M7106   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2ACA")

    NewScene("ED6_DT21/M7107   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2AE3")

    label("loc_2AD6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AE3")

    label("loc_2AE3")

    Jump("loc_2955")

    label("loc_2AE6")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_294B end

    def Function_18_2AF6(): pass

    label("Function_18_2AF6")


    AnonymousTalk(    #17
        "\x06Where?\x02",
    )


    label("loc_2B00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E7A")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "U5100 ル＝ロックル訓練場外観\x01",                  # 0
            "U5102 ル＝ロックル訓練場外観（夜異次元）\x01",      # 1
            "U5110 ル＝ロックル訓練場内部\x01",                  # 2
            "U5111 ル＝ロックル訓練場内部（夜）\x01",            # 3
            "M5503 バルスタール水道入口\x01",                    # 4
            "M5500 バルスタール水道①\x01",                      # 5
            "M5501 バルスタール水道②\x01",                      # 6
            "M5502 バルスタール水道③\x01",                      # 7
            "M5503 バルスタール水道ボス部屋\x01",                # 8
            "M5504 サントクロワの森①\x01",                      # 9
            "M5505 サントクロワの森②\x01",                      # 10
            "M5506 サントクロワの森③\x01",                      # 11
            "M5512 サントクロワの森④\x01",                      # 12
            "M5507 サントクロワの森ボス部屋\x01",                # 13
            "M5508 グリムゼル小要塞①\x01",                      # 14
            "M5509 グリムゼル小要塞②\x01",                      # 15
            "M5510 グリムゼル小要塞③\x01",                      # 16
            "M5511 グリムゼル小要塞④\x01",                      # 17
            "M5513 グリムゼル小要塞ボス部屋\x01",                # 18
            "Cancel\x01",                                        # 19
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D86"),
        (1, "loc_2D92"),
        (2, "loc_2D9E"),
        (3, "loc_2DAA"),
        (4, "loc_2DB6"),
        (5, "loc_2DC2"),
        (6, "loc_2DCE"),
        (7, "loc_2DDA"),
        (8, "loc_2DE6"),
        (9, "loc_2DF2"),
        (10, "loc_2DFE"),
        (11, "loc_2E0A"),
        (12, "loc_2E16"),
        (13, "loc_2E22"),
        (14, "loc_2E2E"),
        (15, "loc_2E3A"),
        (16, "loc_2E46"),
        (17, "loc_2E52"),
        (18, "loc_2E5E"),
        (SWITCH_DEFAULT, "loc_2E6A"),
    )


    label("loc_2D86")

    NewScene("ED6_DT21/U5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2D92")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2D9E")

    NewScene("ED6_DT21/U5110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DAA")

    NewScene("ED6_DT21/U5111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DB6")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DC2")

    NewScene("ED6_DT21/M5500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DCE")

    NewScene("ED6_DT21/M5501   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DDA")

    NewScene("ED6_DT21/M5502   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DE6")

    NewScene("ED6_DT21/M5503   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DF2")

    NewScene("ED6_DT21/M5504   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2DFE")

    NewScene("ED6_DT21/M5505   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E0A")

    NewScene("ED6_DT21/M5506   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E16")

    NewScene("ED6_DT21/M5512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E22")

    NewScene("ED6_DT21/M5507   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E2E")

    NewScene("ED6_DT21/M5508   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E3A")

    NewScene("ED6_DT21/M5509   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E46")

    NewScene("ED6_DT21/M5510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E52")

    NewScene("ED6_DT21/M5511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E5E")

    NewScene("ED6_DT21/M5513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2E77")

    label("loc_2E6A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E77")

    label("loc_2E77")

    Jump("loc_2B00")

    label("loc_2E7A")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_2AF6 end

    def Function_19_2E8A(): pass

    label("Function_19_2E8A")


    AnonymousTalk(    #18
        "\x06Where?\x02",
    )


    label("loc_2E94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_302F")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7200 光エリアマップ　１－１\x01",        # 0
            "M7201 光エリアマップ　１－２\x01",        # 1
            "M7202 影エリアマップ　１\x01",            # 2
            "M7203 影エリアマップ　２\x01",            # 3
            "M7204 光エリアマップ　２－１\x01",        # 4
            "M7205 光エリアマップ　２－２\x01",        # 5
            "M7206 光エリアマップボス前通路\x01",      # 6
            "M7207 光エリアマップボス部屋\x01",        # 7
            "Cancel\x01",                              # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FBF"),
        (1, "loc_2FCB"),
        (2, "loc_2FD7"),
        (3, "loc_2FE3"),
        (4, "loc_2FEF"),
        (5, "loc_2FFB"),
        (6, "loc_3007"),
        (7, "loc_3013"),
        (SWITCH_DEFAULT, "loc_301F"),
    )


    label("loc_2FBF")

    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_2FCB")

    NewScene("ED6_DT21/M7201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_2FD7")

    NewScene("ED6_DT21/M7202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_2FE3")

    NewScene("ED6_DT21/M7203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_2FEF")

    NewScene("ED6_DT21/M7204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_2FFB")

    NewScene("ED6_DT21/M7205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_3007")

    NewScene("ED6_DT21/M7206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_3013")

    NewScene("ED6_DT21/M7207   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_302C")

    label("loc_301F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_302C")

    label("loc_302C")

    Jump("loc_2E94")

    label("loc_302F")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_2E8A end

    def Function_20_303F(): pass

    label("Function_20_303F")


    AnonymousTalk(    #19
        "\x06Where?\x02",
    )


    label("loc_3049")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E3")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M4110 エルベ周遊道①\x01",                                # 0
            "M4111 エルベ周遊道②\x01",                                # 1
            "M4112 エルベ周遊道③\x01",                                # 2
            "M4113 エルベ周遊道④\x01",                                # 3
            "U2500 ジェニス王立学院外部\x01",                          # 4
            "U2501 ジェニス王立学院旧校舎への道\x01",                  # 5
            "U2510 ジェニス王立学院（本館）\x01",                      # 6
            "U2511 ジェニス王立学院（クラブハウス）\x01",              # 7
            "U2512 ジェニス王立学院（寮）\x01",                        # 8
            "U2513 ジェニス王立学院（講堂）\x01",                      # 9
            "U2600 王立学院旧校舎外部\x01",                            # 10
            "U2610 王立学院旧校舎内部\x01",                            # 11
            "M5400 グロリアス内部（エステル監禁部屋）\x01",            # 12
            "M5401 グロリアス内部（ワイスマンの間）\x01",              # 13
            "M5402 グロリアス内部（甲板方面通路）\x01",                # 14
            "M5403 グロリアス内部（甲板～昇降口方面通路）\x01",        # 15
            "M5404 グロリアス内部（昇降口～格納庫方面通路）\x01",      # 16
            "M5405 グロリアス内部（格納庫ハズレ）\x01",                # 17
            "M5406 グロリアス内部（格納庫アタリ）\x01",                # 18
            "M5407 グロリアス内部（エレベーター箱）\x01",              # 19
            "M5408 グロリアス外装（甲板）\x01",                        # 20
            "M5409 グロリアス外装（昇降口）\x01",                      # 21
            "M5410 グロリアス内部（格納庫入り口）\x01",                # 22
            "M5412 グロリアス内部（格納庫ハズレ）\x01",                # 23
            "M5413 グロリアス外装（甲板・夜）\x01",                    # 24
            "M5600 研究所外観\x01",                                    # 25
            "M5610 研究所内部（１階）\x01",                            # 26
            "M5611 研究所内部（２階）\x01",                            # 27
            "M5612 研究所内部（３階）\x01",                            # 28
            "M5613 研究所内部（４階）\x01",                            # 29
            "M5614 研究所内エレベーター\x01",                          # 30
            "M5615 研究所内部（３階ボス部屋のみ）\x01",                # 31
            "M3100 レイストン水上要塞外観(正門)\x01",                  # 32
            "M3101 レイストン水上要塞外観(中庭)\x01",                  # 33
            "M3102 レイストン水上要塞外観(格納庫)\x01",                # 34
            "M3103 レイストン水上要塞外観(研究施設)\x01",              # 35
            "M3110 レイストン水上要塞外観(司令塔)\x01",                # 36
            "M3112 レイストン水上要塞外観(研究施設)\x01",              # 37
            "M3116 レイストン水上要塞外観(夜司令室)\x01",              # 38
            "M3200 レイストン水上要塞内部(兵舎1F)\x01",                # 39
            "M3201 レイストン水上要塞内部(兵舎2F)\x01",                # 40
            "M3202 レイストン水上要塞内部(司令部1F)\x01",              # 41
            "M3203 レイストン水上要塞内部(司令部2F)\x01",              # 42
            "M3204 レイストン水上要塞内部(司令部3F)\x01",              # 43
            "M3205 レイストン水上要塞内部(司令部2F延長)\x01",          # 44
            "M3206 レイストン水上要塞内部(司令部3F延長)\x01",          # 45
            "M5414 異次元の舞台(開始)\x01",                            # 46
            "M5415 異次元の舞台(終端)\x01",                            # 47
            "H3300 ソルダート軍用路　通行止め\x01",                    # 48
            "Cancel\x01",                                              # 49
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3787"),
        (1, "loc_3793"),
        (2, "loc_379F"),
        (3, "loc_37AB"),
        (4, "loc_37B7"),
        (5, "loc_37C3"),
        (6, "loc_37CF"),
        (7, "loc_37DB"),
        (8, "loc_37E7"),
        (9, "loc_37F3"),
        (10, "loc_37FF"),
        (11, "loc_380B"),
        (12, "loc_3817"),
        (13, "loc_3823"),
        (14, "loc_382F"),
        (15, "loc_383B"),
        (16, "loc_3847"),
        (17, "loc_3853"),
        (18, "loc_385F"),
        (19, "loc_386B"),
        (20, "loc_3877"),
        (21, "loc_3883"),
        (22, "loc_388F"),
        (23, "loc_389B"),
        (24, "loc_38A7"),
        (25, "loc_38B3"),
        (26, "loc_38BF"),
        (27, "loc_38CB"),
        (28, "loc_38D7"),
        (29, "loc_38E3"),
        (30, "loc_38EF"),
        (31, "loc_38FB"),
        (32, "loc_3907"),
        (33, "loc_3913"),
        (34, "loc_391F"),
        (35, "loc_392B"),
        (36, "loc_3937"),
        (37, "loc_3943"),
        (38, "loc_394F"),
        (39, "loc_395B"),
        (40, "loc_3967"),
        (41, "loc_3973"),
        (42, "loc_397F"),
        (43, "loc_398B"),
        (44, "loc_3997"),
        (45, "loc_39A3"),
        (46, "loc_39AF"),
        (47, "loc_39BB"),
        (48, "loc_39C7"),
        (SWITCH_DEFAULT, "loc_39D3"),
    )


    label("loc_3787")

    NewScene("ED6_DT21/M4110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3793")

    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_379F")

    NewScene("ED6_DT21/M4112   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37AB")

    NewScene("ED6_DT21/M4113   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37B7")

    NewScene("ED6_DT21/U2500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37C3")

    NewScene("ED6_DT21/U2501   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37CF")

    NewScene("ED6_DT21/U2510   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37DB")

    NewScene("ED6_DT21/U2511   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37E7")

    NewScene("ED6_DT21/U2512   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37F3")

    NewScene("ED6_DT21/U2513   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_37FF")

    NewScene("ED6_DT21/U2600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_380B")

    NewScene("ED6_DT21/U2610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3817")

    NewScene("ED6_DT21/M5400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3823")

    NewScene("ED6_DT21/M5401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_382F")

    NewScene("ED6_DT21/M5402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_383B")

    NewScene("ED6_DT21/M5403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3847")

    NewScene("ED6_DT21/M5404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3853")

    NewScene("ED6_DT21/M5405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_385F")

    NewScene("ED6_DT21/M5406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_386B")

    NewScene("ED6_DT21/M5407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3877")

    NewScene("ED6_DT21/M5408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3883")

    NewScene("ED6_DT21/M5409   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_388F")

    NewScene("ED6_DT21/M5410   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_389B")

    NewScene("ED6_DT21/M5412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38A7")

    NewScene("ED6_DT21/M5413   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38B3")

    NewScene("ED6_DT21/M5600   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38BF")

    NewScene("ED6_DT21/M5610   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38CB")

    NewScene("ED6_DT21/M5611   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38D7")

    NewScene("ED6_DT21/M5612   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38E3")

    NewScene("ED6_DT21/M5613   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38EF")

    NewScene("ED6_DT21/M5614   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_38FB")

    NewScene("ED6_DT21/M5615   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3907")

    NewScene("ED6_DT21/M3100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3913")

    NewScene("ED6_DT21/M3101   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_391F")

    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_392B")

    NewScene("ED6_DT21/M3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3937")

    NewScene("ED6_DT21/M3110   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3943")

    NewScene("ED6_DT21/M3112   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_394F")

    NewScene("ED6_DT21/M3116   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_395B")

    NewScene("ED6_DT21/M3200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3967")

    NewScene("ED6_DT21/M3201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3973")

    NewScene("ED6_DT21/M3202   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_397F")

    NewScene("ED6_DT21/M3203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_398B")

    NewScene("ED6_DT21/M3204   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_3997")

    NewScene("ED6_DT21/M3205   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_39A3")

    NewScene("ED6_DT21/M3206   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_39AF")

    NewScene("ED6_DT21/M5414   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_39BB")

    NewScene("ED6_DT21/M5415   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_39C7")

    NewScene("ED6_DT21/H3300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_39E0")

    label("loc_39D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39E0")

    label("loc_39E0")

    Jump("loc_3049")

    label("loc_39E3")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_303F end

    def Function_21_39F3(): pass

    label("Function_21_39F3")


    AnonymousTalk(    #20
        "\x06Where?\x02",
    )


    label("loc_39FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C98")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7300 煉獄（第７星層）①\x01",                  # 0
            "M7301 煉獄（第７星層）②\x01",                  # 1
            "M7302 煉獄（第７星層）③\x01",                  # 2
            "M7303 煉獄（第７星層）④\x01",                  # 3
            "M7304 煉獄（第７星層）⑤\x01",                  # 4
            "M7305 煉獄（第７星層）⑥\x01",                  # 5
            "M7306 煉獄（第７星層）⑦\x01",                  # 6
            "M7307 煉獄（第７星層）⑧\x01",                  # 7
            "M7308 煉獄（第７星層）⑨\x01",                  # 8
            "M7309 煉獄（第７星層）⑩\x01",                  # 9
            "M7310 煉獄（第７星層）無限①スタート\x01",      # 10
            "M7311 煉獄（第７星層）無限②螺旋\x01",          # 11
            "M7312 煉獄（第７星層）無限③中継\x01",          # 12
            "M7313 煉獄（第７星層）無限④ボス\x01",          # 13
            "Cancel\x01",                                    # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BE0"),
        (1, "loc_3BEC"),
        (2, "loc_3BF8"),
        (3, "loc_3C04"),
        (4, "loc_3C10"),
        (5, "loc_3C1C"),
        (6, "loc_3C28"),
        (7, "loc_3C34"),
        (8, "loc_3C40"),
        (9, "loc_3C4C"),
        (10, "loc_3C58"),
        (11, "loc_3C64"),
        (12, "loc_3C70"),
        (13, "loc_3C7C"),
        (SWITCH_DEFAULT, "loc_3C88"),
    )


    label("loc_3BE0")

    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3BEC")

    NewScene("ED6_DT21/M7301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3BF8")

    NewScene("ED6_DT21/M7302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C04")

    NewScene("ED6_DT21/M7303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C10")

    NewScene("ED6_DT21/M7304   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C1C")

    NewScene("ED6_DT21/M7305   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C28")

    NewScene("ED6_DT21/M7306   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C34")

    NewScene("ED6_DT21/M7307   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C40")

    NewScene("ED6_DT21/M7308   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C4C")

    NewScene("ED6_DT21/M7309   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C58")

    NewScene("ED6_DT21/M7310   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C64")

    NewScene("ED6_DT21/M7311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C70")

    NewScene("ED6_DT21/M7312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C7C")

    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3C95")

    label("loc_3C88")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C95")

    label("loc_3C95")

    Jump("loc_39FD")

    label("loc_3C98")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_39F3 end

    def Function_22_3CA8(): pass

    label("Function_22_3CA8")


    AnonymousTalk(    #21
        "\x06Where?\x02",
    )


    label("loc_3CB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4161")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "M7400 中枢広場/アルセイユ停泊地\x01",                   # 0
            "M7401 中枢Ａボス直前部屋\x01",                          # 1
            "M7402 中枢Ａボス部屋\x01",                              # 2
            "M7403 中枢Ｂボス直前部屋\x01",                          # 3
            "M7404 中枢Ｂボス部屋\x01",                              # 4
            "M7405 中枢Ｃボス直前部屋\x01",                          # 5
            "M7406 中枢Ｃボス部屋\x01",                              # 6
            "M7407 中枢ラスボス直前部屋\x01",                        # 7
            "M7408 中枢ラスボス部屋\x01",                            # 8
            "M7409 中枢Ａ通路①\x01",                                # 9
            "M7410 中枢Ａ通路②\x01",                                # 10
            "M7411 中枢Ａ通路③\x01",                                # 11
            "M7412 中枢Ａ通路④\x01",                                # 12
            "M7413 中枢Ｂ通路①\x01",                                # 13
            "M7414 中枢Ｂ通路②\x01",                                # 14
            "M7415 中枢Ｂ通路③\x01",                                # 15
            "M7416 中枢Ｂ通路④\x01",                                # 16
            "M7417 中枢Ｂ通路⑤\x01",                                # 17
            "M7418 中枢Ｃ通路①\x01",                                # 18
            "M7419 中枢Ｃ通路②\x01",                                # 19
            "M7420 中枢Ｃ通路③\x01",                                # 20
            "M7421 中枢Ｃ通路④\x01",                                # 21
            "M7422 中枢ラスト通路①\x01",                            # 22
            "M7423 中枢ラスト通路②\x01",                            # 23
            "M7424 中枢ラスト通路③\x01",                            # 24
            "M7425 中枢ラスト通路④\x01",                            # 25
            "M7426 中枢ラスト通路⑤\x01",                            # 26
            "M7427 中枢ラスト通路⑥\x01",                            # 27
            "P0800 ｽｶｲﾎﾞｯｸｽ荒野(ｱﾙｾｲﾕ突入用)\x01",      # 28
            "M7499 ラスボスイベント用\x01",                          # 29
            "Cancel\x01",                                            # 30
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FE9"),
        (1, "loc_3FF5"),
        (2, "loc_4001"),
        (3, "loc_400D"),
        (4, "loc_4019"),
        (5, "loc_4025"),
        (6, "loc_4031"),
        (7, "loc_403D"),
        (8, "loc_4049"),
        (9, "loc_4055"),
        (10, "loc_4061"),
        (11, "loc_406D"),
        (12, "loc_4079"),
        (13, "loc_4085"),
        (14, "loc_4091"),
        (15, "loc_409D"),
        (16, "loc_40A9"),
        (17, "loc_40B5"),
        (18, "loc_40C1"),
        (19, "loc_40CD"),
        (20, "loc_40D9"),
        (21, "loc_40E5"),
        (22, "loc_40F1"),
        (23, "loc_40FD"),
        (24, "loc_4109"),
        (25, "loc_4115"),
        (26, "loc_4121"),
        (27, "loc_412D"),
        (28, "loc_4139"),
        (29, "loc_4145"),
        (SWITCH_DEFAULT, "loc_4151"),
    )


    label("loc_3FE9")

    NewScene("ED6_DT21/M7400   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_3FF5")

    NewScene("ED6_DT21/M7401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4001")

    NewScene("ED6_DT21/M7402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_400D")

    NewScene("ED6_DT21/M7403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4019")

    NewScene("ED6_DT21/M7404   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4025")

    NewScene("ED6_DT21/M7405   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4031")

    NewScene("ED6_DT21/M7406   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_403D")

    NewScene("ED6_DT21/M7407   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4049")

    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4055")

    NewScene("ED6_DT21/M7409   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4061")

    NewScene("ED6_DT21/M7410   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_406D")

    NewScene("ED6_DT21/M7411   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4079")

    NewScene("ED6_DT21/M7412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4085")

    NewScene("ED6_DT21/M7413   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4091")

    NewScene("ED6_DT21/M7414   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_409D")

    NewScene("ED6_DT21/M7415   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40A9")

    NewScene("ED6_DT21/M7416   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40B5")

    NewScene("ED6_DT21/M7417   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40C1")

    NewScene("ED6_DT21/M7418   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40CD")

    NewScene("ED6_DT21/M7419   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40D9")

    NewScene("ED6_DT21/M7420   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40E5")

    NewScene("ED6_DT21/M7421   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40F1")

    NewScene("ED6_DT21/M7422   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_40FD")

    NewScene("ED6_DT21/M7423   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4109")

    NewScene("ED6_DT21/M7424   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4115")

    NewScene("ED6_DT21/M7425   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4121")

    NewScene("ED6_DT21/M7426   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_412D")

    NewScene("ED6_DT21/M7427   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4139")

    NewScene("ED6_DT21/P0800   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4145")

    NewScene("ED6_DT21/M7499   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_415E")

    label("loc_4151")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_415E")

    label("loc_415E")

    Jump("loc_3CB2")

    label("loc_4161")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_3CA8 end

    def Function_23_4171(): pass

    label("Function_23_4171")


    AnonymousTalk(    #22
        "\x06Where?\x02",
    )


    label("loc_417B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4200")

    Menu(
        3,
        -1,
        32,
        1,
        (
            "E0810 スカイマップ（昼）\x01",      # 0
            "E1210 メルカバ内部\x01",            # 1
            "Cancel\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41D8"),
        (1, "loc_41E4"),
        (SWITCH_DEFAULT, "loc_41F0"),
    )


    label("loc_41D8")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_41FD")

    label("loc_41E4")

    NewScene("ED6_DT21/E1210   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_41FD")

    label("loc_41F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41FD")

    label("loc_41FD")

    Jump("loc_417B")

    label("loc_4200")

    OP_5F(0x3)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_4171 end

    def Function_24_4210(): pass

    label("Function_24_4210")

    Return()

    # Function_24_4210 end

    def Function_25_4211(): pass

    label("Function_25_4211")

    EventBegin(0x0)
    OP_DA()
    OP_56(0x0)
    OP_5F(0x0)
    OP_5F(0x1)

    AnonymousTalk(    #23
        "\x06どれ？\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_449F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        10,
        100,
        1,
        (
            "Opening\x01",                                                 # 0
            "Glorious Arrives\x01",                                        # 1
            "Aureole Appears\x01",                                         # 2
            "Glorgious Attacks, Aureole Airspace, Arseille Dive\x01",      # 3
            "Aureole Collapse\x01",                                        # 4
            "Cancel\x01",                                                  # 5
        )
    )

    MenuEnd(0x0)
    OP_5F(0x2)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_42EE")
    Jump("loc_449F")

    label("loc_42EE")

    FadeToDark(2000, 0, -1)
    OP_20(0x3E8)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_432C"),
        (1, "loc_4342"),
        (2, "loc_435F"),
        (3, "loc_43B4"),
        (4, "loc_444B"),
        (SWITCH_DEFAULT, "loc_4468"),
    )


    label("loc_432C")

    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Jump("loc_4468")

    label("loc_4342")

    OP_1D(0x1C)
    Sleep(5000)
    PlayMovie(0x0, "ED6_DT40.dat", 0x0, 0x0)
    Jump("loc_4468")

    label("loc_435F")

    OP_1D(0x23)
    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_439E")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_439E")

    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x0)
    Jump("loc_4468")

    label("loc_43B4")

    OP_1D(0x77)
    Sleep(2000)
    PlayMovie(0x0, "ED6_DT43.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F8")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_43F8")

    PlayMovie(0x0, "ED6_DT44.dat", 0x0, 0x0)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4435")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_4435")

    PlayMovie(0x0, "ED6_DT45.dat", 0x0, 0x0)
    Jump("loc_4468")

    label("loc_444B")

    OP_1D(0x50)
    Sleep(5000)
    PlayMovie(0x0, "ED6_DT46.dat", 0x0, 0x0)
    Jump("loc_4468")

    label("loc_4468")

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
    Jump("loc_4230")

    label("loc_449F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_4211 end

    SaveToFile()

Try(main)
