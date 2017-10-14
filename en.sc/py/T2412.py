from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2412   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2412.x',
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
        'Matron Theresa',                       # 9
        'Pot',                                  # 10
        'Tea',                                  # 11
        'Tea',                                  # 12
        'Tea',                                  # 13
        'Clem',                                 # 14
        'Polly',                                # 15
        'Mary',                                 # 16
        'Daniel',                               # 17
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02573 ._CH',             # 01
        'ED6_DT27/CH03003 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT07/CH00053 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH02590 ._CH',             # 06
        'ED6_DT07/CH02500 ._CH',             # 07
        'ED6_DT07/CH02630 ._CH',             # 08
        'ED6_DT07/CH02640 ._CH',             # 09
        'ED6_DT27/CH03083 ._CH',             # 0A
        'ED6_DT07/CH02593 ._CH',             # 0B
        'ED6_DT07/CH02503 ._CH',             # 0C
        'ED6_DT07/CH02633 ._CH',             # 0D
        'ED6_DT07/CH02643 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02573P._CP',             # 01
        'ED6_DT27/CH03003P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT07/CH00053P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH02590P._CP',             # 06
        'ED6_DT07/CH02500P._CP',             # 07
        'ED6_DT07/CH02630P._CP',             # 08
        'ED6_DT07/CH02640P._CP',             # 09
        'ED6_DT27/CH03083P._CP',             # 0A
        'ED6_DT07/CH02593P._CP',             # 0B
        'ED6_DT07/CH02503P._CP',             # 0C
        'ED6_DT07/CH02633P._CP',             # 0D
        'ED6_DT07/CH02643P._CP',             # 0E
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_295",          # 01, 1
        "Function_2_2A8",          # 02, 2
        "Function_3_2BE",          # 03, 3
        "Function_4_2E2",          # 04, 4
        "Function_5_EFD",          # 05, 5
        "Function_6_12EC",         # 06, 6
        "Function_7_1CB2",         # 07, 7
        "Function_8_2FE9",         # 08, 8
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_269")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 4200, 0)
    OP_43(0x10, 0x0, 0x0, 0x3)
    Jump("loc_275")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_275")
    SetChrFlags(0x8, 0x80)

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_283")
    OP_A3(0x10F0)
    Event(0, 7)

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_294")

    Return()

    # Function_0_242 end

    def Function_1_295(): pass

    label("Function_1_295")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_A3(0x0)
    OP_A3(0x1)

    label("loc_2A7")

    Return()

    # Function_1_295 end

    def Function_2_2A8(): pass

    label("Function_2_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2A8")

    label("loc_2BD")

    Return()

    # Function_2_2A8 end

    def Function_3_2BE(): pass

    label("Function_3_2BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1")
    OP_8D(0xFE, -1720, 8440, 1470, 870, 2000)
    Jump("Function_3_2BE")

    label("loc_2E1")

    Return()

    # Function_3_2BE end

    def Function_4_2E2(): pass

    label("Function_4_2E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2590, 0, 15070, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x102, -4040, 0, 13240, 0)
    SetChrPos(0x101, -3050, 0, 13440, 0)
    SetChrPos(0xF8, -3980, 0, 12140, 0)
    SetChrPos(0xF9, -2940, 0, 12340, 0)
    OP_8C(0xFE, 180, 0)
    OP_4A(0xFE, 255)
    OP_0D()

    ChrTalk(    #0
        0x8,
        (
            "#750F#6PEstelle, and...and Joshua.\x02\x03",

            "#751FWelcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1035F#6PMatron Theresa...\x01",
            "I'm very sorry to have worried you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #2
        0x8,
        (
            "#750F#6PJoshua, please, stay with Estelle\x01",
            "from now on.\x02\x03",

            "#751FThat is all I would ask of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1054F#6P...I will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1017F#4PThank you, Matron Theresa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#751F#6PHeehee. I see now that there\x01",
            "was no need to worry.\x02\x03",

            "#750FI'm sure Kloe's very relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1004F#4PThat reminds me.\x02\x01",

            "#1015FMatron Theresa, about Kloe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#754F#6PYes, I hear she's in the capital.\x02\x03",

            "#750FSieg delivered a letter from her to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1016F#4PAhaha, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1049F#6PThat's Sieg for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#754F#6PBased on her letter, she's having\x01",
            "plenty of trouble on her side, too.\x02\x03",

            "From the content, I could feel a\x01",
            "very decisive will to face some kind\x01",
            "of problem directly.\x02\x03",

            "#750FI don't know what kind of decision\x01",
            "that represents, but...\x02\x03",

            "I'm confident that girl will find her\x01",
            "own path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1004F#4PAwww...\x02\x03",

            "#1006FYeah, I think so, too!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x20B1)
    EventEnd(0x0)
    OP_4B(0xFE, 255)
    Jump("loc_B5F")

    label("loc_759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_97C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_889")

    ChrTalk(    #12
        0x8,
        (
            "#757FBased on her letter, she's having\x01",
            "plenty of trouble on her side, too.\x02\x03",

            "#754FFrom the content, I could feel a\x01",
            "very decisive will to face some kind\x01",
            "of problem directly.\x02\x03",

            "#750FI don't know what kind of decision\x01",
            "that represents, but I'm confident that\x01",
            "girl will find her own path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_979")

    label("loc_889")


    ChrTalk(    #13
        0x8,
        (
            "#750FThe soldiers on the patrol ship who had\x01",
            "to make an emergency landing are going\x01",
            "to guard us for now.\x02\x03",

            "They seem very tired, so I was thinking of\x01",
            "offering them some herbal tea.\x02\x03",

            "#751FIf you'd like, Estelle, you're welcome to a cup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_979")

    Jump("loc_B5F")

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A4D")

    ChrTalk(    #14
        0x8,
        (
            "#757FBased on her letter, she's having\x01",
            "plenty of trouble on her side, too.\x02\x03",

            "#754FI don't know what kind of decision\x01",
            "that represents, but...\x02\x03",

            "#750FI'm confident that girl will find her\x01",
            "own path.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5F")

    label("loc_A4D")


    ChrTalk(    #15
        0x8,
        (
            "#754FWe evacuated to Manoria the other day\x01",
            "because of that monster trouble.\x02\x03",

            "#757FJust as I thought we'd gotten back home,\x01",
            "something like this happens...\x02\x03",

            "#750FStill, how curious.\x02\x03",

            "#751FJust seeing the children smile and laugh\x01",
            "makes me feel like we can get through it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B5F")

    Jump("loc_EF9")

    label("loc_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_B6C")
    Jump("loc_EF9")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C07")

    ChrTalk(    #16
        0xFE,
        (
            "#751FThe children have been eagerly\x01",
            "awaiting the end of exams.\x02\x03",

            "Once exams are over, Kloe will come\x01",
            "play with them again, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CCC")

    label("loc_C07")

    OP_A2(0x0)

    ChrTalk(    #17
        0x8,
        (
            "#750FThe exams at the academy will be\x01",
            "over soon, yes?\x02\x03",

            "The children are eagerly awaiting\x01",
            "Kloe's return.\x02\x03",

            "#751FShe's promised to come play with\x01",
            "them afterward, and they couldn't be\x01",
            "happier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCC")

    Jump("loc_EF9")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_DED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D42")

    ChrTalk(    #18
        0x8,
        (
            "#751FWhile you're in Ruan, come by\x01",
            "any time you'd like.\x02\x03",

            "The children would love to see you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEA")

    label("loc_D42")

    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "#750FI'm very sorry about today.\x02\x03",

            "Thank you for going out and\x01",
            "getting the children.\x02\x03",

            "#751FCome by again any time you like.\x01",
            "You know you're always welcome\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DEA")

    Jump("loc_EF9")

    label("loc_DED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 6)), scpexpr(EXPR_END)), "loc_EF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E7A")

    ChrTalk(    #20
        0x8,
        (
            "#750FManoria Village is out west along\x01",
            "the Gull Seaside Way, as I'm sure\x01",
            "you know.\x02\x03",

            "Please, take care of the children.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EF9")

    label("loc_E7A")

    OP_A2(0x0)

    ChrTalk(    #21
        0x8,
        (
            "#750FSunday School over at Manoria Village\x01",
            "should be finished soon.\x02\x03",

            "I'm sorry, but could you bring back\x01",
            "the children?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF9")

    TalkEnd(0xFE)
    Return()

    # Function_4_2E2 end

    def Function_5_EFD(): pass

    label("Function_5_EFD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_103D")
    TurnDirection(0xFE, 0x102, 0)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #22
        0xFE,
        "#1723FWha...? It's Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040FHi, Daniel. It's been a while.\x02\x03",

            "Have you been a good boy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "#1721FYeah!\x02\x03",

            "#1720FI decided to help Matron Theresa,\x01",
            "just like Clem!\x02\x03",

            "Today, I watered the plants!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#1049FI see. Good job, Daniel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#1721FHeeheehee.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x20ED)
    Jump("loc_12E8")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10B0")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #27
        0xFE,
        (
            "#1720FI decided to help Matron Theresa,\x01",
            "just like Clem!\x02\x03",

            "Today, I watered the plants!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121E")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11AF")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #28
        0xFE,
        "#1720FHey, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1011FHm? Yeees?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#1720FCan you make me an apple pie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1015FUmm... Well.\x02\x03",

            "#1007FS-Sorry. I don't think I can...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "#1723FAww, okay, then.\x02\x03",

            "#1720FI'll just have to ask Kloe when she\x01",
            "comes, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_121E")

    label("loc_11AF")


    ChrTalk(    #33
        0xFE,
        (
            "#1720FWhen Kloe comes, I'm gonna ask\x01",
            "her to bake an apple pie.\x02\x03",

            "#1721FThe ones she makes are the bestest!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121E")

    Jump("loc_12E8")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_128D")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #34
        0xFE,
        (
            "#1720FI decided to help Matron Theresa,\x01",
            "just like Clem!\x02\x03",

            "Today, I watered the plants!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E8")

    label("loc_128D")


    ChrTalk(    #35
        0xFE,
        (
            "#1720FIt gets reeeally dark at night.\x02\x03",

            "The stars are pretty, but it's a little scary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E8")

    TalkEnd(0x10)
    Return()

    # Function_5_EFD end

    def Function_6_12EC(): pass

    label("Function_6_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FD")
    Call(0, 8)

    label("loc_12FD")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x8, 1)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_132B")
    SetChrChipByIndex(0x103, 3)
    Jump("loc_1330")

    label("loc_132B")

    SetChrChipByIndex(0x106, 4)

    label("loc_1330")

    SetChrPos(0x101, -5240, 200, 7350, 90)
    SetChrPos(0xF7, -5240, 200, 6050, 90)
    SetChrPos(0x8, -2550, 200, 7350, 270)
    SetChrPos(0x9, -3710, 700, 6060, 0)
    SetChrPos(0xA, -4550, 700, 6860, 0)
    SetChrPos(0xB, -4530, 700, 6060, 0)
    SetChrPos(0xC, -3810, 700, 6860, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(-3770, 100, 7530, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #36
        0x101,
        (
            "#1007F#6P*sigh*...\x01",
            "Well, that was embarrassing.\x02\x03",

            "And here I was wanting to show up and show\x01",
            "how I'm a big, tough bracer woman now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#751FThat's right. You are a\x01",
            "senior bracer now, aren't you?\x02\x03",

            "Congratulations, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1016F#6PAhaha, um, well... I'm still\x01",
            "kinda green, to be honest.\x02\x03",

            "#1026FSpeaking of my little crying jag, though...\x02\x03",

            "Theresa, you mentioned that\x01",
            "Kloe was worried about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#750FYes, about you and Joshua specifically.\x02\x03",

            "#754FShe saw her precious friends suffering\x01",
            "and felt powerless to do anything for\x01",
            "them...\x02\x03",

            "She's struggled with it.\x01",
            "She desperately wants to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1004F#6PPrecious friends...\x02\x03",

            "#1008FHaha... I feel kind of awful she's been\x01",
            "tearing herself up so much over it,\x01",
            "but I'm glad she cares...\x02\x03",

            "I really need to go see her soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#750FI believe the Jenis campus is closed to\x01",
            "visitors right now due to the end-of-term\x01",
            "examinations.\x02\x03",

            "Those should be over soon, though,\x01",
            "and you can see her then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1017F#6PSounds like a plan!\x02\x03",

            "Also...y'know, the kids are a\x01",
            "little bit late, aren't they?\x02\x03",

            "I don't remember Sunday School\x01",
            "taking this long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#750FThey may be playing in the\x01",
            "village after class.\x02\x03",

            "The new traveling priest who's been coming\x01",
            "by does seem like he's fond of children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1015F#6PA new traveling priest, huh?\x01",
            "(Wait, why does that sound familiar?)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF7, 1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19AD")

    ChrTalk(    #45
        0x106,
        (
            "#051F#2PWe should head over to Manoria\x01",
            "to check on 'em, then.\x02\x03",

            "We'll bring the kids back,\x01",
            "if need be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A1A")

    label("loc_19AD")


    ChrTalk(    #46
        0x103,
        (
            "#020F#2PLet's head to Manoria to see \x01",
            "if they're all right, then.\x02\x03",

            "We'll bring them home if\x01",
            "we need to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1A")

    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #47
        0x101,
        "#1006F#3PGood idea!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#753FAre you sure?\x01",
            "I wouldn't want to trouble you...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #49
        0x101,
        (
            "#1001F#6PHaha! No problem!\x02\x03",

            "Think of it as thanks for\x01",
            "the great tea and snacks!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B31")

    ChrTalk(    #50
        0x106,
        (
            "#051F#2P'Sides, you owe her a big one for\x01",
            "letting you cry like that, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B6F")

    label("loc_1B31")


    ChrTalk(    #51
        0x103,
        (
            "#021F#2PYou also owe her for that big\x01",
            "hug back there. ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6F")

    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #52
        0x101,
        "#1013F#3PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#751FHaha...\x02\x03",

            "#750FThank you so much.\x01",
            "I'll be waiting here for your return.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x101, -3650, 0, 8410, 90)
    SetChrPos(0xF7, -3650, 0, 8410, 90)
    SetChrPos(0x8, -3700, 0, 14600, 0)
    OP_6D(-3650, 0, 8410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_4B(0x8, 255)
    OP_A2(0x1216)
    OP_28(0x82, 0x2, 0x80)
    OP_28(0x82, 0x1, 0x100)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_12EC end

    def Function_7_1CB2(): pass

    label("Function_7_1CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC3")
    Call(0, 8)

    label("loc_1CC3")

    EventBegin(0x0)
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0xD, 11)
    SetChrChipByIndex(0xE, 12)
    SetChrChipByIndex(0xF, 13)
    SetChrChipByIndex(0x10, 14)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF7, -5240, 200, 4750, 90)
    SetChrPos(0x10, -2550, 200, 4750, 0)
    SetChrPos(0x109, -3850, 200, 3900, 12)
    SetChrPos(0x8, -3930, 200, 8250, 180)
    SetChrPos(0xF, -5240, 200, 7350, 90)
    SetChrPos(0x101, -5240, 200, 6050, 90)
    SetChrPos(0xD, -2550, 200, 7350, 270)
    SetChrPos(0xE, -2550, 200, 6050, 270)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 2)
    SetChrChipByIndex(0x109, 10)
    SetChrChipByIndex(0x8, 1)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1E02")
    SetChrChipByIndex(0x103, 3)
    Jump("loc_1E07")

    label("loc_1E02")

    SetChrChipByIndex(0x106, 4)

    label("loc_1E07")

    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #54
        0x8,
        (
            "#750FAh, I see...\x02\x03",

            "So you've met Father Kevin before, Estelle?\x02\x03",

            "#751FThe world really is a small place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x109,
        (
            "#1061F#4PI know, right? Craziness!\x02\x03",

            "#1062FThanks for lunch, by the way!\x01",
            "It was excellent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#750FNo, no, it's no trouble. Besides,\x01",
            "it's the least I can do in return for\x01",
            "what you've done for the children.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #57
        0xD,
        (
            "#775FHey, Estelle.\x02\x03",

            "How come Joshua's not with you today?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #58
        0x101,
        (
            "#1025F#6PAh...you see...\x02\x03",

            "He's...pretty busy with something,\x01",
            "so he couldn't come today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x109,
        "#1067F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        "#1723FAww, too bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "#773FAwww! I wanted Joshua to see\x01",
            "the orphanage all fixed up, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xF,
        "#1716FMe too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        (
            "#1730F#4PI wanted to see him dressed up\x01",
            "like a princess again. So pretty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1016F#6PAh...haha...\x02\x03",

            "#1011FAnyway, you guys were in Sunday\x01",
            "School for a while.\x02\x03",

            "What was that you were reading when\x01",
            "we came in? Some kind of novel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "#770FHeheh! It's called 'The Doll Knight'!\x02\x03",

            "It's an awesome action story about\x01",
            "fights between puppeteers!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #66
        0xF,
        (
            "#1712FOooh, no it wasn't, swords-for-brains!\x02\x03",

            "#1718FIt was a romance! With desperate love\x01",
            "between a noble lady and a common man...\x01",
            "Mmmmmmm... Desperate love...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x109,
        (
            "#1068F#4PIt's a young adult novel series I brought\x01",
            "with me when I came to Liberl.\x02\x03",

            "I'd planned on reading it to the kids\x01",
            "a little at a time...but they, uh, convinced\x01",
            "me to do it all in one go. Hooo...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #68
        0x101,
        (
            "#1016F#6PHaha! I guess the way you get caught\x01",
            "up in stuff kinda backfired, there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#751FWell, thank you for your\x01",
            "devotion, Father Kevin.\x02\x03",

            "#750FYou'll be heading back to Ruan\x01",
            "now, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1062F#4PYeah, next logical stop, really.\x02\x03",

            "I've got other villages to visit, so\x01",
            "I need to hop an airship soon.\x02\x03",

            "#1060FSpeakin' of. How come you're in\x01",
            "Ruan yourself, Estelle?\x02\x03",

            "Bracer business, I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1006F#6PYeah, there's a lot going on.\x02\x03",

            "#1004FWait, on that note, we came out\x01",
            "here to ask about something...\x01",
            "um...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(300)

    ChrTalk(    #72
        0x8,
        (
            "#750FI believe you wanted to ask about\x01",
            "the 'white man' Polly saw.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #73
        0xD,
        "#770FOh, yeah, that thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        "#1733F#4PHmmmm? You wanna ask me stuff?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)

    ChrTalk(    #75
        0x101,
        (
            "#1011F#6PYes, Polly, we have a question...\x02\x03",

            "Can you tell us about the white\x01",
            "man you saw a little while ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xE,
        (
            "#1731F#4PThe white man was a white man.\x02\x03",

            "#1732FHe was spinning like a top\x01",
            "and was neato and fun!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x101,
        "#1016F#6PErm... We were hoping for a bit more...\x02",
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #78
        0xF,
        (
            "#1710FUm, let me try and explain a bit better...\x02\x03",

            "#1900FIt was about four days ago...\x02\x03",

            "Polly was outside, just kind of spacing\x01",
            "out...which is, y'know, usual for her...\x02\x03",

            "#1710FAnd then she saw a 'white\x01",
            "man' floating in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xE,
        (
            "#1730F#4PYeah!\x02\x03",

            "He was dancing around in\x01",
            "circles in the sky!\x02\x03",

            "And when I tried talking to him, he\x01",
            "bowed and flew away like a birdie!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #80
        0xD,
        (
            "#772FYou were totally asleep and\x01",
            "dreamed up the whole thing!\x02\x03",

            "I mean, c'mon, that is the\x01",
            "lamest ghost story ever!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#754FI thought she might be dreaming\x01",
            "at first, as well...but it seems\x01",
            "someone else saw it, too.\x02\x03",

            "#750FRight, Daniel?\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    ChrTalk(    #82
        0x10,
        (
            "#1720FUm, yeah. I only saw a little, though.\x02\x03",

            "That night, I saw a weird white\x01",
            "shadow flying off to the east.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1007F#6PWh-White shadow, oookay...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B86")

    ChrTalk(    #84
        0x106,
        (
            "#552F#6PWell, with two kids seeing it, I'm\x01",
            "a lot more inclined to believe it.\x02\x03",

            "#053FThe hell's up with just bowing\x01",
            "when spoken to, though...\x02\x03",

            "#051FHey, Polly? Did you get a good\x01",
            "look at his face?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C73")

    label("loc_2B86")


    ChrTalk(    #85
        0x103,
        (
            "#522F#6PWell, two witnesses makes this\x01",
            "quite a bit more believable.\x02\x03",

            "#026FBowing and leaving when addressed,\x01",
            "though... Curious...\x02\x03",

            "#020FPolly, I have one more question,\x01",
            "and it's important: do you remember\x01",
            "what his face looked like?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C73")


    ChrTalk(    #86
        0xE,
        (
            "#1733F#4PI dunno what his face looks like.\x02\x03",

            "#1730FHe was wearing a weird mask.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0x101,
        "#1004F#6PA mask?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D52")

    ChrTalk(    #88
        0x106,
        "#055F#6PWhat the hell kind of ghost wears a mask?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D8C")

    label("loc_2D52")


    ChrTalk(    #89
        0x103,
        "#023F#6PWell, that's...not your average ghost, then.\x02",
    )

    CloseMessageWindow()

    label("loc_2D8C")


    ChrTalk(    #90
        0xD,
        (
            "#775FHeeey, Pollyyy, you need to say this stuff!\x02\x03",

            "You never mentioned that before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xE,
        "#1733F#4PBut nobody asked.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #92
        0x8,
        (
            "#750FWell, masks aside, it seems\x01",
            "it wasn't just a dream...\x02\x03",

            "Once Daniel told me about it, I contacted\x01",
            "the Bracer Guild, just in case.\x02\x03",

            "We've been watching for it since then,\x01",
            "but there's been no sign of it.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #93
        0x101,
        "#1015F#6PHmmmm...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF7, 1)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F6A")

    ChrTalk(    #94
        0x106,
        (
            "#051F#6PWell, thanks for your time, ma'am.\x01",
            "This gives us a lot to think about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCC")

    label("loc_2F6A")


    ChrTalk(    #95
        0x103,
        (
            "#021F#6PWell, thank you for your time, Matron Theresa.\x01",
            "This has given us a lot to mull over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1CB2 end

    def Function_8_2FE9(): pass

    label("Function_8_2FE9")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3062"),
        (1, "loc_3068"),
        (SWITCH_DEFAULT, "loc_306E"),
    )


    label("loc_3062")

    OP_A2(0x1200)
    Jump("loc_306E")

    label("loc_3068")

    OP_A2(0x1201)
    Jump("loc_306E")

    label("loc_306E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_307C")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3080")

    label("loc_307C")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3080")

    Return()

    # Function_8_2FE9 end

    SaveToFile()

Try(main)
