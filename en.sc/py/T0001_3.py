from ED6SCScenarioHelper import *

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
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_10F",          # 01, 1
        "Function_2_359",          # 02, 2
        "Function_3_57C",          # 03, 3
        "Function_4_5E1",          # 04, 4
        "Function_5_A37",          # 05, 5
        "Function_6_CAF",          # 06, 6
        "Function_7_DE9",          # 07, 7
        "Function_8_14C1",         # 08, 8
        "Function_9_1C4F",         # 09, 9
        "Function_10_25B7",        # 0A, 10
        "Function_11_2DB0",        # 0B, 11
        "Function_12_3644",        # 0C, 12
        "Function_13_46C2",        # 0D, 13
        "Function_14_4BED",        # 0E, 14
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06Which?\x02",
    )


    label("loc_B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF")

    Menu(
        1,
        10,
        32,
        1,
        (
            "SC\x01",      # 0
            "FC\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E4"),
        (1, "loc_EB"),
        (SWITCH_DEFAULT, "loc_F2"),
    )


    label("loc_E4")

    Call(3, 1)
    Jump("loc_FC")

    label("loc_EB")

    Call(3, 2)
    Jump("loc_FC")

    label("loc_F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC")

    Jump("loc_B4")

    label("loc_FF")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_10F(): pass

    label("Function_1_10F")


    AnonymousTalk(    #1
        "\x06Which?\x02",
    )


    label("loc_119")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_349")

    Menu(
        2,
        10,
        100,
        1,
        (
            "A0020 Party and Dedicated NPL\x01",                              # 0
            "A0021 Battle Estelle, Joshua, Zin, Agate, Olivier\x01",          # 1
            "A0022 Battle Scherazard, Tita, Kloe, Kloe Formal\x01",           # 2
            "A0023 Battle Kevin, Anelace, Josette, Kurt\x01",                 # 3
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
        (0, "loc_2EB"),
        (1, "loc_2F4"),
        (2, "loc_2FD"),
        (3, "loc_306"),
        (4, "loc_30F"),
        (5, "loc_318"),
        (6, "loc_321"),
        (7, "loc_32A"),
        (8, "loc_333"),
        (SWITCH_DEFAULT, "loc_33C"),
    )


    label("loc_2EB")

    NewScene("ED6_DT21/A0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2F4")

    NewScene("ED6_DT21/A0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_2FD")

    NewScene("ED6_DT21/A0022   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_306")

    NewScene("ED6_DT21/A0023   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_30F")

    NewScene("ED6_DT21/A0024   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_318")

    NewScene("ED6_DT21/A0025   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_321")

    NewScene("ED6_DT21/A0026   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_32A")

    NewScene("ED6_DT21/A0027   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_333")

    NewScene("ED6_DT21/A0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_33C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_119")

    label("loc_349")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_10F end

    def Function_2_359(): pass

    label("Function_2_359")


    AnonymousTalk(    #2
        "\x06Which?\x02",
    )


    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56C")

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
            "37 NPC Battle Royal Guard, Officer, Agent, Lola, Risha, Kanoe\x01",      # 7
            "39座りキャラ\x01",                                                       # 8
            "Cancel\x01",                                                             # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_50E"),
        (1, "loc_517"),
        (2, "loc_520"),
        (3, "loc_529"),
        (4, "loc_532"),
        (5, "loc_53B"),
        (6, "loc_544"),
        (7, "loc_54D"),
        (8, "loc_556"),
        (SWITCH_DEFAULT, "loc_55F"),
    )


    label("loc_50E")

    NewScene("ED6_DT21/T0030   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_517")

    NewScene("ED6_DT21/T0031   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_520")

    NewScene("ED6_DT21/T0032   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_529")

    NewScene("ED6_DT21/T0033   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_532")

    NewScene("ED6_DT21/T0034   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_53B")

    NewScene("ED6_DT21/T0035   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_544")

    NewScene("ED6_DT21/T0036   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_54D")

    NewScene("ED6_DT21/T0037   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_556")

    NewScene("ED6_DT21/T0039   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_55F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_363")

    label("loc_56C")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_359 end

    def Function_3_57C(): pass

    label("Function_3_57C")


    AnonymousTalk(    #3
        "\x06Which?\x02",
    )


    label("loc_586")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D1")

    Menu(
        1,
        10,
        32,
        1,
        (
            "SC\x01",      # 0
            "FC\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B6"),
        (1, "loc_5BD"),
        (SWITCH_DEFAULT, "loc_5C4"),
    )


    label("loc_5B6")

    Call(3, 5)
    Jump("loc_5CE")

    label("loc_5BD")

    Call(3, 4)
    Jump("loc_5CE")

    label("loc_5C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CE")

    Jump("loc_586")

    label("loc_5D1")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_57C end

    def Function_4_5E1(): pass

    label("Function_4_5E1")


    AnonymousTalk(    #4
        "\x06Which?\x02",
    )


    label("loc_5EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A27")

    Menu(
        2,
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
        (0, "loc_954"),
        (1, "loc_95D"),
        (2, "loc_966"),
        (3, "loc_96F"),
        (4, "loc_978"),
        (5, "loc_981"),
        (6, "loc_98A"),
        (7, "loc_993"),
        (8, "loc_99C"),
        (9, "loc_9A5"),
        (10, "loc_9AE"),
        (11, "loc_9B7"),
        (12, "loc_9C0"),
        (13, "loc_9C9"),
        (14, "loc_9D2"),
        (15, "loc_9DB"),
        (16, "loc_9E4"),
        (17, "loc_9ED"),
        (18, "loc_9F6"),
        (19, "loc_9FF"),
        (20, "loc_A08"),
        (21, "loc_A11"),
        (SWITCH_DEFAULT, "loc_A1A"),
    )


    label("loc_954")

    NewScene("ED6_DT21/T0040   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_95D")

    NewScene("ED6_DT21/T0041   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_966")

    NewScene("ED6_DT21/T0042   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_96F")

    NewScene("ED6_DT21/T0057   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_978")

    NewScene("ED6_DT21/T0060   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_981")

    NewScene("ED6_DT21/T0043   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_98A")

    NewScene("ED6_DT21/T0044   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_993")

    NewScene("ED6_DT21/T0045   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_99C")

    NewScene("ED6_DT21/T0046   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9A5")

    NewScene("ED6_DT21/T0047   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9AE")

    NewScene("ED6_DT21/T0048   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9B7")

    NewScene("ED6_DT21/T0049   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9C0")

    NewScene("ED6_DT21/T0050   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9C9")

    NewScene("ED6_DT21/T0051   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9D2")

    NewScene("ED6_DT21/T0052   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9DB")

    NewScene("ED6_DT21/T0053   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9E4")

    NewScene("ED6_DT21/T0054   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9ED")

    NewScene("ED6_DT21/T0055   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9F6")

    NewScene("ED6_DT21/T0056   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_9FF")

    NewScene("ED6_DT21/T0058   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A08")

    NewScene("ED6_DT21/T0059   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A11")

    NewScene("ED6_DT21/T0061   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_A1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EB")

    label("loc_A27")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_5E1 end

    def Function_5_A37(): pass

    label("Function_5_A37")


    AnonymousTalk(    #5
        "\x06Which?\x02",
    )


    label("loc_A41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9F")

    Menu(
        2,
        10,
        32,
        1,
        (
            "A0000 Monster List (12000-12040)\x01",      # 0
            "A0001 Monster List (12050-12090)\x01",      # 1
            "A0002 Monster List (12100-12140)\x01",      # 2
            "A0003 Monster List (12150-12190)\x01",      # 3
            "A0004 Monster List (12200-12240)\x01",      # 4
            "A0005 Monster List (12250-12290)\x01",      # 5
            "A0006 Monster List (12300-12340)\x01",      # 6
            "A0007 Monster List (12350-12390)\x01",      # 7
            "A0008 Monster List (12400-12440)\x01",      # 8
            "A0009 Monster List (12450-12490)\x01",      # 9
            "A0010 Monster List (12500-12520)\x01",      # 10
            "A0011 Monster List (12530-12540)\x01",      # 11
            "Cancel\x01",                                # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C26"),
        (1, "loc_C2F"),
        (2, "loc_C38"),
        (3, "loc_C41"),
        (4, "loc_C4A"),
        (5, "loc_C53"),
        (6, "loc_C5C"),
        (7, "loc_C65"),
        (8, "loc_C6E"),
        (9, "loc_C77"),
        (10, "loc_C80"),
        (11, "loc_C89"),
        (SWITCH_DEFAULT, "loc_C92"),
    )


    label("loc_C26")

    NewScene("ED6_DT21/A0000   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C2F")

    NewScene("ED6_DT21/A0001   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C38")

    NewScene("ED6_DT21/A0002   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C41")

    NewScene("ED6_DT21/A0003   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C4A")

    NewScene("ED6_DT21/A0004   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C53")

    NewScene("ED6_DT21/A0005   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C5C")

    NewScene("ED6_DT21/A0006   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C65")

    NewScene("ED6_DT21/A0007   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C6E")

    NewScene("ED6_DT21/A0008   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C77")

    NewScene("ED6_DT21/A0009   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C80")

    NewScene("ED6_DT21/A0010   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C89")

    NewScene("ED6_DT21/A0011   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_C92")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A41")

    label("loc_C9F")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_A37 end

    def Function_6_CAF(): pass

    label("Function_6_CAF")


    AnonymousTalk(    #6
        "\x06[Maps] Select\x02",
    )


    label("loc_CC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD9")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Rolent Region\x01",                                         # 0
            "Bose Region\x01",                                           # 1
            "Ruan Region\x01",                                           # 2
            "Zeiss Region\x01",                                          # 3
            "Grancel Region\x01",                                        # 4
            "Aureole, Training Grounds, Aboard Glorious, etc.\x01",      # 5
            "Events, Airships\x01",                                      # 6
            "Movies\x01",                                                # 7
            "Cancel\x01",                                                # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D94"),
        (1, "loc_D9B"),
        (2, "loc_DA2"),
        (3, "loc_DA9"),
        (4, "loc_DB0"),
        (5, "loc_DB7"),
        (6, "loc_DBE"),
        (7, "loc_DC5"),
        (SWITCH_DEFAULT, "loc_DCC"),
    )


    label("loc_D94")

    Call(3, 7)
    Jump("loc_DD6")

    label("loc_D9B")

    Call(3, 8)
    Jump("loc_DD6")

    label("loc_DA2")

    Call(3, 9)
    Jump("loc_DD6")

    label("loc_DA9")

    Call(3, 10)
    Jump("loc_DD6")

    label("loc_DB0")

    Call(3, 11)
    Jump("loc_DD6")

    label("loc_DB7")

    Call(3, 12)
    Jump("loc_DD6")

    label("loc_DBE")

    Call(3, 13)
    Jump("loc_DD6")

    label("loc_DC5")

    Call(3, 14)
    Jump("loc_DD6")

    label("loc_DCC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD6")

    Jump("loc_CC0")

    label("loc_DD9")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_CAF end

    def Function_7_DE9(): pass

    label("Function_7_DE9")


    AnonymousTalk(    #7
        "\x06Where?\x02",
    )


    label("loc_DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14B1")

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
        (0, "loc_E48"),
        (1, "loc_100C"),
        (2, "loc_136F"),
        (3, "loc_143E"),
        (SWITCH_DEFAULT, "loc_14A4"),
    )


    label("loc_E48")


    AnonymousTalk(    #8
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T0100 Rolent\x01",                     # 0
            "T0200 Mayor's Manor\x01",              # 1
            "T0300 Bright House\x01",               # 2
            "T0400 Perzel Farm\x01",                # 3
            "T0401 Perzel Farm (Night)\x01",        # 4
            "T0500 Verte Guardpost\x01",            # 5
            "T0700 Landingport\x01",                # 6
            "T0300 Bright House\x01",               # 7
            "T0600 Gurune Gate\x01",                # 8
            "T0101 Rolent (Night)\x01",             # 9
            "T0201 Mayor's Manor (Night)\x01",      # 10
            "T0701 Landing Port (Night)\x01",       # 11
            "Cancel\x01",                           # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F97"),
        (1, "loc_FA0"),
        (2, "loc_FA9"),
        (3, "loc_FB2"),
        (4, "loc_FBB"),
        (5, "loc_FC4"),
        (6, "loc_FCD"),
        (7, "loc_FD6"),
        (8, "loc_FDF"),
        (9, "loc_FE8"),
        (10, "loc_FF1"),
        (11, "loc_FFA"),
        (SWITCH_DEFAULT, "loc_1003"),
    )


    label("loc_F97")

    NewScene("ED6_DT21/T0100   ._SN", 119, 0, 0)
    IdleLoop()

    label("loc_FA0")

    NewScene("ED6_DT21/T0200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FA9")

    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FB2")

    NewScene("ED6_DT21/T0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FBB")

    NewScene("ED6_DT21/T0401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FC4")

    NewScene("ED6_DT21/T0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FCD")

    NewScene("ED6_DT21/T0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FD6")

    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FDF")

    NewScene("ED6_DT21/T0600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FE8")

    NewScene("ED6_DT21/T0101   ._SN", 119, 0, 0)
    IdleLoop()

    label("loc_FF1")

    NewScene("ED6_DT21/T0201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_FFA")

    NewScene("ED6_DT21/T0701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1003")

    OP_5F(0x3)
    Jump("loc_1009")

    label("loc_1009")

    Jump("loc_14AE")

    label("loc_100C")


    AnonymousTalk(    #9
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "C0100 Malga Mine (FC)\x01",                                                    # 0
            "C0101 Malga Mine (SC Chapter 8 quest)\x01",                                    # 1
            "C0300 Mistwald Forest\x01",                                                    # 2
            "C0304 Mistwald Forest Loop\x01",                                               # 3
            "C0500 Underground Waterways\x01",                                              # 4
            "C0411 Esmelas Tower 1F (FC)\x01",                                              # 5
            "C0412 Esmelas Tower 2F (FC)\x01",                                              # 6
            "C0413 Esmelas Tower 3F (FC)\x01",                                              # 7
            "C0414 Esmelas Tower 4F (FC)\x01",                                              # 8
            "C0415 Esmelas Tower 5F (FC)\x01",                                              # 9
            "C0700 Esmelas Tower 1F (SC)\x01",                                              # 10
            "C0701 Esmelas Tower 2F (SC)\x01",                                              # 11
            "C0702 Esmelas Tower 3F (SC)\x01",                                              # 12
            "C0703 Esmelas Tower 4F (SC)\x01",                                              # 13
            "C0704 Esmelas Tower 5F (SC)\x01",                                              # 14
            "C0705 Esmelas Tower Roof (SC Dimensional Background)\x01",                     # 15
            "C0706 Esmelas Tower Roof (SC Dimensional Background, Arseille View)\x01",      # 16
            "C0707 Esmelas Tower Roof (SC Normal Background)\x01",                          # 17
            "Cancel\x01",                                                                   # 18
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12C4"),
        (1, "loc_12CD"),
        (2, "loc_12D6"),
        (3, "loc_12DF"),
        (4, "loc_12E8"),
        (5, "loc_12F1"),
        (6, "loc_12FA"),
        (7, "loc_1303"),
        (8, "loc_130C"),
        (9, "loc_1315"),
        (10, "loc_131E"),
        (11, "loc_1327"),
        (12, "loc_1330"),
        (13, "loc_1339"),
        (14, "loc_1342"),
        (15, "loc_134B"),
        (16, "loc_1354"),
        (17, "loc_135D"),
        (SWITCH_DEFAULT, "loc_1366"),
    )


    label("loc_12C4")

    NewScene("ED6_DT21/C0100   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_12CD")

    NewScene("ED6_DT21/C0101   ._SN", 103, 0, 0)
    IdleLoop()

    label("loc_12D6")

    NewScene("ED6_DT21/C0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_12DF")

    NewScene("ED6_DT21/C0304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_12E8")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_12F1")

    NewScene("ED6_DT21/C0411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_12FA")

    NewScene("ED6_DT21/C0412   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1303")

    NewScene("ED6_DT21/C0413   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_130C")

    NewScene("ED6_DT21/C0414   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1315")

    NewScene("ED6_DT21/C0415   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_131E")

    NewScene("ED6_DT21/C0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1327")

    NewScene("ED6_DT21/C0701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1330")

    NewScene("ED6_DT21/C0702   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1339")

    NewScene("ED6_DT21/C0703   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1342")

    NewScene("ED6_DT21/C0704   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_134B")

    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1354")

    NewScene("ED6_DT21/C0706   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_135D")

    NewScene("ED6_DT21/C0707   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1366")

    OP_5F(0x3)
    Jump("loc_136C")

    label("loc_136C")

    Jump("loc_14AE")

    label("loc_136F")


    AnonymousTalk(    #10
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "R0100 Elize Highway\x01",                      # 0
            "R0200 Milch Main Road\x01",                    # 1
            "R0300 Malga Trail\x01",                        # 2
            "R0203 Milch Main Road, Army Airship\x01",      # 3
            "Cancel\x01",                                   # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1405"),
        (1, "loc_1411"),
        (2, "loc_141D"),
        (3, "loc_1429"),
        (SWITCH_DEFAULT, "loc_1435"),
    )


    label("loc_1405")

    NewScene("ED6_DT21/R0100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_143B")

    label("loc_1411")

    NewScene("ED6_DT21/R0200   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_143B")

    label("loc_141D")

    NewScene("ED6_DT21/R0300   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_143B")

    label("loc_1429")

    NewScene("ED6_DT21/R0203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_143B")

    label("loc_1435")

    OP_5F(0x3)
    Jump("loc_143B")

    label("loc_143B")

    Jump("loc_14AE")

    label("loc_143E")


    AnonymousTalk(    #11
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
        (0, "loc_148F"),
        (SWITCH_DEFAULT, "loc_149B"),
    )


    label("loc_148F")

    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_149B")

    OP_5F(0x3)
    Jump("loc_14A1")

    label("loc_14A1")

    Jump("loc_14AE")

    label("loc_14A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AE")

    Jump("loc_DF3")

    label("loc_14B1")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_DE9 end

    def Function_8_14C1(): pass

    label("Function_8_14C1")


    AnonymousTalk(    #12
        "\x06Where?\x02",
    )


    label("loc_14CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C3F")

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
        (0, "loc_1520"),
        (1, "loc_16F8"),
        (2, "loc_1A24"),
        (3, "loc_1B47"),
        (SWITCH_DEFAULT, "loc_1C2F"),
    )


    label("loc_1520")


    AnonymousTalk(    #13
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
            "T1211 Ravennue Village(Night)\x01",        # 6
            "T1400 Haken Gate\x01",                     # 7
            "T1402 Haken Gate North Plain\x01",         # 8
            "T1500 Lakeshore Inn\x01",                  # 9
            "T1103 Bose Ruins\x01",                     # 10
            "Cancel\x01",                               # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_168C"),
        (1, "loc_1695"),
        (2, "loc_169E"),
        (3, "loc_16A7"),
        (4, "loc_16B0"),
        (5, "loc_16B9"),
        (6, "loc_16C2"),
        (7, "loc_16CB"),
        (8, "loc_16D4"),
        (9, "loc_16DD"),
        (10, "loc_16E6"),
        (SWITCH_DEFAULT, "loc_16EF"),
    )


    label("loc_168C")

    NewScene("ED6_DT21/T1100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1695")

    NewScene("ED6_DT21/T1110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_169E")

    NewScene("ED6_DT21/T1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16A7")

    NewScene("ED6_DT21/T1301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16B0")

    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16B9")

    NewScene("ED6_DT21/T1200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16C2")

    NewScene("ED6_DT21/T1211   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16CB")

    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16D4")

    NewScene("ED6_DT21/T1402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16DD")

    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16E6")

    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16EF")

    OP_5F(0x3)
    Jump("loc_16F5")

    label("loc_16F5")

    Jump("loc_1C3C")

    label("loc_16F8")


    AnonymousTalk(    #14
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400 Nebel Valley\x01",                                                      # 0
            "C1102 Ravennue Abandoned Mine (SC)\x01",                                      # 1
            "C1300 Sky Bandit Stronghold\x01",                                             # 2
            "C1600 Ancient Dragon Nest\x01",                                               # 3
            "C1211 Amberl Tower 1F (FC)\x01",                                              # 4
            "C1212 Amberl Tower 2F (FC)\x01",                                              # 5
            "C1213 Amberl Tower 3F (FC)\x01",                                              # 6
            "C1214 Amberl Tower 4F (FC)\x01",                                              # 7
            "C1215 Amberl Tower 5F (FC)\x01",                                              # 8
            "C1700 Amberl Tower 1F (SC)\x01",                                              # 9
            "C1701 Amberl Tower 2F (SC)\x01",                                              # 10
            "C1702 Amberl Tower 3F (SC)\x01",                                              # 11
            "C1703 Amberl Tower 4F (SC)\x01",                                              # 12
            "C1704 Amberl Tower 5F (SC)\x01",                                              # 13
            "C1705 Amberl Tower Roof (SC Dimensional Background)\x01",                     # 14
            "C1706 Amberl Tower Roof (SC Dimensional Background, Arseille View)\x01",      # 15
            "C1707 Amberl Tower Roof (SC Normal Background)\x01",                          # 16
            "Cancel\x01",                                                                  # 17
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1982"),
        (1, "loc_198B"),
        (2, "loc_1994"),
        (3, "loc_199D"),
        (4, "loc_19A6"),
        (5, "loc_19AF"),
        (6, "loc_19B8"),
        (7, "loc_19C1"),
        (8, "loc_19CA"),
        (9, "loc_19D3"),
        (10, "loc_19DC"),
        (11, "loc_19E5"),
        (12, "loc_19EE"),
        (13, "loc_19F7"),
        (14, "loc_1A00"),
        (15, "loc_1A09"),
        (16, "loc_1A12"),
        (SWITCH_DEFAULT, "loc_1A1B"),
    )


    label("loc_1982")

    NewScene("ED6_DT21/C1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_198B")

    NewScene("ED6_DT21/C1102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1994")

    NewScene("ED6_DT21/C1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_199D")

    NewScene("ED6_DT21/C1600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19A6")

    NewScene("ED6_DT21/C1211   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19AF")

    NewScene("ED6_DT21/C1212   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19B8")

    NewScene("ED6_DT21/C1213   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19C1")

    NewScene("ED6_DT21/C1214   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19CA")

    NewScene("ED6_DT21/C1215   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19D3")

    NewScene("ED6_DT21/C1700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19DC")

    NewScene("ED6_DT21/C1701   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19E5")

    NewScene("ED6_DT21/C1702   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19EE")

    NewScene("ED6_DT21/C1703   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_19F7")

    NewScene("ED6_DT21/C1704   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A00")

    NewScene("ED6_DT21/C1705   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A09")

    NewScene("ED6_DT21/C1706   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A12")

    NewScene("ED6_DT21/C1707   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1A1B")

    OP_5F(0x3)
    Jump("loc_1A21")

    label("loc_1A21")

    Jump("loc_1C3C")

    label("loc_1A24")


    AnonymousTalk(    #15
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
        (0, "loc_1AFF"),
        (1, "loc_1B08"),
        (2, "loc_1B11"),
        (3, "loc_1B1A"),
        (4, "loc_1B23"),
        (5, "loc_1B2C"),
        (6, "loc_1B35"),
        (SWITCH_DEFAULT, "loc_1B3E"),
    )


    label("loc_1AFF")

    NewScene("ED6_DT21/C1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B08")

    NewScene("ED6_DT21/R1300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B11")

    NewScene("ED6_DT21/R1100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B1A")

    NewScene("ED6_DT21/R1200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B23")

    NewScene("ED6_DT21/R1400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B2C")

    NewScene("ED6_DT21/R1403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B35")

    NewScene("ED6_DT21/R1500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1B3E")

    OP_5F(0x3)
    Jump("loc_1B44")

    label("loc_1B44")

    Jump("loc_1C3C")

    label("loc_1B47")


    AnonymousTalk(    #16
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        120,
        1,
        (
            "T1401 Haken Gate\x01",                   # 0
            "T1311 Krone Guardpost\x01",              # 1
            "C1402 Nebel Valley\x01",                 # 2
            "R1203 West Bose Highway\x01",            # 3
            "C1104 Ravennue Abandoned Mine\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BEA"),
        (1, "loc_1BF6"),
        (2, "loc_1C02"),
        (3, "loc_1C0E"),
        (4, "loc_1C1A"),
        (SWITCH_DEFAULT, "loc_1C26"),
    )


    label("loc_1BEA")

    NewScene("ED6_DT21/T1401   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2C")

    label("loc_1BF6")

    NewScene("ED6_DT21/T1311   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2C")

    label("loc_1C02")

    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2C")

    label("loc_1C0E")

    NewScene("ED6_DT21/R1203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1C2C")

    label("loc_1C1A")

    NewScene("ED6_DT21/C1104   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_1C2C")

    label("loc_1C26")

    OP_5F(0x3)
    Jump("loc_1C2C")

    label("loc_1C2C")

    Jump("loc_1C3C")

    label("loc_1C2F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C3C")

    label("loc_1C3C")

    Jump("loc_14CB")

    label("loc_1C3F")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_14C1 end

    def Function_9_1C4F(): pass

    label("Function_9_1C4F")


    AnonymousTalk(    #17
        "\x06Where?\x02",
    )


    label("loc_1C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A7")

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
        (0, "loc_1CB8"),
        (1, "loc_2049"),
        (2, "loc_2368"),
        (3, "loc_2476"),
        (4, "loc_252D"),
        (SWITCH_DEFAULT, "loc_2597"),
    )


    label("loc_1CB8")


    AnonymousTalk(    #18
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
            "T2601 Royal Academy Old Schoolhouse (Night)\x01",                         # 17
            "T2810 Royal Academy Main Building (Night)\x01",                           # 18
            "T2105 Ruan City (Night)\x01",                                             # 19
            "Cancel\x01",                                                              # 20
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F8C"),
        (1, "loc_1F95"),
        (2, "loc_1F9E"),
        (3, "loc_1FA7"),
        (4, "loc_1FB0"),
        (5, "loc_1FB9"),
        (6, "loc_1FC2"),
        (7, "loc_1FCB"),
        (8, "loc_1FD4"),
        (9, "loc_1FDD"),
        (10, "loc_1FE6"),
        (11, "loc_1FEF"),
        (12, "loc_1FF8"),
        (13, "loc_2001"),
        (14, "loc_200A"),
        (15, "loc_2013"),
        (16, "loc_201C"),
        (17, "loc_2025"),
        (18, "loc_202E"),
        (19, "loc_2037"),
        (SWITCH_DEFAULT, "loc_2040"),
    )


    label("loc_1F8C")

    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1F95")

    NewScene("ED6_DT21/T2102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1F9E")

    NewScene("ED6_DT21/T2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FA7")

    NewScene("ED6_DT21/T2600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FB0")

    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FB9")

    NewScene("ED6_DT21/T2520   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FC2")

    NewScene("ED6_DT21/T2530   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FCB")

    NewScene("ED6_DT21/T2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FD4")

    NewScene("ED6_DT21/T2401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FDD")

    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FE6")

    NewScene("ED6_DT21/T2110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FEF")

    NewScene("ED6_DT21/T2120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1FF8")

    NewScene("ED6_DT21/T2130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2001")

    NewScene("ED6_DT21/T2131   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_200A")

    NewScene("ED6_DT21/T2700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2013")

    NewScene("ED6_DT21/T2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_201C")

    NewScene("ED6_DT21/T2411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2025")

    NewScene("ED6_DT21/T2601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_202E")

    NewScene("ED6_DT21/T2810   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2037")

    NewScene("ED6_DT21/T2105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2040")

    OP_5F(0x3)
    Jump("loc_2046")

    label("loc_2046")

    Jump("loc_25A4")

    label("loc_2049")


    AnonymousTalk(    #19
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C2209 Lighthouse\x01",                                                          # 0
            "C2200 Lighthouse (Night)\x01",                                                  # 1
            "C2400 Old Schoolhouse Underground Ruins\x01",                                   # 2
            "C2111 Sapphirl Tower 1F (FC)\x01",                                              # 3
            "C2112 Sapphirl Tower 2F (FC)\x01",                                              # 4
            "C2113 Sapphirl Tower 3F (FC)\x01",                                              # 5
            "C2114 Sapphirl Tower 4F (FC)\x01",                                              # 6
            "C2115 Sapphirl Tower 5F (FC)\x01",                                              # 7
            "C2300 Sapphirl Tower 1F (SC)\x01",                                              # 8
            "C2301 Sapphirl Tower 2F (SC)\x01",                                              # 9
            "C2302 Sapphirl Tower 3F (SC)\x01",                                              # 10
            "C2303 Sapphirl Tower 4F (SC)\x01",                                              # 11
            "C2304 Sapphirl Tower 5F (SC)\x01",                                              # 12
            "C2305 Sapphirl Tower Roof (SC Dimensional Background)\x01",                     # 13
            "C2306 Sapphirl Tower Roof (SC Dimensional Background, Arseille View)\x01",      # 14
            "C2307 Sapphirl Tower Roof (SC Normal Background)\x01",                          # 15
            "Cancel\x01",                                                                    # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22CF"),
        (1, "loc_22D8"),
        (2, "loc_22E1"),
        (3, "loc_22EA"),
        (4, "loc_22F3"),
        (5, "loc_22FC"),
        (6, "loc_2305"),
        (7, "loc_230E"),
        (8, "loc_2317"),
        (9, "loc_2320"),
        (10, "loc_2329"),
        (11, "loc_2332"),
        (12, "loc_233B"),
        (13, "loc_2344"),
        (14, "loc_234D"),
        (15, "loc_2356"),
        (SWITCH_DEFAULT, "loc_235F"),
    )


    label("loc_22CF")

    NewScene("ED6_DT21/C2209   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22D8")

    NewScene("ED6_DT21/C2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22E1")

    NewScene("ED6_DT21/C2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22EA")

    NewScene("ED6_DT21/C2111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22F3")

    NewScene("ED6_DT21/C2112   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_22FC")

    NewScene("ED6_DT21/C2113   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2305")

    NewScene("ED6_DT21/C2114   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_230E")

    NewScene("ED6_DT21/C2115   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2317")

    NewScene("ED6_DT21/C2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2320")

    NewScene("ED6_DT21/C2301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2329")

    NewScene("ED6_DT21/C2302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2332")

    NewScene("ED6_DT21/C2303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_233B")

    NewScene("ED6_DT21/C2304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2344")

    NewScene("ED6_DT21/C2305   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_234D")

    NewScene("ED6_DT21/C2306   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2356")

    NewScene("ED6_DT21/C2307   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_235F")

    OP_5F(0x3)
    Jump("loc_2365")

    label("loc_2365")

    Jump("loc_25A4")

    label("loc_2368")


    AnonymousTalk(    #20
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1501 Krone Trail\x01",                         # 0
            "R2100 Manoria Byroad\x01",                      # 1
            "R2400 Aurian Causeway\x01",                     # 2
            "R2200 Gull Seaside Way\x01",                    # 3
            "R2300 Vista Forest Road\x01",                   # 4
            "R2203 Gull Seaside Way, Army Airship\x01",      # 5
            "Cancel\x01",                                    # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2437"),
        (1, "loc_2440"),
        (2, "loc_2449"),
        (3, "loc_2452"),
        (4, "loc_245B"),
        (5, "loc_2464"),
        (SWITCH_DEFAULT, "loc_246D"),
    )


    label("loc_2437")

    NewScene("ED6_DT21/C1501   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2440")

    NewScene("ED6_DT21/R2100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2449")

    NewScene("ED6_DT21/R2400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2452")

    NewScene("ED6_DT21/R2200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_245B")

    NewScene("ED6_DT21/R2300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2464")

    NewScene("ED6_DT21/R2203   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_246D")

    OP_5F(0x3)
    Jump("loc_2473")

    label("loc_2473")

    Jump("loc_25A4")

    label("loc_2476")


    AnonymousTalk(    #21
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
        (0, "loc_24F4"),
        (1, "loc_2500"),
        (2, "loc_250C"),
        (3, "loc_2518"),
        (SWITCH_DEFAULT, "loc_2524"),
    )


    label("loc_24F4")

    NewScene("ED6_DT21/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_252A")

    label("loc_2500")

    NewScene("ED6_DT21/R2111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_252A")

    label("loc_250C")

    NewScene("ED6_DT21/T2403   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_252A")

    label("loc_2518")

    NewScene("ED6_DT21/R2412   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_252A")

    label("loc_2524")

    OP_5F(0x3)
    Jump("loc_252A")

    label("loc_252A")

    Jump("loc_25A4")

    label("loc_252D")


    AnonymousTalk(    #22
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
        (0, "loc_2576"),
        (1, "loc_2582"),
        (SWITCH_DEFAULT, "loc_258E"),
    )


    label("loc_2576")

    NewScene("ED6_DT21/T2103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2594")

    label("loc_2582")

    NewScene("ED6_DT21/T2104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2594")

    label("loc_258E")

    OP_5F(0x3)
    Jump("loc_2594")

    label("loc_2594")

    Jump("loc_25A4")

    label("loc_2597")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_25A4")

    label("loc_25A4")

    Jump("loc_1C59")

    label("loc_25A7")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_1C4F end

    def Function_10_25B7(): pass

    label("Function_10_25B7")


    AnonymousTalk(    #23
        "\x06Where?\x02",
    )


    label("loc_25C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA0")

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
        (0, "loc_2616"),
        (1, "loc_283B"),
        (2, "loc_2C3A"),
        (3, "loc_2D1F"),
        (SWITCH_DEFAULT, "loc_2D90"),
    )


    label("loc_2616")


    AnonymousTalk(    #24
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
            "T3401 Sanktheim Gate After Earthquake\x01",      # 10
            "T3103 Zeiss City (Night)\x01",                   # 11
            "T3106 Zeiss City (Power Outage Event)\x01",      # 12
            "Cancel\x01",                                     # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27BD"),
        (1, "loc_27C6"),
        (2, "loc_27CF"),
        (3, "loc_27D8"),
        (4, "loc_27E1"),
        (5, "loc_27EA"),
        (6, "loc_27F3"),
        (7, "loc_27FC"),
        (8, "loc_2805"),
        (9, "loc_280E"),
        (10, "loc_2817"),
        (11, "loc_2820"),
        (12, "loc_2829"),
        (SWITCH_DEFAULT, "loc_2832"),
    )


    label("loc_27BD")

    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27C6")

    NewScene("ED6_DT21/T3110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27CF")

    NewScene("ED6_DT21/T3111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27D8")

    NewScene("ED6_DT21/T3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27E1")

    NewScene("ED6_DT21/T3130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27EA")

    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27F3")

    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_27FC")

    NewScene("ED6_DT21/T3200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2805")

    NewScene("ED6_DT21/T3201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_280E")

    NewScene("ED6_DT21/T3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2817")

    NewScene("ED6_DT21/T3401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2820")

    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2829")

    NewScene("ED6_DT21/T3106   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2832")

    OP_5F(0x3)
    Jump("loc_2838")

    label("loc_2838")

    Jump("loc_2D9D")

    label("loc_283B")


    AnonymousTalk(    #25
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3100 Leiston Fortress Outside\x01",                                            # 0
            "C3110 Leiston Fortress Inside\x01",                                             # 1
            "C3104 Leiston Fortress Outside (Night)\x01",                                    # 2
            "C3108 Leiston Fortress (No Ships)\x01",                                         # 3
            "C3300 Kaldia Limestone Cave\x01",                                               # 4
            "C3303 Kaldia Limestone Cave Boss\x01",                                          # 5
            "C3400 Hot Springs Entrance\x01",                                                # 6
            "C3401 Hot Springs\x01",                                                         # 7
            "C3511 Carnelia Tower 1F (FC)\x01",                                              # 8
            "C3512 Carnelia Tower 2F (FC)\x01",                                              # 9
            "C3513 Carnelia Tower 3F (FC)\x01",                                              # 10
            "C3514 Carnelia Tower 4F (FC)\x01",                                              # 11
            "C3515 Carnelia Tower 5F (FC)\x01",                                              # 12
            "C3600 Carnelia Tower 1F (SC)\x01",                                              # 13
            "C3601 Carnelia Tower 2F (SC)\x01",                                              # 14
            "C3602 Carnelia Tower 3F (SC)\x01",                                              # 15
            "C3603 Carnelia Tower 4F (SC)\x01",                                              # 16
            "C3604 Carnelia Tower 5F (SC）\x01",                                             # 17
            "C3605 Carnelia Tower Roof (SC Dimensional Background)\x01",                     # 18
            "C3606 Carnelia Tower Roof (SC Dimensional Background, Arseille View)\x01",      # 19
            "C3607 Carnelia Tower Roof (SC Normal Background)\x01",                          # 20
            "Cancel\x01",                                                                    # 21
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B74"),
        (1, "loc_2B7D"),
        (2, "loc_2B86"),
        (3, "loc_2B8F"),
        (4, "loc_2B98"),
        (5, "loc_2BA1"),
        (6, "loc_2BAA"),
        (7, "loc_2BB3"),
        (8, "loc_2BBC"),
        (9, "loc_2BC5"),
        (10, "loc_2BCE"),
        (11, "loc_2BD7"),
        (12, "loc_2BE0"),
        (13, "loc_2BE9"),
        (14, "loc_2BF2"),
        (15, "loc_2BFB"),
        (16, "loc_2C04"),
        (17, "loc_2C0D"),
        (18, "loc_2C16"),
        (19, "loc_2C1F"),
        (20, "loc_2C28"),
        (SWITCH_DEFAULT, "loc_2C31"),
    )


    label("loc_2B74")

    NewScene("ED6_DT21/C3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B7D")

    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B86")

    NewScene("ED6_DT21/C3104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B8F")

    NewScene("ED6_DT21/C3108   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B98")

    NewScene("ED6_DT21/C3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BA1")

    NewScene("ED6_DT21/C3303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BAA")

    NewScene("ED6_DT21/C3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BB3")

    NewScene("ED6_DT21/C3401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BBC")

    NewScene("ED6_DT21/C3511   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BC5")

    NewScene("ED6_DT21/C3512   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BCE")

    NewScene("ED6_DT21/C3513   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BD7")

    NewScene("ED6_DT21/C3514   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BE0")

    NewScene("ED6_DT21/C3515   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BE9")

    NewScene("ED6_DT21/C3600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BF2")

    NewScene("ED6_DT21/C3601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2BFB")

    NewScene("ED6_DT21/C3602   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C04")

    NewScene("ED6_DT21/C3603   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C0D")

    NewScene("ED6_DT21/C3604   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C16")

    NewScene("ED6_DT21/C3605   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C1F")

    NewScene("ED6_DT21/C3606   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C28")

    NewScene("ED6_DT21/C3607   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2C31")

    OP_5F(0x3)
    Jump("loc_2C37")

    label("loc_2C37")

    Jump("loc_2D9D")

    label("loc_2C3A")


    AnonymousTalk(    #26
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300 Soldat Army Road\x01",            # 0
            "R3400 Kaldia Tunnel\x01",               # 1
            "R3100 Tratt Plains Road\x01",           # 2
            "R3200 Ritter Roadway\x01",              # 3
            "R3105 Tratt Plains Road Pool\x01",      # 4
            "Cancel\x01",                            # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CE9"),
        (1, "loc_2CF2"),
        (2, "loc_2CFB"),
        (3, "loc_2D04"),
        (4, "loc_2D0D"),
        (SWITCH_DEFAULT, "loc_2D16"),
    )


    label("loc_2CE9")

    NewScene("ED6_DT21/R3300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2CF2")

    NewScene("ED6_DT21/R3400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2CFB")

    NewScene("ED6_DT21/R3100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2D04")

    NewScene("ED6_DT21/R3200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2D0D")

    NewScene("ED6_DT21/R3105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2D16")

    OP_5F(0x3)
    Jump("loc_2D1C")

    label("loc_2D1C")

    Jump("loc_2D9D")

    label("loc_2D1F")


    AnonymousTalk(    #27
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
        (0, "loc_2D6F"),
        (1, "loc_2D7B"),
        (SWITCH_DEFAULT, "loc_2D87"),
    )


    label("loc_2D6F")

    NewScene("ED6_DT21/T3103   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D8D")

    label("loc_2D7B")

    NewScene("ED6_DT21/T3104   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2D8D")

    label("loc_2D87")

    OP_5F(0x3)
    Jump("loc_2D8D")

    label("loc_2D8D")

    Jump("loc_2D9D")

    label("loc_2D90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9D")

    label("loc_2D9D")

    Jump("loc_25C1")

    label("loc_2DA0")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_25B7 end

    def Function_11_2DB0(): pass

    label("Function_11_2DB0")


    AnonymousTalk(    #28
        "\x06Where?\x02",
    )


    label("loc_2DBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3634")

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
        (0, "loc_2E0F"),
        (1, "loc_31AF"),
        (2, "loc_32E4"),
        (3, "loc_3384"),
        (SWITCH_DEFAULT, "loc_3624"),
    )


    label("loc_2E0F")


    AnonymousTalk(    #29
        "\x06Where\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "----- Grancel\x01",                            # 0
            "T4200 Grancel Castle\x01",                     # 1
            "T4300 Erbe Royal Villa (Night)\x01",           # 2
            "T4133 Hotel Rooms (Night)\x01",                # 3
            "T4134 Cathedral Rooms (Night)\x01",            # 4
            "T4135 Museum Rooms\x01",                       # 5
            "T4136 Grand Arena Rooms\x01",                  # 6
            "T4400 Port\x01",                               # 7
            "T4138 Erebonian Embassy Inside\x01",           # 8
            "T4139 Calvardian Embassy Inside\x01",          # 9
            "T4140 Weapon Shop, Factory (Night)\x01",       # 10
            "T4141 Edel Department Store (Night)\x01",      # 11
            "T4142 Bar (Night)\x01",                        # 12
            "T4143 Inside Black Market Store\x01",          # 13
            "Cancel\x01",                                   # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FD4"),
        (1, "loc_3131"),
        (2, "loc_313A"),
        (3, "loc_3143"),
        (4, "loc_314C"),
        (5, "loc_3155"),
        (6, "loc_315E"),
        (7, "loc_3167"),
        (8, "loc_3170"),
        (9, "loc_3179"),
        (10, "loc_3182"),
        (11, "loc_318B"),
        (12, "loc_3194"),
        (13, "loc_319D"),
        (SWITCH_DEFAULT, "loc_31A6"),
    )


    label("loc_2FD4")


    AnonymousTalk(    #30
        "\x06Where?\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "T4100 Grancel - South Block\x01",                  # 0
            "T4101 Grancel - East Block\x01",                   # 1
            "T4102 Grancel - West Block\x01",                   # 2
            "T4103 Grancel - North Block\x01",                  # 3
            "T4104 Grancel - Coliseum Inside\x01",              # 4
            "T4105 Grancel - Landing Port\x01",                 # 5
            "T4106 Grancel - Landing Port (Arseille)\x01",      # 6
            "Cancel\x01",                                       # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30E9"),
        (1, "loc_30F2"),
        (2, "loc_30FB"),
        (3, "loc_3104"),
        (4, "loc_310D"),
        (5, "loc_3116"),
        (6, "loc_311F"),
        (SWITCH_DEFAULT, "loc_3128"),
    )


    label("loc_30E9")

    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_30F2")

    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_30FB")

    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3104")

    NewScene("ED6_DT21/T4103   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_310D")

    NewScene("ED6_DT21/T4104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3116")

    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_311F")

    NewScene("ED6_DT21/T4106   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3128")

    OP_5F(0x4)
    OP_5F(0x3)
    Jump("loc_31AC")

    label("loc_3131")

    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_313A")

    NewScene("ED6_DT21/T4300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3143")

    NewScene("ED6_DT21/T4133   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_314C")

    NewScene("ED6_DT21/T4134   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3155")

    NewScene("ED6_DT21/T4135   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_315E")

    NewScene("ED6_DT21/T4136   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3167")

    NewScene("ED6_DT21/T4400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3170")

    NewScene("ED6_DT21/T4138   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3179")

    NewScene("ED6_DT21/T4139   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3182")

    NewScene("ED6_DT21/T4140   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_318B")

    NewScene("ED6_DT21/T4141   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3194")

    NewScene("ED6_DT21/T4142   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_319D")

    NewScene("ED6_DT21/T4143   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_31A6")

    OP_5F(0x3)
    Jump("loc_31AC")

    label("loc_31AC")

    Jump("loc_3631")

    label("loc_31AF")


    AnonymousTalk(    #31
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
        (0, "loc_32A5"),
        (1, "loc_32AE"),
        (2, "loc_32B7"),
        (3, "loc_32C0"),
        (4, "loc_32C9"),
        (5, "loc_32D2"),
        (SWITCH_DEFAULT, "loc_32DB"),
    )


    label("loc_32A5")

    NewScene("ED6_DT21/C4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32AE")

    NewScene("ED6_DT21/C4202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32B7")

    NewScene("ED6_DT21/C4204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32C0")

    NewScene("ED6_DT21/C4300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32C9")

    NewScene("ED6_DT21/C4301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32D2")

    NewScene("ED6_DT21/C4302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_32DB")

    OP_5F(0x3)
    Jump("loc_32E1")

    label("loc_32E1")

    Jump("loc_3631")

    label("loc_32E4")


    AnonymousTalk(    #32
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100 Erbe Scenic Route\x01",             # 0
            "R4100 Royal Avenue\x01",                  # 1
            "C4103 Erbe Scenic Route - Lake\x01",      # 2
            "Cancel\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3360"),
        (1, "loc_3369"),
        (2, "loc_3372"),
        (SWITCH_DEFAULT, "loc_337B"),
    )


    label("loc_3360")

    NewScene("ED6_DT21/C4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3369")

    NewScene("ED6_DT21/R4100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3372")

    NewScene("ED6_DT21/C4103   ._SN", 101, 0, 0)
    IdleLoop()

    label("loc_337B")

    OP_5F(0x3)
    Jump("loc_3381")

    label("loc_3381")

    Jump("loc_3631")

    label("loc_3384")


    AnonymousTalk(    #33
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
            "T4156 Grancel (Arseille Port)\x01",                      # 10
            "T4203 Grancel Castle\x01",                               # 11
            "T4250 Grancel Castle Rooms\x01",                         # 12
            "T4403 Port\x01",                                         # 13
            "Cancel\x01",                                             # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3573"),
        (1, "loc_357F"),
        (2, "loc_358B"),
        (3, "loc_3597"),
        (4, "loc_35A3"),
        (5, "loc_35AF"),
        (6, "loc_35BB"),
        (7, "loc_35C7"),
        (8, "loc_35D3"),
        (9, "loc_35DF"),
        (10, "loc_35EB"),
        (11, "loc_35F7"),
        (12, "loc_3603"),
        (13, "loc_360F"),
        (SWITCH_DEFAULT, "loc_361B"),
    )


    label("loc_3573")

    NewScene("ED6_DT21/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_357F")

    NewScene("ED6_DT21/C4113   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_358B")

    NewScene("ED6_DT21/T4302   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_3597")

    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35A3")

    NewScene("ED6_DT21/T4312   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35AF")

    NewScene("ED6_DT21/T4313   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35BB")

    NewScene("ED6_DT21/T4150   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35C7")

    NewScene("ED6_DT21/T4151   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35D3")

    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35DF")

    NewScene("ED6_DT21/T4153   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35EB")

    NewScene("ED6_DT21/T4156   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_35F7")

    NewScene("ED6_DT21/T4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_3603")

    NewScene("ED6_DT21/T4250   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_360F")

    NewScene("ED6_DT21/T4403   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_3621")

    label("loc_361B")

    OP_5F(0x3)
    Jump("loc_3621")

    label("loc_3621")

    Jump("loc_3631")

    label("loc_3624")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3631")

    label("loc_3631")

    Jump("loc_2DBA")

    label("loc_3634")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_2DB0 end

    def Function_12_3644(): pass

    label("Function_12_3644")


    AnonymousTalk(    #34
        "\x06Where?\x02",
    )


    label("loc_364E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46B2")

    Menu(
        2,
        10,
        100,
        1,
        (
            "Le Locle\x01",             # 0
            "Laboratory\x01",           # 1
            "Aureole\x01",              # 2
            "Hamel Village\x01",        # 3
            "Glorious Inside\x01",      # 4
            "Cancel\x01",               # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_36C5"),
        (1, "loc_37C5"),
        (2, "loc_39CE"),
        (3, "loc_4298"),
        (4, "loc_4305"),
        (SWITCH_DEFAULT, "loc_46A2"),
    )


    label("loc_36C5")


    AnonymousTalk(    #35
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T5100 Le-Locle Outside Perspective\x01",              # 0
            "C5503 Balstar Channel\x01",                           # 1
            "C5504 Saint-Croix Forest\x01",                        # 2
            "C5508 Grimsel Fort\x01",                              # 3
            "T5101 Le-Locle Outside Perspective (Night)\x01",      # 4
            "Cancel\x01",                                          # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_378F"),
        (1, "loc_3798"),
        (2, "loc_37A1"),
        (3, "loc_37AA"),
        (4, "loc_37B3"),
        (SWITCH_DEFAULT, "loc_37BC"),
    )


    label("loc_378F")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3798")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_37A1")

    NewScene("ED6_DT21/C5504   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_37AA")

    NewScene("ED6_DT21/C5508   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_37B3")

    NewScene("ED6_DT21/T5101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_37BC")

    OP_5F(0x3)
    Jump("loc_37C2")

    label("loc_37C2")

    Jump("loc_46AF")

    label("loc_37C5")


    AnonymousTalk(    #36
        (
            "\x06Where? Rooms will connect to night map. This is because\x01",
            "invasion event happens at night. Use for events during day.\x02",
        )
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5600 Laboratory Outside Perspective (Entrance)\x01",              # 0
            "C5601 Laboratory Outside Perspective (Entrance) (Night)\x01",      # 1
            "C5610 Laboratory Inside (Floor 1)\x01",                            # 2
            "C5611 Laboratory Inside (Floor 1)\x01",                            # 3
            "C5612 Laboratory Inside (Floor 1)\x01",                            # 4
            "C5613 Laboratory Inside (Floor 1)\x01",                            # 5
            "C5610 Laboratory Inside, Elevator\x01",                            # 6
            "Cancel\x01",                                                       # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3986"),
        (1, "loc_398F"),
        (2, "loc_3998"),
        (3, "loc_39A1"),
        (4, "loc_39AA"),
        (5, "loc_39B3"),
        (6, "loc_39BC"),
        (SWITCH_DEFAULT, "loc_39C5"),
    )


    label("loc_3986")

    NewScene("ED6_DT21/C5600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_398F")

    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3998")

    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39A1")

    NewScene("ED6_DT21/C5611   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39AA")

    NewScene("ED6_DT21/C5612   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39B3")

    NewScene("ED6_DT21/C5613   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39BC")

    NewScene("ED6_DT21/C5614   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_39C5")

    OP_5F(0x3)
    Jump("loc_39CB")

    label("loc_39CB")

    Jump("loc_46AF")

    label("loc_39CE")


    AnonymousTalk(    #37
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5100 Passage Before Axis Pillar\x01",              # 0
            "C5101 Axis Pillar Entrance\x01",                    # 1
            "C5700 Industrial Block (Factoria)\x01",             # 2
            "C5800 Residential Block (Cradle)\x01",              # 3
            "C5900 Park Block (Calmare)\x01",                    # 4
            "----- Aureole Inside (Tunnels, Stations)\x01",      # 5
            "----- Central Axis Pillar Inside\x01",              # 6
            "----- Stations\x01",                                # 7
            "Cancel\x01",                                        # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B07"),
        (1, "loc_3B10"),
        (2, "loc_3B19"),
        (3, "loc_3B22"),
        (4, "loc_3B2B"),
        (5, "loc_3B34"),
        (6, "loc_3DD2"),
        (7, "loc_418E"),
        (SWITCH_DEFAULT, "loc_428F"),
    )


    label("loc_3B07")

    NewScene("ED6_DT21/C5100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B10")

    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B19")

    NewScene("ED6_DT21/C5700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B22")

    NewScene("ED6_DT21/C5800   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B2B")

    NewScene("ED6_DT21/C5900   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3B34")


    AnonymousTalk(    #38
        "\x06Where?\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "C5200 Tunnel (Park~Residential Block 1)\x01",                    # 0
            "C5201 Tunnel (Park~Residential Block 2)\x01",                    # 1
            "C5202 Tunnel (Residential Block~Construction Block 1)\x01",      # 2
            "C5203 Tunnel (Residential Block~Construction Block 2)\x01",      # 3
            "C5204 Tunnel (Industrial Block~Axis Pillar 1)\x01",              # 4
            "C5205 Tunnel (Industrial Block~Axis Pillar 2)\x01",              # 5
            "C5206 Tunnel (Axis Pillar~Park Block 1)\x01",                    # 6
            "C5207 Tunnel (Axis Pillar~Park Block 2)\x01",                    # 7
            "C6000 West Calmare Station\x01",                                 # 8
            "C6001 Cradle Station #35\x01",                                   # 9
            "C6002 Factoria Station #7\x01",                                  # 10
            "C6003 Axis Pillar Station\x01",                                  # 11
            "Cancel\x01",                                                     # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D5A"),
        (1, "loc_3D63"),
        (2, "loc_3D6C"),
        (3, "loc_3D75"),
        (4, "loc_3D7E"),
        (5, "loc_3D87"),
        (6, "loc_3D90"),
        (7, "loc_3D99"),
        (8, "loc_3DA2"),
        (9, "loc_3DAB"),
        (10, "loc_3DB4"),
        (11, "loc_3DBD"),
        (SWITCH_DEFAULT, "loc_3DC6"),
    )


    label("loc_3D5A")

    NewScene("ED6_DT21/C5200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D63")

    NewScene("ED6_DT21/C5201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D6C")

    NewScene("ED6_DT21/C5202   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D75")

    NewScene("ED6_DT21/C5203   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D7E")

    NewScene("ED6_DT21/C5204   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D87")

    NewScene("ED6_DT21/C5205   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D90")

    NewScene("ED6_DT21/C5206   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3D99")

    NewScene("ED6_DT21/C5207   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DA2")

    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DAB")

    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DB4")

    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DBD")

    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_3DC6")

    OP_5F(0x4)
    Jump("loc_3DCC")

    label("loc_3DCC")

    OP_5F(0x3)
    Jump("loc_4295")

    label("loc_3DD2")


    AnonymousTalk(    #39
        "\x06Where inside the Axis Pillar?\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "C5300 Central Axis Pillar Inside 0\x01",             # 0
            "C5301 Central Axis Pillar Inside 1\x01",             # 1
            "C5302 Central Axis Pillar Inside 2\x01",             # 2
            "C5303 Central Axis Pillar Inside 3\x01",             # 3
            "C5304 Central Axis Pillar Inside 4\x01",             # 4
            "C5305 Central Axis Pillar Inside 5\x01",             # 5
            "C5306 Central Axis Pillar Inside 6\x01",             # 6
            "C5307 Central Axis Pillar Inside 7\x01",             # 7
            "C5308 Midboss Map 1 (Bleublanc)\x01",                # 8
            "C5309 Midboss Map 2 (Walter)\x01",                   # 9
            "C5310 Midboss Map 3 (Lucciola)\x01",                 # 10
            "C5311 Midboss Map 4 (Renne)\x01",                    # 11
            "C5312 Shaft Inside Where Road Ends\x01",             # 12
            "C5313 Pinnacle\x01",                                 # 13
            "C5314 Bottom, Before Boss Room, Boss Room\x01",      # 14
            "C5315 High-Speed Elevator\x01",                      # 15
            "C5316 Small Elevator\x01",                           # 16
            "C5317 Boss Room\x01",                                # 17
            "C5318 Boss Battle Map Event Purposed\x01",           # 18
            "C5319 Passage before Boss Room\x01",                 # 19
            "Cancel\x01",                                         # 20
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40CE"),
        (1, "loc_40D7"),
        (2, "loc_40E0"),
        (3, "loc_40E9"),
        (4, "loc_40F2"),
        (5, "loc_40FB"),
        (6, "loc_4104"),
        (7, "loc_410D"),
        (8, "loc_4116"),
        (9, "loc_411F"),
        (10, "loc_4128"),
        (11, "loc_4131"),
        (12, "loc_413A"),
        (13, "loc_4143"),
        (14, "loc_414C"),
        (15, "loc_4155"),
        (16, "loc_415E"),
        (17, "loc_4167"),
        (18, "loc_4170"),
        (19, "loc_4179"),
        (SWITCH_DEFAULT, "loc_4182"),
    )


    label("loc_40CE")

    NewScene("ED6_DT21/C5300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_40D7")

    NewScene("ED6_DT21/C5301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_40E0")

    NewScene("ED6_DT21/C5302   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_40E9")

    NewScene("ED6_DT21/C5303   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_40F2")

    NewScene("ED6_DT21/C5304   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_40FB")

    NewScene("ED6_DT21/C5305   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4104")

    NewScene("ED6_DT21/C5306   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_410D")

    NewScene("ED6_DT21/C5307   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4116")

    NewScene("ED6_DT21/C5308   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_411F")

    NewScene("ED6_DT21/C5309   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4128")

    NewScene("ED6_DT21/C5310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4131")

    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_413A")

    NewScene("ED6_DT21/C5312   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4143")

    NewScene("ED6_DT21/C5313   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_414C")

    NewScene("ED6_DT21/C5314   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4155")

    NewScene("ED6_DT21/C5315   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_415E")

    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4167")

    NewScene("ED6_DT21/C5317   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4170")

    NewScene("ED6_DT21/C5318   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4179")

    NewScene("ED6_DT21/C5319   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4182")

    OP_5F(0x4)
    Jump("loc_4188")

    label("loc_4188")

    OP_5F(0x3)
    Jump("loc_4295")

    label("loc_418E")


    AnonymousTalk(    #40
        "\x06Which station?\x02",
    )


    Menu(
        4,
        10,
        100,
        1,
        (
            "C6000 West Calmare Station\x01",         # 0
            "C6001 Cradle Station #35\x01",           # 1
            "C6002 Factoria Station #7\x01",          # 2
            "C6003 Axis Pillar Station\x01",          # 3
            "C6010 In Transit on Halo Rail\x01",      # 4
            "Cancel\x01",                             # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4256"),
        (1, "loc_425F"),
        (2, "loc_4268"),
        (3, "loc_4271"),
        (4, "loc_427A"),
        (SWITCH_DEFAULT, "loc_4283"),
    )


    label("loc_4256")

    NewScene("ED6_DT21/C6000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_425F")

    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4268")

    NewScene("ED6_DT21/C6002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4271")

    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_427A")

    NewScene("ED6_DT21/C6010   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4283")

    OP_5F(0x4)
    Jump("loc_4289")

    label("loc_4289")

    OP_5F(0x3)
    Jump("loc_4295")

    label("loc_428F")

    OP_5F(0x3)
    Jump("loc_4295")

    label("loc_4295")

    Jump("loc_46AF")

    label("loc_4298")


    AnonymousTalk(    #41
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "Hamel\x01",                              # 0
            "Hamel (Before Monument Stone)\x01",      # 1
            "Cancel\x01",                             # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42EA"),
        (1, "loc_42F3"),
        (SWITCH_DEFAULT, "loc_42FC"),
    )


    label("loc_42EA")

    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_42F3")

    NewScene("ED6_DT21/T5201   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_42FC")

    OP_5F(0x3)
    Jump("loc_4302")

    label("loc_4302")

    Jump("loc_46AF")

    label("loc_4305")


    AnonymousTalk(    #42
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C5400 Glorious Inside (Room Estelle is held in)\x01",                  # 0
            "C5401 Glorious Inside (Weissman's Space)\x01",                         # 1
            "C5402 Glorious Inside (Passage toward deck)\x01",                      # 2
            "C5403 Glorious Inside (Deck~Passage to Hatch)\x01",                    # 3
            "C5404 Glorious Inside (Hatch~Passage to Hangar)\x01",                  # 4
            "C5405 Glorious Inside (Hangar Wrong)\x01",                             # 5
            "C5406 Glorious Inside (Hangar Right)\x01",                             # 6
            "C5407 Glorious Inside (Elevator Box)\x01",                             # 7
            "C5408 Glorious Outside (Deck)\x01",                                    # 8
            "C5409 Glorious Outside (Hatch)\x01",                                   # 9
            "C5410 Glorious Inside (Hatch~Passage to Hangar Entry Added)\x01",      # 10
            "C5411 Glorious Inside (Hangar Entrance)\x01",                          # 11
            "C5412 Glorious Inside (Hangar Wrong)\x01",                             # 12
            "C5413 Glorious Outside (Hatch Night)\x01",                             # 13
            "C5414 Glorious Outside (Outer Equipment W Windows)\x01",               # 14
            "C5415 Glorious Inside (Latter Section, Hatch)\x01",                    # 15
            "Cancel\x01",                                                           # 16
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4609"),
        (1, "loc_4612"),
        (2, "loc_461B"),
        (3, "loc_4624"),
        (4, "loc_462D"),
        (5, "loc_4636"),
        (6, "loc_463F"),
        (7, "loc_4648"),
        (8, "loc_4651"),
        (9, "loc_465A"),
        (10, "loc_4663"),
        (11, "loc_466C"),
        (12, "loc_4675"),
        (13, "loc_467E"),
        (14, "loc_4687"),
        (15, "loc_4690"),
        (SWITCH_DEFAULT, "loc_4699"),
    )


    label("loc_4609")

    NewScene("ED6_DT21/C5400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4612")

    NewScene("ED6_DT21/C5401   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_461B")

    NewScene("ED6_DT21/C5402   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4624")

    NewScene("ED6_DT21/C5403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_462D")

    NewScene("ED6_DT21/C5404   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4636")

    NewScene("ED6_DT21/C5405   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_463F")

    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_4648")

    NewScene("ED6_DT21/C5407   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4651")

    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_465A")

    NewScene("ED6_DT21/C5409   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4663")

    NewScene("ED6_DT21/C5410   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_466C")

    NewScene("ED6_DT21/C5411   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4675")

    NewScene("ED6_DT21/C5412   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_467E")

    NewScene("ED6_DT21/C5413   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4687")

    NewScene("ED6_DT21/C5414   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4690")

    NewScene("ED6_DT21/C5415   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4699")

    OP_5F(0x3)
    Jump("loc_469F")

    label("loc_469F")

    Jump("loc_46AF")

    label("loc_46A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46AF")

    label("loc_46AF")

    Jump("loc_364E")

    label("loc_46B2")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_3644 end

    def Function_13_46C2(): pass

    label("Function_13_46C2")


    AnonymousTalk(    #43
        "\x06Where?\x02",
    )


    label("loc_46CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BDD")

    Menu(
        2,
        10,
        100,
        1,
        (
            "Various Ships\x01",                   # 0
            "Arseille\x01",                        # 1
            "For In-Air/On-Water Events\x01",      # 2
            "Cancel\x01",                          # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4733"),
        (1, "loc_4909"),
        (2, "loc_4A88"),
        (SWITCH_DEFAULT, "loc_4BCD"),
    )


    label("loc_4733")


    AnonymousTalk(    #44
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0000 Liner Linde\x01",                     # 0
            "E0001 Liner Cecilia (Green)\x01",           # 1
            "E0002 Ship Workshop\x01",                   # 2
            "E0100 Airborne Ship\x01",                   # 3
            "E0101 Airborne Ship (Night)\x01",           # 4
            "E0111 Airborne Ship Mechanisms\x01",        # 5
            "E0200 Military Ship\x01",                   # 6
            "E0400 Special Forces Ship\x01",             # 7
            "E0600 Red Airborne Ship\x01",               # 8
            "E0610 Red Airborne Ship Interior\x01",      # 9
            "E0700 International Liner Greta\x01",       # 10
            "Cancel\x01",                                # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_489D"),
        (1, "loc_48A6"),
        (2, "loc_48AF"),
        (3, "loc_48B8"),
        (4, "loc_48C1"),
        (5, "loc_48CA"),
        (6, "loc_48D3"),
        (7, "loc_48DC"),
        (8, "loc_48E5"),
        (9, "loc_48EE"),
        (10, "loc_48F7"),
        (SWITCH_DEFAULT, "loc_4900"),
    )


    label("loc_489D")

    NewScene("ED6_DT21/E0000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48A6")

    NewScene("ED6_DT21/E0001   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48AF")

    NewScene("ED6_DT21/E0002   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48B8")

    NewScene("ED6_DT21/E0100   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48C1")

    NewScene("ED6_DT21/E0101   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48CA")

    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48D3")

    NewScene("ED6_DT21/E0200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48DC")

    NewScene("ED6_DT21/E0400   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48E5")

    NewScene("ED6_DT21/E0600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48EE")

    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_48F7")

    NewScene("ED6_DT21/E0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4900")

    OP_5F(0x3)
    Jump("loc_4906")

    label("loc_4906")

    Jump("loc_4BDA")

    label("loc_4909")


    AnonymousTalk(    #45
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "E0300 Arseille Outside Perspective Test\x01",                                      # 0
            "E0301 Arseille Outside Perspective On Cloud, Panorama (Change with OPS)\x01",      # 1
            "E0310 Arseille Connecting Passage/Bridge\x01",                                     # 2
            "E0311 Arseille Passage 1/Meeting Room/Lounge\x01",                                 # 3
            "E0312 Arseille Passage 2/Workshop/Cabin\x01",                                      # 4
            "E0313 Arseille Hold\x01",                                                          # 5
            "Cancel\x01",                                                                       # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4A49"),
        (1, "loc_4A52"),
        (2, "loc_4A5B"),
        (3, "loc_4A64"),
        (4, "loc_4A6D"),
        (5, "loc_4A76"),
        (SWITCH_DEFAULT, "loc_4A7F"),
    )


    label("loc_4A49")

    NewScene("ED6_DT21/E0300   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A52")

    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A5B")

    NewScene("ED6_DT21/E0310   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A64")

    NewScene("ED6_DT21/E0311   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A6D")

    NewScene("ED6_DT21/E0312   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A76")

    NewScene("ED6_DT21/E0313   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4A7F")

    OP_5F(0x3)
    Jump("loc_4A85")

    label("loc_4A85")

    Jump("loc_4BDA")

    label("loc_4A88")


    AnonymousTalk(    #46
        "\x06Where?\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "      Skybox Test\x01",                      # 0
            "E0800 Sky: Dragon + Army Airships\x01",      # 1
            "E0810 Sky: Dragon + Army Airships\x01",      # 2
            "E0811 Sky: Night\x01",                       # 3
            "E0900 Water: Dragon + Arseille\x01",         # 4
            "E0901 Water: Night Boat\x01",                # 5
            "E1000 For Mental Space Event\x01",           # 6
            "Cancel\x01",                                 # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B85"),
        (1, "loc_4B8E"),
        (2, "loc_4B97"),
        (3, "loc_4BA0"),
        (4, "loc_4BA9"),
        (5, "loc_4BB2"),
        (6, "loc_4BBB"),
        (SWITCH_DEFAULT, "loc_4BC4"),
    )


    label("loc_4B85")

    NewScene("ED6_DT21/E0500   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4B8E")

    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4B97")

    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4BA0")

    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4BA9")

    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4BB2")

    NewScene("ED6_DT21/E0901   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4BBB")

    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_4BC4")

    OP_5F(0x3)
    Jump("loc_4BCA")

    label("loc_4BCA")

    Jump("loc_4BDA")

    label("loc_4BCD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4BDA")

    label("loc_4BDA")

    Jump("loc_46CC")

    label("loc_4BDD")

    OP_5F(0x2)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_46C2 end

    def Function_14_4BED(): pass

    label("Function_14_4BED")

    EventBegin(0x0)
    OP_DA()
    OP_56(0x0)
    OP_5F(0x0)
    OP_5F(0x1)

    AnonymousTalk(    #47
        "\x06Which one?\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E98")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        10,
        100,
        1,
        (
            "Opening\x01",                              # 0
            "Glorious Arrives\x01",                     # 1
            "Aureole Appears\x01",                      # 2
            "Orbal Shutdown Phenomenon [PSP]\x01",      # 3
            "Glorious Attacks\x01",                     # 4
            "Aureole Airspace\x01",                     # 5
            "Arseille Dive\x01",                        # 6
            "Aureole Collapse\x01",                     # 7
            "Ending\x01",                               # 8
            "Weissmann Transforms [PSP]\x01",           # 9
            "Weissmann's Regrets [PSP]\x01",            # 10
            "Cancel\x01",                               # 11
        )
    )

    MenuEnd(0x0)
    OP_5F(0x2)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D27")
    Jump("loc_4E98")

    label("loc_4D27")

    FadeToDark(2000, 0, -1)
    OP_20(0x3E8)
    OP_0D()
    OP_21()
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D71"),
        (1, "loc_4D87"),
        (2, "loc_4D9D"),
        (4, "loc_4DF0"),
        (5, "loc_4E06"),
        (6, "loc_4E1C"),
        (7, "loc_4E32"),
        (8, "loc_4E48"),
        (SWITCH_DEFAULT, "loc_4E5E"),
    )


    label("loc_4D71")

    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Jump("loc_4E61")

    label("loc_4D87")

    PlayMovie(0x0, "ED6_DT40.dat", 0x1C, 0x1)
    Jump("loc_4E61")

    label("loc_4D9D")

    PlayMovie(0x0, "ED6_DT41.dat", 0x82, 0x1)
    Sleep(1000)
    OP_56(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DDA")
    FadeToDark(2000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToBright(1, 0)
    OP_0D()

    label("loc_4DDA")

    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x1)
    Jump("loc_4E61")

    label("loc_4DF0")

    PlayMovie(0x0, "ED6_DT43.dat", 0x77, 0x1)
    Jump("loc_4E61")

    label("loc_4E06")

    PlayMovie(0x0, "ED6_DT44.dat", 0x83, 0x1)
    Jump("loc_4E61")

    label("loc_4E1C")

    PlayMovie(0x0, "ED6_DT45.dat", 0x84, 0x1)
    Jump("loc_4E61")

    label("loc_4E32")

    PlayMovie(0x0, "ED6_DT46.dat", 0x85, 0x1)
    Jump("loc_4E61")

    label("loc_4E48")

    PlayMovie(0x0, "ED6_DT47.dat", 0x8, 0x0)
    Jump("loc_4E61")

    label("loc_4E5E")

    Jump("loc_4E61")

    label("loc_4E61")

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
    Jump("loc_4C10")

    label("loc_4E98")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_4BED end

    SaveToFile()

Try(main)
