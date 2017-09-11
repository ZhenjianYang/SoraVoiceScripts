from ED6ScenarioHelper import *

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
            'ED6_DT01/T0001   ._SN',
            'ED6_DT01/T0001_1 ._SN',
            'ED6_DT01/T0001_2 ._SN',
            'ED6_DT01/T0001_3 ._SN',
            'ED6_DT01/T0001_4 ._SN',
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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_2CD",          # 01, 1
        "Function_2_723",          # 02, 2
        "Function_3_805",          # 03, 3
        "Function_4_C4B",          # 04, 4
        "Function_5_1139",         # 05, 5
        "Function_6_1843",         # 06, 6
        "Function_7_1DCB",         # 07, 7
        "Function_8_2379",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06Which?\x02",
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD")

    Menu(
        1,
        10,
        100,
        1,
        (
            "30 General Purpose NPL\x01",                                             # 0
            "31 Party and Dedicated NPL\x01",                                         # 1
            "32 General Purpose and dedicated NPL2/APL\x01",                          # 2
            "33 PT battle Estelle, Joshua, Zin, Agate, Olivier\x01",                  # 3
            "34 PT battle Joshua, Scherazard, Tita, Kloe\x01",                        # 4
            "35 NPC Battle Bracer Female, Thug, Sky Bandit\x01",                      # 5
            "36 NPC Battle Thin Bandit, Bracer Female 2\x01",                         # 6
            "37 NPC Battle Royal Guard, Officer, Agent, Lola, Risha, Kanoe\x01",      # 7
            "39座りキャラ\x01",                                                       # 8
            "Cancel\x01",                                                             # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25F"),
        (1, "loc_268"),
        (2, "loc_271"),
        (3, "loc_27A"),
        (4, "loc_283"),
        (5, "loc_28C"),
        (6, "loc_295"),
        (7, "loc_29E"),
        (8, "loc_2A7"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25F")

    NewScene("ED6_DT01/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_268")

    NewScene("ED6_DT01/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_271")

    NewScene("ED6_DT01/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_27A")

    NewScene("ED6_DT01/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_283")

    NewScene("ED6_DT01/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_28C")

    NewScene("ED6_DT01/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_295")

    NewScene("ED6_DT01/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_29E")

    NewScene("ED6_DT01/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2A7")

    NewScene("ED6_DT01/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4")

    label("loc_2BD")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_2CD(): pass

    label("Function_1_2CD")


    AnonymousTalk(    #1
        "\x06Which?\x02",
    )


    label("loc_2D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_713")

    Menu(
        1,
        10,
        32,
        1,
        (
            "40 Monster List (10000-10290)\x01",         # 0
            "41 Monster List (10300-10590)\x01",         # 1
            "42 Monster List (10600-10890)\x01",         # 2
            "57 Monster List (10900-11040)\x01",         # 3
            "60 Monster List (11050-11190)\x01",         # 4
            "43 Monster Motions (10000-10050)\x01",      # 5
            "44 Monster Motions (10060-10140)\x01",      # 6
            "45 Monster Motions (10150-10210)\x01",      # 7
            "46 Monster Motions (10220-10290)\x01",      # 8
            "47 Monster Motions (10300-10380)\x01",      # 9
            "48 Monster Motions (10390-10450)\x01",      # 10
            "49 Monster Motions (10460-10530)\x01",      # 11
            "50 Monster Motions (10540-10610)\x01",      # 12
            "51 Monster Motions (10620-10690)\x01",      # 13
            "52 Monster Motions (10700-10770)\x01",      # 14
            "53 Monster Motions (10780-10850)\x01",      # 15
            "54 Monster Motions (10860-10900)\x01",      # 16
            "55 Monster Motions (10910-10940)\x01",      # 17
            "56 Monster Motions (10950-10990)\x01",      # 18
            "58 Monster Motions (11000-11060)\x01",      # 19
            "59 Monster Motions (11070-11110)\x01",      # 20
            "61 Monster Motions (11120-11150)\x01",      # 21
            "62 Monster Motions (11160-11190)\x01",      # 22
            "Cancel\x01",                                # 23
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_640"),
        (1, "loc_649"),
        (2, "loc_652"),
        (3, "loc_65B"),
        (4, "loc_664"),
        (5, "loc_66D"),
        (6, "loc_676"),
        (7, "loc_67F"),
        (8, "loc_688"),
        (9, "loc_691"),
        (10, "loc_69A"),
        (11, "loc_6A3"),
        (12, "loc_6AC"),
        (13, "loc_6B5"),
        (14, "loc_6BE"),
        (15, "loc_6C7"),
        (16, "loc_6D0"),
        (17, "loc_6D9"),
        (18, "loc_6E2"),
        (19, "loc_6EB"),
        (20, "loc_6F4"),
        (21, "loc_6FD"),
        (SWITCH_DEFAULT, "loc_706"),
    )


    label("loc_640")

    NewScene("ED6_DT01/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_649")

    NewScene("ED6_DT01/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_652")

    NewScene("ED6_DT01/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_65B")

    NewScene("ED6_DT01/T0057   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_664")

    NewScene("ED6_DT01/T0060   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_66D")

    NewScene("ED6_DT01/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_676")

    NewScene("ED6_DT01/T0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_67F")

    NewScene("ED6_DT01/T0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_688")

    NewScene("ED6_DT01/T0046   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_691")

    NewScene("ED6_DT01/T0047   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_69A")

    NewScene("ED6_DT01/T0048   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6A3")

    NewScene("ED6_DT01/T0049   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6AC")

    NewScene("ED6_DT01/T0050   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6B5")

    NewScene("ED6_DT01/T0051   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6BE")

    NewScene("ED6_DT01/T0052   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6C7")

    NewScene("ED6_DT01/T0053   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6D0")

    NewScene("ED6_DT01/T0054   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6D9")

    NewScene("ED6_DT01/T0055   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6E2")

    NewScene("ED6_DT01/T0056   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6EB")

    NewScene("ED6_DT01/T0058   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6F4")

    NewScene("ED6_DT01/T0059   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_6FD")

    NewScene("ED6_DT01/T0061   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_706")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D7")

    label("loc_713")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_2CD end

    def Function_2_723(): pass

    label("Function_2_723")


    AnonymousTalk(    #2
        "\x06[Maps] Select\x02",
    )


    label("loc_734")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F5")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Rolent Region\x01",       # 0
            "Bose Region\x01",         # 1
            "Ruan Region\x01",         # 2
            "Zeiss Region\x01",        # 3
            "Grancel Region\x01",      # 4
            "Others\x01",              # 5
            "Cancel\x01",              # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BE"),
        (1, "loc_7C5"),
        (2, "loc_7CC"),
        (3, "loc_7D3"),
        (4, "loc_7DA"),
        (5, "loc_7E1"),
        (SWITCH_DEFAULT, "loc_7E8"),
    )


    label("loc_7BE")

    Call(3, 3)
    Jump("loc_7F2")

    label("loc_7C5")

    Call(3, 4)
    Jump("loc_7F2")

    label("loc_7CC")

    Call(3, 5)
    Jump("loc_7F2")

    label("loc_7D3")

    Call(3, 6)
    Jump("loc_7F2")

    label("loc_7DA")

    Call(3, 7)
    Jump("loc_7F2")

    label("loc_7E1")

    Call(3, 8)
    Jump("loc_7F2")

    label("loc_7E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F2")

    Jump("loc_734")

    label("loc_7F5")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_723 end

    def Function_3_805(): pass

    label("Function_3_805")


    AnonymousTalk(    #3
        "\x06Where?\x02",
    )


    label("loc_80F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3B")

    Menu(
        2,
        10,
        100,
        1,
        (
            "City\x01",          # 0
            "Dungeon\x01",       # 1
            "Highways\x01",      # 2
            "Night\x01",         # 3
            "Cancel\x01",        # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_864"),
        (1, "loc_9B5"),
        (2, "loc_B2D"),
        (3, "loc_BC8"),
        (SWITCH_DEFAULT, "loc_C2E"),
    )


    label("loc_864")


    AnonymousTalk(    #4
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T0100 Rolent\x01",                   # 0
            "T0200 Mayor's Manor\x01",            # 1
            "T0300 Bright House\x01",             # 2
            "T0400 Perzel Farm\x01",              # 3
            "T0401 Perzel Farm (Night)\x01",      # 4
            "T0500 Verte Guardpost\x01",          # 5
            "T0700 Landingport\x01",              # 6
            "T0300 Bright House\x01",             # 7
            "T0600 Gurune Gate\x01",              # 8
            "Cancel\x01",                         # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_95B"),
        (1, "loc_964"),
        (2, "loc_96D"),
        (3, "loc_976"),
        (4, "loc_97F"),
        (5, "loc_988"),
        (6, "loc_991"),
        (7, "loc_99A"),
        (8, "loc_9A3"),
        (SWITCH_DEFAULT, "loc_9AC"),
    )


    label("loc_95B")

    NewScene("ED6_DT01/T0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_964")

    NewScene("ED6_DT01/T0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_96D")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_976")

    NewScene("ED6_DT01/T0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_97F")

    NewScene("ED6_DT01/T0401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_988")

    NewScene("ED6_DT01/T0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_991")

    NewScene("ED6_DT01/T0700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_99A")

    NewScene("ED6_DT01/T0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9A3")

    NewScene("ED6_DT01/T0600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9AC")

    OP_5F(0x3)
    Jump("loc_9B2")

    label("loc_9B2")

    Jump("loc_C38")

    label("loc_9B5")


    AnonymousTalk(    #5
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "C0100 Malga Mine\x01",                 # 0
            "C0101 Malga Mine Interior\x01",        # 1
            "C0300 Mistwald Forest\x01",            # 2
            "C0304 Mistwald Forest Loop\x01",       # 3
            "C0500 Underground Waterways\x01",      # 4
            "C0411 Esmelas Tower 1F\x01",           # 5
            "C0412 Esmelas Tower 2F\x01",           # 6
            "C0413 Esmelas Tower 3F\x01",           # 7
            "C0414 Esmelas Tower 4F\x01",           # 8
            "Cancel\x01",                           # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AD3"),
        (1, "loc_ADC"),
        (2, "loc_AE5"),
        (3, "loc_AEE"),
        (4, "loc_AF7"),
        (5, "loc_B00"),
        (6, "loc_B09"),
        (7, "loc_B12"),
        (8, "loc_B1B"),
        (SWITCH_DEFAULT, "loc_B24"),
    )


    label("loc_AD3")

    NewScene("ED6_DT01/C0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_ADC")

    NewScene("ED6_DT01/C0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_AE5")

    NewScene("ED6_DT01/C0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_AEE")

    NewScene("ED6_DT01/C0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_AF7")

    NewScene("ED6_DT01/C0411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B00")

    NewScene("ED6_DT01/C0412   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B09")

    NewScene("ED6_DT01/C0413   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B12")

    NewScene("ED6_DT01/C0414   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B1B")

    NewScene("ED6_DT01/C0415   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_B24")

    OP_5F(0x3)
    Jump("loc_B2A")

    label("loc_B2A")

    Jump("loc_C38")

    label("loc_B2D")


    AnonymousTalk(    #6
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "R0100 Elize Highway\x01",        # 0
            "R0200 Milch Main Road\x01",      # 1
            "R0300 Malga Trail\x01",          # 2
            "Cancel\x01",                     # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B9B"),
        (1, "loc_BA7"),
        (2, "loc_BB3"),
        (SWITCH_DEFAULT, "loc_BBF"),
    )


    label("loc_B9B")

    NewScene("ED6_DT01/R0100   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_BC5")

    label("loc_BA7")

    NewScene("ED6_DT01/R0200   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_BC5")

    label("loc_BB3")

    NewScene("ED6_DT01/R0300   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_BC5")

    label("loc_BBF")

    OP_5F(0x3)
    Jump("loc_BC5")

    label("loc_BC5")

    Jump("loc_C38")

    label("loc_BC8")


    AnonymousTalk(    #7
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T0311 Bright House Outside Perspective\x01",      # 0
            "Cancel\x01",                                      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C19"),
        (SWITCH_DEFAULT, "loc_C25"),
    )


    label("loc_C19")

    NewScene("ED6_DT01/T0311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_C2B")

    label("loc_C25")

    OP_5F(0x3)
    Jump("loc_C2B")

    label("loc_C2B")

    Jump("loc_C38")

    label("loc_C2E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C38")

    Jump("loc_80F")

    label("loc_C3B")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_805 end

    def Function_4_C4B(): pass

    label("Function_4_C4B")


    AnonymousTalk(    #8
        "\x06Where?\x02",
    )


    label("loc_C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1129")

    Menu(
        2,
        10,
        100,
        1,
        (
            "City\x01",          # 0
            "Dungeon\x01",       # 1
            "Highways\x01",      # 2
            "Night\x01",         # 3
            "Cancel\x01",        # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CAA"),
        (1, "loc_E0F"),
        (2, "loc_F80"),
        (3, "loc_10A3"),
        (SWITCH_DEFAULT, "loc_1119"),
    )


    label("loc_CAA")


    AnonymousTalk(    #9
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T1100 Bose City, South Entrance\x01",      # 0
            "T1110 Bose City, Citizen Houses\x01",      # 1
            "T1300 Krone Guardpost\x01",                # 2
            "T1301 Krone Guardpost (Night)\x01",        # 3
            "T1102 Bose International Port\x01",        # 4
            "T1200 Ravennue Village\x01",               # 5
            "T1400 Haken Gate\x01",                     # 6
            "T1500 Lakeshore Inn\x01",                  # 7
            "Cancel\x01",                               # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DBE"),
        (1, "loc_DC7"),
        (2, "loc_DD0"),
        (3, "loc_DD9"),
        (4, "loc_DE2"),
        (5, "loc_DEB"),
        (6, "loc_DF4"),
        (7, "loc_DFD"),
        (SWITCH_DEFAULT, "loc_E06"),
    )


    label("loc_DBE")

    NewScene("ED6_DT01/T1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DC7")

    NewScene("ED6_DT01/T1110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DD0")

    NewScene("ED6_DT01/T1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DD9")

    NewScene("ED6_DT01/T1301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DE2")

    NewScene("ED6_DT01/T1102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DEB")

    NewScene("ED6_DT01/T1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DF4")

    NewScene("ED6_DT01/T1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_DFD")

    NewScene("ED6_DT01/T1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_E06")

    OP_5F(0x3)
    Jump("loc_E0C")

    label("loc_E0C")

    Jump("loc_1126")

    label("loc_E0F")


    AnonymousTalk(    #10
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1200 Amberl Tower (SC)\x01",            # 0
            "C1400 Nebel Valley\x01",                 # 1
            "C1100 Ravennue Abandoned Mine\x01",      # 2
            "C1300 Sky Bandit Fort\x01",              # 3
            "C1211 Amberl Tower 1F\x01",              # 4
            "C1212 Amberl Tower 2F\x01",              # 5
            "C1213 Amberl Tower 3F\x01",              # 6
            "C1214 Amberl Tower 4F\x01",              # 7
            "C1215 Amberl Tower 5F\x01",              # 8
            "Cancel\x01",                             # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F26"),
        (1, "loc_F2F"),
        (2, "loc_F38"),
        (3, "loc_F41"),
        (4, "loc_F4A"),
        (5, "loc_F53"),
        (6, "loc_F5C"),
        (7, "loc_F65"),
        (8, "loc_F6E"),
        (SWITCH_DEFAULT, "loc_F77"),
    )


    label("loc_F26")

    NewScene("ED6_DT01/C1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F2F")

    NewScene("ED6_DT01/C1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F38")

    NewScene("ED6_DT01/C1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F41")

    NewScene("ED6_DT01/C1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F4A")

    NewScene("ED6_DT01/C1211   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F53")

    NewScene("ED6_DT01/C1212   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F5C")

    NewScene("ED6_DT01/C1213   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F65")

    NewScene("ED6_DT01/C1214   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F6E")

    NewScene("ED6_DT01/C1215   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_F77")

    OP_5F(0x3)
    Jump("loc_F7D")

    label("loc_F7D")

    Jump("loc_1126")

    label("loc_F80")


    AnonymousTalk(    #11
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500 Krone Pass\x01",                  # 0
            "R1300 Eisen Road\x01",                  # 1
            "R1100 East Bose Highway\x01",           # 2
            "R1200 West Bose Highway\x01",           # 3
            "R1400 New Ansel Path\x01",              # 4
            "R1403 New Ansel Path (Night)\x01",      # 5
            "R1500 Ravennue Trail\x01",              # 6
            "Cancel\x01",                            # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_105B"),
        (1, "loc_1064"),
        (2, "loc_106D"),
        (3, "loc_1076"),
        (4, "loc_107F"),
        (5, "loc_1088"),
        (6, "loc_1091"),
        (SWITCH_DEFAULT, "loc_109A"),
    )


    label("loc_105B")

    NewScene("ED6_DT01/C1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1064")

    NewScene("ED6_DT01/R1300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_106D")

    NewScene("ED6_DT01/R1100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1076")

    NewScene("ED6_DT01/R1200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_107F")

    NewScene("ED6_DT01/R1400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1088")

    NewScene("ED6_DT01/R1403   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1091")

    NewScene("ED6_DT01/R1500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_109A")

    OP_5F(0x3)
    Jump("loc_10A0")

    label("loc_10A0")

    Jump("loc_1126")

    label("loc_10A3")


    AnonymousTalk(    #12
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T1401 Haken Gate\x01",           # 0
            "T1311 Krone Guardpost\x01",      # 1
            "Cancel\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10F8"),
        (1, "loc_1104"),
        (SWITCH_DEFAULT, "loc_1110"),
    )


    label("loc_10F8")

    NewScene("ED6_DT01/T1401   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1116")

    label("loc_1104")

    NewScene("ED6_DT01/T1311   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1116")

    label("loc_1110")

    OP_5F(0x3)
    Jump("loc_1116")

    label("loc_1116")

    Jump("loc_1126")

    label("loc_1119")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1126")

    label("loc_1126")

    Jump("loc_C55")

    label("loc_1129")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_C4B end

    def Function_5_1139(): pass

    label("Function_5_1139")


    AnonymousTalk(    #13
        "\x06Where?\x02",
    )


    label("loc_1143")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1833")

    Menu(
        2,
        10,
        100,
        1,
        (
            "City\x01",          # 0
            "Dungeon\x01",       # 1
            "Highways\x01",      # 2
            "Night\x01",         # 3
            "Other\x01",         # 4
            "Cancel\x01",        # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_11A2"),
        (1, "loc_149E"),
        (2, "loc_1626"),
        (3, "loc_1702"),
        (4, "loc_17B9"),
        (SWITCH_DEFAULT, "loc_1823"),
    )


    label("loc_11A2")


    AnonymousTalk(    #14
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T2100 Ruan City\x01",                                                     # 0
            "T2102 Landing Port\x01",                                                  # 1
            "T2200 Mayor's Manor\x01",                                                 # 2
            "T2600 Royal Academy Old Schoolhouse\x01",                                 # 3
            "T2510 Royal Academy Main Building\x01",                                   # 4
            "T2520 Royal Academy Main Building School Festival\x01",                   # 5
            "T2530 Royal Academy Main Building School Festival Preparations\x01",      # 6
            "T2400 Mercia Orphanage\x01",                                              # 7
            "T2401 Mercia Orphanage (After Fire)\x01",                                 # 8
            "T2402 Mercia Orphanage (After Rebuilding)\x01",                           # 9
            "T2110 Citizen Homes\x01",                                                 # 10
            "T2120 Shops\x01",                                                         # 11
            "T2130 Church\x01",                                                        # 12
            "T2131 Bar, Casino\x01",                                                   # 13
            "T2700 Air-Letten Guard Post\x01",                                         # 14
            "T2300 Manoria Village\x01",                                               # 15
            "T2411 Mercia Orphanage Inside (During Fire)\x01",                         # 16
            "Cancel\x01",                                                              # 17
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13FC"),
        (1, "loc_1405"),
        (2, "loc_140E"),
        (3, "loc_1417"),
        (4, "loc_1420"),
        (5, "loc_1429"),
        (6, "loc_1432"),
        (7, "loc_143B"),
        (8, "loc_1444"),
        (9, "loc_144D"),
        (10, "loc_1456"),
        (11, "loc_145F"),
        (12, "loc_1468"),
        (13, "loc_1471"),
        (14, "loc_147A"),
        (15, "loc_1483"),
        (16, "loc_148C"),
        (SWITCH_DEFAULT, "loc_1495"),
    )


    label("loc_13FC")

    NewScene("ED6_DT01/T2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1405")

    NewScene("ED6_DT01/T2102   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_140E")

    NewScene("ED6_DT01/T2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1417")

    NewScene("ED6_DT01/T2600   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1420")

    NewScene("ED6_DT01/T2510   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1429")

    NewScene("ED6_DT01/T2520   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1432")

    NewScene("ED6_DT01/T2530   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_143B")

    NewScene("ED6_DT01/T2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1444")

    NewScene("ED6_DT01/T2401   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_144D")

    NewScene("ED6_DT01/T2402   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1456")

    NewScene("ED6_DT01/T2110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_145F")

    NewScene("ED6_DT01/T2120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1468")

    NewScene("ED6_DT01/T2130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1471")

    NewScene("ED6_DT01/T2131   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_147A")

    NewScene("ED6_DT01/T2700   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1483")

    NewScene("ED6_DT01/T2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_148C")

    NewScene("ED6_DT01/T2411   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1495")

    OP_5F(0x3)
    Jump("loc_149B")

    label("loc_149B")

    Jump("loc_1830")

    label("loc_149E")


    AnonymousTalk(    #15
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C2100 Sapphirl Tower (SC)\x01",                    # 0
            "C2209 Lighthouse\x01",                             # 1
            "C2200 Lighthouse (Night)\x01",                     # 2
            "C2400 Old Schoolhouse Underground Ruins\x01",      # 3
            "C2111 Sapphirl Tower 1F\x01",                      # 4
            "C2112 Sapphirl Tower 2F\x01",                      # 5
            "C2113 Sapphirl Tower 3F\x01",                      # 6
            "C2114 Sapphirl Tower 4F\x01",                      # 7
            "C2115 Sapphirl Tower 5F\x01",                      # 8
            "Cancel\x01",                                       # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15CC"),
        (1, "loc_15D5"),
        (2, "loc_15DE"),
        (3, "loc_15E7"),
        (4, "loc_15F0"),
        (5, "loc_15F9"),
        (6, "loc_1602"),
        (7, "loc_160B"),
        (8, "loc_1614"),
        (SWITCH_DEFAULT, "loc_161D"),
    )


    label("loc_15CC")

    NewScene("ED6_DT01/C2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_15D5")

    NewScene("ED6_DT01/C2209   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_15DE")

    NewScene("ED6_DT01/C2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_15E7")

    NewScene("ED6_DT01/C2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_15F0")

    NewScene("ED6_DT01/C2111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_15F9")

    NewScene("ED6_DT01/C2112   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1602")

    NewScene("ED6_DT01/C2113   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_160B")

    NewScene("ED6_DT01/C2114   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1614")

    NewScene("ED6_DT01/C2115   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_161D")

    OP_5F(0x3)
    Jump("loc_1623")

    label("loc_1623")

    Jump("loc_1830")

    label("loc_1626")


    AnonymousTalk(    #16
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1501 Krone Trail\x01",            # 0
            "R2100 Manoria Byroad\x01",         # 1
            "R2400 Aurian Causeway\x01",        # 2
            "R2200 Gull Seaside Way\x01",       # 3
            "R2300 Vista Forest Road\x01",      # 4
            "Cancel\x01",                       # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16CC"),
        (1, "loc_16D5"),
        (2, "loc_16DE"),
        (3, "loc_16E7"),
        (4, "loc_16F0"),
        (SWITCH_DEFAULT, "loc_16F9"),
    )


    label("loc_16CC")

    NewScene("ED6_DT01/C1501   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16D5")

    NewScene("ED6_DT01/R2100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16DE")

    NewScene("ED6_DT01/R2400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16E7")

    NewScene("ED6_DT01/R2200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16F0")

    NewScene("ED6_DT01/R2300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_16F9")

    OP_5F(0x3)
    Jump("loc_16FF")

    label("loc_16FF")

    Jump("loc_1830")

    label("loc_1702")


    AnonymousTalk(    #17
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T2301 Manoria\x01",              # 0
            "R2111 Manoria Coast\x01",        # 1
            "T2403 Orphanage\x01",            # 2
            "R2412 Aurian Causeway\x01",      # 3
            "Cancel\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1780"),
        (1, "loc_178C"),
        (2, "loc_1798"),
        (3, "loc_17A4"),
        (SWITCH_DEFAULT, "loc_17B0"),
    )


    label("loc_1780")

    NewScene("ED6_DT01/T2301   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_17B6")

    label("loc_178C")

    NewScene("ED6_DT01/R2111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_17B6")

    label("loc_1798")

    NewScene("ED6_DT01/T2403   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_17B6")

    label("loc_17A4")

    NewScene("ED6_DT01/R2412   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_17B6")

    label("loc_17B0")

    OP_5F(0x3)
    Jump("loc_17B6")

    label("loc_17B6")

    Jump("loc_1830")

    label("loc_17B9")


    AnonymousTalk(    #18
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T2103 Sea Scroll\x01",      # 0
            "T2104 Sea\x01",             # 1
            "Cancel\x01",                # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1802"),
        (1, "loc_180E"),
        (SWITCH_DEFAULT, "loc_181A"),
    )


    label("loc_1802")

    NewScene("ED6_DT01/T2103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1820")

    label("loc_180E")

    NewScene("ED6_DT01/T2104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1820")

    label("loc_181A")

    OP_5F(0x3)
    Jump("loc_1820")

    label("loc_1820")

    Jump("loc_1830")

    label("loc_1823")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1830")

    label("loc_1830")

    Jump("loc_1143")

    label("loc_1833")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_1139 end

    def Function_6_1843(): pass

    label("Function_6_1843")


    AnonymousTalk(    #19
        "\x06Where?\x02",
    )


    label("loc_184D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBB")

    Menu(
        2,
        10,
        100,
        1,
        (
            "City\x01",          # 0
            "Dungeon\x01",       # 1
            "Highways\x01",      # 2
            "Night\x01",         # 3
            "Cancel\x01",        # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18A2"),
        (1, "loc_1A94"),
        (2, "loc_1C7F"),
        (3, "loc_1D3A"),
        (SWITCH_DEFAULT, "loc_1DAB"),
    )


    label("loc_18A2")


    AnonymousTalk(    #20
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T3100 Zeiss City\x01",                           # 0
            "T3110 Zeiss Citizen Houses Rooms 1~3\x01",       # 1
            "T3111 Central Factory Rooms\x01",                # 2
            "T3300 Wolf Fort\x01",                            # 3
            "T3130 Zeiss Church\x01",                         # 4
            "T3120 Weapon Shop\x01",                          # 5
            "T3133 Russell Factory\x01",                      # 6
            "T3200 Elmo Village Outside\x01",                 # 7
            "T3201 Elmo Village Outside\x01",                 # 8
            "T3400 Sanktheim Gate\x01",                       # 9
            "T3103 Zeiss City (Night)\x01",                   # 10
            "T3106 Zeiss City (Power Outage Event)\x01",      # 11
            "Cancel\x01",                                     # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A1F"),
        (1, "loc_1A28"),
        (2, "loc_1A31"),
        (3, "loc_1A3A"),
        (4, "loc_1A43"),
        (5, "loc_1A4C"),
        (6, "loc_1A55"),
        (7, "loc_1A5E"),
        (8, "loc_1A67"),
        (9, "loc_1A70"),
        (10, "loc_1A79"),
        (11, "loc_1A82"),
        (SWITCH_DEFAULT, "loc_1A8B"),
    )


    label("loc_1A1F")

    NewScene("ED6_DT01/T3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A28")

    NewScene("ED6_DT01/T3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A31")

    NewScene("ED6_DT01/T3111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A3A")

    NewScene("ED6_DT01/T3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A43")

    NewScene("ED6_DT01/T3130   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A4C")

    NewScene("ED6_DT01/T3120   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A55")

    NewScene("ED6_DT01/T3133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A5E")

    NewScene("ED6_DT01/T3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A67")

    NewScene("ED6_DT01/T3201   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A70")

    NewScene("ED6_DT01/T3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A79")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A82")

    NewScene("ED6_DT01/T3106   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1A8B")

    OP_5F(0x3)
    Jump("loc_1A91")

    label("loc_1A91")

    Jump("loc_1DB8")

    label("loc_1A94")


    AnonymousTalk(    #21
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "Carnelia Tower (SC)\x01",                         # 0
            "C3100 Leiston Fortress Outside\x01",              # 1
            "C3110 Leiston Fortress Inside\x01",               # 2
            "C3104 Leiston Fortress Outside (Night)\x01",      # 3
            "C3300 Kaldia Limestone Cave\x01",                 # 4
            "C3303 Kaldia Limestone Cave Boss\x01",            # 5
            "C3511 Carnelia Tower 1F\x01",                     # 6
            "C3512 Carnelia Tower 2F\x01",                     # 7
            "C3513 Carnelia Tower 3F\x01",                     # 8
            "C3514 Carnelia Tower 4F\x01",                     # 9
            "C3515 Carnelia Tower 5F\x01",                     # 10
            "Cancel\x01",                                      # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C13"),
        (1, "loc_1C1C"),
        (2, "loc_1C25"),
        (3, "loc_1C2E"),
        (4, "loc_1C37"),
        (5, "loc_1C40"),
        (6, "loc_1C49"),
        (7, "loc_1C52"),
        (8, "loc_1C5B"),
        (9, "loc_1C64"),
        (10, "loc_1C6D"),
        (SWITCH_DEFAULT, "loc_1C76"),
    )


    label("loc_1C13")

    NewScene("ED6_DT01/C3500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C1C")

    NewScene("ED6_DT01/C3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C25")

    NewScene("ED6_DT01/C3110   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C2E")

    NewScene("ED6_DT01/C3104   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C37")

    NewScene("ED6_DT01/C3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C40")

    NewScene("ED6_DT01/C3303   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C49")

    NewScene("ED6_DT01/C3511   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C52")

    NewScene("ED6_DT01/C3512   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C5B")

    NewScene("ED6_DT01/C3513   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C64")

    NewScene("ED6_DT01/C3514   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C6D")

    NewScene("ED6_DT01/C3515   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1C76")

    OP_5F(0x3)
    Jump("loc_1C7C")

    label("loc_1C7C")

    Jump("loc_1DB8")

    label("loc_1C7F")


    AnonymousTalk(    #22
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300 Soldat Army Road\x01",       # 0
            "R3400 Kaldia Tunnel\x01",          # 1
            "R3100 Tratt Plains Road\x01",      # 2
            "R3200 Ritter Roadway\x01",         # 3
            "Cancel\x01",                       # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D0D"),
        (1, "loc_1D16"),
        (2, "loc_1D1F"),
        (3, "loc_1D28"),
        (SWITCH_DEFAULT, "loc_1D31"),
    )


    label("loc_1D0D")

    NewScene("ED6_DT01/R3300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1D16")

    NewScene("ED6_DT01/R3400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1D1F")

    NewScene("ED6_DT01/R3100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1D28")

    NewScene("ED6_DT01/R3200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1D31")

    OP_5F(0x3)
    Jump("loc_1D37")

    label("loc_1D37")

    Jump("loc_1DB8")

    label("loc_1D3A")


    AnonymousTalk(    #23
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T3103 Zweis\x01",                # 0
            "T3104 Central Factory\x01",      # 1
            "Cancel\x01",                     # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D8A"),
        (1, "loc_1D96"),
        (SWITCH_DEFAULT, "loc_1DA2"),
    )


    label("loc_1D8A")

    NewScene("ED6_DT01/T3103   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DA8")

    label("loc_1D96")

    NewScene("ED6_DT01/T3104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1DA8")

    label("loc_1DA2")

    OP_5F(0x3)
    Jump("loc_1DA8")

    label("loc_1DA8")

    Jump("loc_1DB8")

    label("loc_1DAB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DB8")

    label("loc_1DB8")

    Jump("loc_184D")

    label("loc_1DBB")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_1843 end

    def Function_7_1DCB(): pass

    label("Function_7_1DCB")


    AnonymousTalk(    #24
        "\x06どこ？\x02",
    )


    label("loc_1DD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2369")

    Menu(
        2,
        10,
        100,
        1,
        (
            "City\x01",          # 0
            "Dungeon\x01",       # 1
            "Highways\x01",      # 2
            "Night\x01",         # 3
            "Cancel\x01",        # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E2A"),
        (1, "loc_1F59"),
        (2, "loc_208E"),
        (3, "loc_2102"),
        (SWITCH_DEFAULT, "loc_2359"),
    )


    label("loc_1E2A")


    AnonymousTalk(    #25
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4100 Grancel\x01",                       # 0
            "T4200 Grancel Castle\x01",                # 1
            "T4300 Erbe Royal Villa (Night)\x01",      # 2
            "T4133 Hotel Rooms (Night)\x01",           # 3
            "T4134 Cathedral Rooms (Night)\x01",       # 4
            "T4135 Museum Rooms\x01",                  # 5
            "T4136 Grand Arena Rooms\x01",             # 6
            "Cancel\x01",                              # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F11"),
        (1, "loc_1F1A"),
        (2, "loc_1F23"),
        (3, "loc_1F2C"),
        (4, "loc_1F35"),
        (5, "loc_1F3E"),
        (6, "loc_1F47"),
        (SWITCH_DEFAULT, "loc_1F50"),
    )


    label("loc_1F11")

    NewScene("ED6_DT01/T4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F1A")

    NewScene("ED6_DT01/T4200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F23")

    NewScene("ED6_DT01/T4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F2C")

    NewScene("ED6_DT01/T4133   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F35")

    NewScene("ED6_DT01/T4134   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F3E")

    NewScene("ED6_DT01/T4135   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F47")

    NewScene("ED6_DT01/T4136   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1F50")

    OP_5F(0x3)
    Jump("loc_1F56")

    label("loc_1F56")

    Jump("loc_2366")

    label("loc_1F59")


    AnonymousTalk(    #26
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200 Underground Waterways A\x01",        # 0
            "C4202 Underground Waterways B\x01",        # 1
            "C4204 Underground Waterways C\x01",        # 2
            "C4300 Sealed Area Highest Floor\x01",      # 3
            "C4301 Sealed Area Middle Floor\x01",       # 4
            "C4302 Sealed Area Lowest Floor\x01",       # 5
            "Cancel\x01",                               # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_204F"),
        (1, "loc_2058"),
        (2, "loc_2061"),
        (3, "loc_206A"),
        (4, "loc_2073"),
        (5, "loc_207C"),
        (SWITCH_DEFAULT, "loc_2085"),
    )


    label("loc_204F")

    NewScene("ED6_DT01/C4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2058")

    NewScene("ED6_DT01/C4202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2061")

    NewScene("ED6_DT01/C4204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_206A")

    NewScene("ED6_DT01/C4300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2073")

    NewScene("ED6_DT01/C4301   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_207C")

    NewScene("ED6_DT01/C4302   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2085")

    OP_5F(0x3)
    Jump("loc_208B")

    label("loc_208B")

    Jump("loc_2366")

    label("loc_208E")


    AnonymousTalk(    #27
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100 Erbe Scenic Route\x01",      # 0
            "R4100 Royal Avenue\x01",           # 1
            "Cancel\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20E7"),
        (1, "loc_20F0"),
        (SWITCH_DEFAULT, "loc_20F9"),
    )


    label("loc_20E7")

    NewScene("ED6_DT01/C4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_20F0")

    NewScene("ED6_DT01/R4100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_20F9")

    OP_5F(0x3)
    Jump("loc_20FF")

    label("loc_20FF")

    Jump("loc_2366")

    label("loc_2102")


    AnonymousTalk(    #28
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "C4111 Erbe Scenic Route\x01",                            # 0
            "C4113 Erbe Scenic Route\x01",                            # 1
            "T4302 Erbe Royal Villa Entrance Garden (Day)\x01",       # 2
            "T4303 Erbe Royal Villa Inner Garden, Hallways\x01",      # 3
            "T4312 Erbe Royal Villa Hall\x01",                        # 4
            "T4313 Erbe Royal Villa Guest Rooms\x01",                 # 5
            "T4150 Grancel - South Block\x01",                        # 6
            "T4151 Grancel - East Block\x01",                         # 7
            "T4152 Grancel - West Block\x01",                         # 8
            "T4153 Grancel - North Block\x01",                        # 9
            "T4203 Grancel Castle\x01",                               # 10
            "T4250 Grancel Castle Rooms\x01",                         # 11
            "Cancel\x01",                                             # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22C0"),
        (1, "loc_22CC"),
        (2, "loc_22D8"),
        (3, "loc_22E4"),
        (4, "loc_22F0"),
        (5, "loc_22FC"),
        (6, "loc_2308"),
        (7, "loc_2314"),
        (8, "loc_2320"),
        (9, "loc_232C"),
        (10, "loc_2338"),
        (11, "loc_2344"),
        (SWITCH_DEFAULT, "loc_2350"),
    )


    label("loc_22C0")

    NewScene("ED6_DT01/C4111   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_22CC")

    NewScene("ED6_DT01/C4113   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_22D8")

    NewScene("ED6_DT01/T4302   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_22E4")

    NewScene("ED6_DT01/T4303   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_22F0")

    NewScene("ED6_DT01/T4312   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_22FC")

    NewScene("ED6_DT01/T4313   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2308")

    NewScene("ED6_DT01/T4150   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2314")

    NewScene("ED6_DT01/T4151   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2320")

    NewScene("ED6_DT01/T4152   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_232C")

    NewScene("ED6_DT01/T4153   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2338")

    NewScene("ED6_DT01/T4203   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2344")

    NewScene("ED6_DT01/T4250   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_2356")

    label("loc_2350")

    OP_5F(0x3)
    Jump("loc_2356")

    label("loc_2356")

    Jump("loc_2366")

    label("loc_2359")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2366")

    label("loc_2366")

    Jump("loc_1DD5")

    label("loc_2369")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_1DCB end

    def Function_8_2379(): pass

    label("Function_8_2379")


    AnonymousTalk(    #29
        "\x06どこ？\x02",
    )


    label("loc_2383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2565")

    Menu(
        2,
        10,
        100,
        1,
        (
            "Various Ships\x01",      # 0
            "Skyboxes\x01",           # 1
            "Cancel\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23CB"),
        (1, "loc_250C"),
        (SWITCH_DEFAULT, "loc_2555"),
    )


    label("loc_23CB")


    AnonymousTalk(    #30
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0000 Liner Linde\x01",                # 0
            "E0001 Liner Cecilia (Green)\x01",      # 1
            "E0002 Ship Workshop\x01",              # 2
            "E0100 Airborne Ship\x01",              # 3
            "E0200 Military Ship\x01",              # 4
            "E0300 Arseille Deck\x01",              # 5
            "E0400 Special Forces Ship\x01",        # 6
            "E0111 Sky Devices\x01",                # 7
            "Cancel\x01",                           # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24BB"),
        (1, "loc_24C4"),
        (2, "loc_24CD"),
        (3, "loc_24D6"),
        (4, "loc_24DF"),
        (5, "loc_24E8"),
        (6, "loc_24F1"),
        (7, "loc_24FA"),
        (SWITCH_DEFAULT, "loc_2503"),
    )


    label("loc_24BB")

    NewScene("ED6_DT01/E0000   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24C4")

    NewScene("ED6_DT01/E0001   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24CD")

    NewScene("ED6_DT01/E0002   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24D6")

    NewScene("ED6_DT01/E0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24DF")

    NewScene("ED6_DT01/E0200   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24E8")

    NewScene("ED6_DT01/E0300   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24F1")

    NewScene("ED6_DT01/E0400   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_24FA")

    NewScene("ED6_DT01/E0111   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2503")

    OP_5F(0x3)
    Jump("loc_2509")

    label("loc_2509")

    Jump("loc_2562")

    label("loc_250C")


    AnonymousTalk(    #31
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0500 Skybox\x01",      # 0
            "Cancel\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2543"),
        (SWITCH_DEFAULT, "loc_254C"),
    )


    label("loc_2543")

    NewScene("ED6_DT01/E0500   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_254C")

    OP_5F(0x3)
    Jump("loc_2552")

    label("loc_2552")

    Jump("loc_2562")

    label("loc_2555")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2562")

    label("loc_2562")

    Jump("loc_2383")

    label("loc_2565")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_2379 end

    SaveToFile()

Try(main)
