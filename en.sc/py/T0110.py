from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0110   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0110.x',
        MapIndex            = 11,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0110_1 ._SN',
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
        'Luke',                                 # 9
        'Luke',                                 # 10
        'Maggy',                                # 11
        'Pat',                                  # 12
        'Rhett',                                # 13
        'Serra',                                # 14
        'CWO Ashton',                           # 15
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
        'ED6_DT07/CH01160 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01060 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01310 ._CH',             # 05
        'ED6_DT26/CH20330 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01160P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01060P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01310P._CP',             # 05
        'ED6_DT26/CH20330P._CP',             # 06
    )

    DeclNpc(
        X                   = 54480,
        Z                   = 0,
        Y                   = 163580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 55200,
        Z                   = 100,
        Y                   = 159950,
        Direction           = 180,
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
        X                   = 51750,
        Z                   = 0,
        Y                   = 163200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56170,
        Z                   = 0,
        Y                   = 161420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 93320,
        Z                   = 0,
        Y                   = 162900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 58080,
        Z                   = 0,
        Y                   = 198250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 49300,
        Z                   = 0,
        Y                   = 161100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 94990,
        TriggerZ            = 0,
        TriggerY            = 166570,
        TriggerRange        = 800,
        ActorX              = 95120,
        ActorZ              = 1400,
        ActorY              = 165990,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_2E1",          # 01, 1
        "Function_2_32B",          # 02, 2
        "Function_3_4A8",          # 03, 3
        "Function_4_1015",         # 04, 4
        "Function_5_12EF",         # 05, 5
        "Function_6_15DF",         # 06, 6
        "Function_7_23C5",         # 07, 7
        "Function_8_2C4A",         # 08, 8
        "Function_9_2C51",         # 09, 9
        "Function_10_2DF5",        # 0A, 10
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22D")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E")
    SetChrPos(0xB, 55510, 0, 163460, 270)
    Jump("loc_22A")

    label("loc_20E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219")
    Jump("loc_22A")

    label("loc_219")

    SetChrPos(0xB, 55510, 0, 163460, 270)

    label("loc_22A")

    Jump("loc_2D2")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_237")
    Jump("loc_2D2")

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_272")
    SetChrPos(0xA, 55120, 0, 161430, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 92380, 0, 161500, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x9, 4)
    Jump("loc_2D2")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, 55120, 0, 161430, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrSubChip(0x9, 4)
    Jump("loc_2D2")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrPos(0xD, 88100, 0, 162410, 270)
    Jump("loc_2D2")

    label("loc_2BC")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 49230, 0, 165600, 0)

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E0")
    OP_A3(0x10F0)
    Event(0, 9)

    label("loc_2E0")

    Return()

    # Function_0_1E6 end

    def Function_1_2E1(): pass

    label("Function_1_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_317")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2FC")
    OP_6F(0x2, 15)
    Jump("loc_317")

    label("loc_2FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_30D")
    OP_6F(0x2, 15)
    Jump("loc_317")

    label("loc_30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_317")
    Jump("loc_317")

    label("loc_317")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_32A")
    OP_65(0x0, 0x1)

    label("loc_32A")

    Return()

    # Function_1_2E1 end

    def Function_2_32B(): pass

    label("Function_2_32B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_350")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_492")

    label("loc_350")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_492")

    label("loc_369")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_382")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_492")

    label("loc_382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_492")

    label("loc_39B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_492")

    label("loc_3B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_492")

    label("loc_3CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_492")

    label("loc_3E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_492")

    label("loc_3FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_418")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_492")

    label("loc_418")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_492")

    label("loc_431")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_492")

    label("loc_44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_463")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_492")

    label("loc_463")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_492")

    label("loc_47C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_492")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_492")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_492")

    label("loc_4A7")

    Return()

    # Function_2_32B end

    def Function_3_4A8(): pass

    label("Function_3_4A8")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_521")

    ChrTalk(    #0
        0xFE,
        "Well, Luke is out quite late, isn't he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "How carefree that boy is, even in the\x01",
            "middle of all this!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1011")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_757")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69A")

    ChrTalk(    #2
        0xFE,
        (
            "This morning, my stove wouldn't turn on.\x01",
            "I thought it was broken!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I went to Melders' factory, and apparently\x01",
            "everyone's come down with a case of\x01",
            "the orbal troubles!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Mark my words, this is punishment from\x01",
            "Aidios for man's folly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "She's scolding us, telling us we've been\x01",
            "too focused on avoiding honest work with\x01",
            "machines. I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_754")

    label("loc_69A")


    ChrTalk(    #6
        0xFE,
        (
            "I'm sure this nonsense with the orbments\x01",
            "is punishment from Aidios.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "She's scolding us, telling us we've been\x01",
            "too focused on avoiding honest work with\x01",
            "machines. I'm sure of it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_754")

    Jump("loc_1011")

    label("loc_757")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7C2")

    ChrTalk(    #8
        0xFE,
        "I don't know anything about that dish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "You should ask someone else,\x01",
            "I'm afraid.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A60")

    label("loc_7C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7ED")
    Call(1, 0)
    Jump("loc_A60")

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F3")

    ChrTalk(    #10
        0xFE,
        "Luke woke up, at long last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Now I can watch him practice his\x01",
            "swordsmanship with my son again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "In light of all this, his 'unruliness'\x01",
            "was the most insignificant thing,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "As long as he's healthy and happy,\x01",
            "that's all I need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A60")

    label("loc_8F3")


    ChrTalk(    #14
        0xFE,
        "Oh, everyone, hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Luke woke up, at long last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "He's fit as a fiddle again.\x01",
            "In fact, he ran outside almost as soon\x01",
            "as he woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Really! Not realizing how sick with\x01",
            "worry his grandmother was for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Ah, well. It's hardly the time for\x01",
            "complaints!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I thank Aidios he woke up at all.\x01",
            "Simply having him healthy is more\x01",
            "than enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A60")

    Jump("loc_1011")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B56")

    ChrTalk(    #20
        0xFE,
        (
            "My son, Ashton, stopped by a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "After looking in on Luke for a moment,\x01",
            "he went right back out on his guard duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Isn't there someone who could take his\x01",
            "place for a while? For the sake of his son?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C77")

    label("loc_B56")


    ChrTalk(    #23
        0xFE,
        (
            "My son, Ashton, stopped by a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "After looking in on Luke for a moment,\x01",
            "he went right back out on his guard duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I know his duties are important,\x01",
            "but I can tell he's forcing himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "It's his son, after all...\x01",
            "I'm sure he's beside himself with worry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C77")

    Jump("loc_1011")

    label("loc_C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CEF")

    ChrTalk(    #27
        0xFE,
        (
            "Pat's here, Luke.\x01",
            "You can go out and play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "You usually leap out of bed on hearing\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE2")

    label("loc_CEF")

    SetChrName("Maggy")

    ChrTalk(    #29
        0xFE,
        "Luke...it's morning, come on, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Up with you, young man!\x01",
            "Are you going to leave an old woman in\x01",
            "the fog like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Pat's here, too...\x01",
            "You can go out and play like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Come, Luke...\x01",
            "wake up, now...\x01",
            "please...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DE2")

    Jump("loc_1011")

    label("loc_DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_FC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EB3")

    ChrTalk(    #33
        0xFE,
        (
            "I wonder, who HAS Luke taken after\x01",
            "to be so unruly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I'm sure it's hard on my son, Ashton,\x01",
            "who is trying to teach him swordsmanship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Yes, my grandson is a bit of a handful...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FBE")

    label("loc_EB3")


    ChrTalk(    #36
        0xFE,
        (
            "I wonder, who HAS Luke taken after\x01",
            "to be so unruly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "He ran out without even eating breakfast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "He's even started to learn to use a sword,\x01",
            "but he hasn't improved at all.\x01",
            "He's too impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "And to think, Ashton was such a calm\x01",
            "and steadfast boy.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FBE")

    Jump("loc_1011")

    label("loc_FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1011")

    ChrTalk(    #40
        0xFE,
        "Oh, no, where did Luke go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Really now. It's almost lunch, too!\x02",
    )

    CloseMessageWindow()

    label("loc_1011")

    TalkEnd(0xA)
    Return()

    # Function_3_4A8 end

    def Function_4_1015(): pass

    label("Function_4_1015")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_12EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 3)), scpexpr(EXPR_END)), "loc_10B5")

    ChrTalk(    #42
        0xFE,
        (
            "The Royal Army is going to be undergoing\x01",
            "substantial organizational reform.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "We're all going to be very busy in the\x01",
            "near future...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EB")

    label("loc_10B5")


    ChrTalk(    #44
        0xFE,
        "Ah, Estelle, Estelle Bright! Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I wasn't aware you'd be returning to\x01",
            "Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#000FHi, Mr. Ashton!\x01",
            "I, like, literally just got back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I see! Well, I'm sure Luke will be very\x01",
            "happy to see you've returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Luke's been dedicating himself heavily\x01",
            "to learning the way of the sword\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I had wondered what sparked\x01",
            "the sudden interest, but he doesn't\x01",
            "want to tell me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "To be honest, I'm not entirely sure how\x01",
            "to spend time with my son, since I'm out\x01",
            "of the house so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Haha... It is a little embarrassing,\x01",
            "to be honest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1033)

    label("loc_12EB")

    TalkEnd(0xE)
    Return()

    # Function_4_1015 end

    def Function_5_12EF(): pass

    label("Function_5_12EF")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_136B")

    ChrTalk(    #52
        0xB,
        (
            "Once I eat, I'm gonna go over to Luke's.\x02\x03",

            "If I go, I'm sure he'll want to play!\x01",
            "I just know it...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_136B")


    ChrTalk(    #53
        0xB,
        (
            "I went to see Luke earlier...\x02\x03",

            "But Mom dragged me back home.\x02\x03",

            "But I'm gonna go visit him again after\x01",
            "I eat.\x02\x03",

            "If I'm there, he's gonna want to play,\x01",
            "right?\x02\x03",

            "So I should go, and make him want to\x01",
            "wake up...!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1440")

    Jump("loc_15DB")

    label("loc_1443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_15DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14C9")

    ChrTalk(    #54
        0xB,
        (
            "Luke hasn't woken up, but he has\x01",
            "a really happy expression on his face.\x02\x03",

            "I bet he's having a really nice dream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DB")

    label("loc_14C9")


    ChrTalk(    #55
        0xB,
        (
            "Oh, Estelle...\x02\x03",

            "It's morning, but Luke still hasn't woken up.\x02\x03",

            "It doesn't seem like he can hear Maggy,\x01",
            "either.\x02\x03",

            "It's kinda funny, though.\x02\x03",

            "Luke's got... He's got a really happy\x01",
            "expression, even though he's asleep.\x02\x03",

            "I bet he's having a really nice dream.\x01",
            "Luke would!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_15DB")

    TalkEnd(0xB)
    Return()

    # Function_5_12EF end

    def Function_6_15DF(): pass

    label("Function_6_15DF")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_16E1")

    ChrTalk(    #56
        0xFE,
        (
            "My wife, Serra, and my son, Pat,\x01",
            "are out at a wedding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Having a wedding in the middle of THIS\x01",
            "mess... you want to talk rotten luck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Well, I guess all I can do is wish the\x01",
            "newlyweds that much more good luck\x01",
            "in their wedded life!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C1")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_18DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1869")

    ChrTalk(    #59
        0xFE,
        (
            "It was a real shock when all our orbments\x01",
            "just blinked out of existence, more or\x01",
            "less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I was reading one of my favorite books,\x01",
            "when suddenly everything went pitch\x01",
            "black!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I thought the light's orbment had broken\x01",
            "somehow, but the factory had no idea\x01",
            "why it stopped working...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "And it all started with that island in\x01",
            "the sky. I have a terrible feeling...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_18DA")

    label("loc_1869")


    ChrTalk(    #63
        0xFE,
        (
            "Apparently no one can figure out what's\x01",
            "causing the orbments to not work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "I have a terrible feeling...\x02",
    )

    CloseMessageWindow()

    label("loc_18DA")

    Jump("loc_23C1")

    label("loc_18DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1BCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19D8")

    ChrTalk(    #65
        0xFE,
        "Looks like you found the recipe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I'm personally really looking forward to\x01",
            "the traditional cooking revival that\x01",
            "book could spark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "In fact, it'd be nice to see it be part\x01",
            "of the Abend's standard menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC7")

    label("loc_19D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A7A")

    ChrTalk(    #68
        0xFE,
        (
            "I'm sure that recipe book you're looking\x01",
            "for is on one of the shelves here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "But, sorry, could you look for it\x01",
            "yourselves?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC7")

    label("loc_1A7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x200)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AA5")
    Call(1, 1)
    Jump("loc_1BC7")

    label("loc_1AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1AFC")

    ChrTalk(    #70
        0xFE,
        "Pat went out to play with Luke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I'm just glad Luke woke up at all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BC7")

    label("loc_1AFC")


    ChrTalk(    #72
        0xFE,
        "Pat went out to play with Luke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "I'm just glad Luke woke up at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Though...for him to awaken right as the\x01",
            "fog clears...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "These have been a strange few days,\x01",
            "that much is for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1BC7")

    Jump("loc_23C1")

    label("loc_1BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(    #76
        0xFE,
        (
            "'A brave knight walks through the fog\x01",
            "but loses the road, and, in the end,\x01",
            "forgets even his mission and purpose...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Seeing Rolent like this reminds me of\x01",
            "that old fairy tale.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DFF")

    label("loc_1C94")


    ChrTalk(    #78
        0xFE,
        (
            "Seems even the Royal Army men are\x01",
            "bewildered by this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "This fog reminds me of those pictures\x01",
            "of Mistwald. You know, from the old\x01",
            "stories that it was named after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "'A brave knight walks through the fog but\x01",
            "loses the road, and, in the end, forgets even\x01",
            "his mission and purpose...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Seeing Rolent like this reminds me of\x01",
            "that old fairy tale.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1DFF")

    Jump("loc_23C1")

    label("loc_1E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E9E")

    ChrTalk(    #82
        0xFE,
        (
            "So today's the day they sign the\x01",
            "non-aggression pact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Should be a day to celebrate,\x01",
            "but it's hard to be in a celebratory\x01",
            "mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F81")

    label("loc_1E9E")


    ChrTalk(    #84
        0xFE,
        (
            "So today's the day they sign the\x01",
            "non-aggression pact...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Should be a day to celebrate, but the\x01",
            "city's engulfed in this damned fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Especially with what happened to Luke,\x01",
            "it's hard to be in a mood to celebrate.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1F81")

    Jump("loc_23C1")

    label("loc_1F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2034")

    ChrTalk(    #87
        0xFE,
        (
            "That old circus troupe used to come by\x01",
            "here all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "It's been years since they've been here,\x01",
            "though. It's a shame. I'd love to see\x01",
            "them again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2210")

    label("loc_2034")


    ChrTalk(    #89
        0xFE,
        "The fog is still awful today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "It seemed like the humidity might hurt my\x01",
            "books, so I rushed to get them packed\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "In the middle of it all, though,\x01",
            "I found something really, really\x01",
            "nostalgic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "It's a ticket to an old circus\x01",
            "performance from ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I put this inside this book as a memory of\x01",
            "my first date with my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Man, oh, man. The memories.\x01",
            "Serra was so pretty back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "E-Er! Not that she's any LESS pretty now,\x01",
            "mind you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2210")

    Jump("loc_23C1")

    label("loc_2213")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_23C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_22CC")

    ChrTalk(    #96
        0xFE,
        (
            "There's lots of examples of nations being\x01",
            "invaded or meddled with during domestic\x01",
            "turmoil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I was really worried Erebonia or someone\x01",
            "might actually invade us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C1")

    label("loc_22CC")


    ChrTalk(    #98
        0xFE,
        (
            "Colonel Richard's coup was a really scary\x01",
            "time for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "I mean, there's lots of examples of nations\x01",
            "being invaded or meddled with during domestic\x01",
            "turmoil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "I was really worried Erebonia or someone\x01",
            "might actually invade us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_23C1")

    TalkEnd(0xC)
    Return()

    # Function_6_15DF end

    def Function_7_23C5(): pass

    label("Function_7_23C5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2470")

    ChrTalk(    #101
        0xFE,
        (
            "Maybe I should take a lesson from Pat and\x01",
            "get Rhett out of the house for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Haha, it might not be bad to go on a date\x01",
            "like the old days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2545")

    label("loc_2470")


    ChrTalk(    #103
        0xFE,
        (
            "It's such a relief that Luke woke up and\x01",
            "was just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "The fog's cleared, too. Perhaps I should\x01",
            "get Rhett out of the house for once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Haha, it might not be bad to go on a date\x01",
            "like the old days.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2545")

    Jump("loc_2C46")

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2689")

    ChrTalk(    #106
        0xFE,
        (
            "I feel awful for him, but...\x01",
            "I brought Pat back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "I mean, we have no idea what the cause\x01",
            "of this is, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "What if it's a contagious disease?\x01",
            "Something awful might happen to Pat, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I mean, what Maggy is going through\x01",
            "right now breaks my heart, but a parent\x01",
            "has to protect her child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C46")

    label("loc_2689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2717")

    ChrTalk(    #110
        0xFE,
        (
            "Pat went off to check on Luke as soon as\x01",
            "he got up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I just hope what happened to Luke doesn't\x01",
            "happen to him too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281E")

    label("loc_2717")


    ChrTalk(    #112
        0xFE,
        (
            "Pat went off to check on Luke as soon as\x01",
            "he got up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "I KNOW he's worried, really, I do,\x01",
            "but he didn't even stop for breakfast...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I'm worried he'll make himself ill\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I just hope what happened to Luke doesn't\x01",
            "happen to him too...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_281E")

    Jump("loc_2C46")

    label("loc_2821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 2)), scpexpr(EXPR_END)), "loc_290B")

    ChrTalk(    #116
        0xFE,
        (
            "Oh, really, my husband's shuffling his\x01",
            "books around AGAIN.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "And on top of that, he found some old scrap\x01",
            "of paper and just started smiling weirdly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "...This humidity must be making moss grow\x01",
            "on his brain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5F")

    label("loc_290B")


    ChrTalk(    #119
        0xFE,
        (
            "Oh, really, my husband's shuffling his\x01",
            "books around AGAIN.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "He has a huge pile of books he just picked\x01",
            "up on impulse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "If he's going to throw them out, he may\x01",
            "as well give them to people so that it's\x01",
            "not a waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "So, here, I'll give this to you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #123
        "\x07\x00Received #575i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23F, 1)
    OP_A2(0x10BA)

    label("loc_2A5F")

    Jump("loc_2C46")

    label("loc_2A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_2C46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B4A")

    ChrTalk(    #124
        0xFE,
        (
            "I worry about Pat playing with that wild\x01",
            "boy Luke, yes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "I do feel a little worried about him\x01",
            "spending a lot of time with my husband,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "If only there were some better role\x01",
            "models around him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C46")

    label("loc_2B4A")


    ChrTalk(    #127
        0xFE,
        (
            "Lately, Pat's been spending a lot of time\x01",
            "with my husband, reading.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "They say books are good for the soul,\x01",
            "so I think it's probably good for him,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I'm just a little worried Pat might take\x01",
            "after my husband in less admirable ways.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2C46")

    TalkEnd(0xD)
    Return()

    # Function_7_23C5 end

    def Function_8_2C4A(): pass

    label("Function_8_2C4A")

    TalkBegin(0x8)
    TalkEnd(0x8)
    Return()

    # Function_8_2C4A end

    def Function_9_2C51(): pass

    label("Function_9_2C51")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x9, 255)
    OP_6F(0x2, 15)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x9, 55200, 100, 159950, 180)
    SetChrPos(0xA, 55120, 0, 161430, 180)
    SetChrPos(0xB, 56170, 0, 161420, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x9, 6)
    SetChrSubChip(0x9, 4)
    OP_6D(51920, 350, 164390, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_2D16():
        OP_6D(54630, 350, 161690, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2D16)
    FadeToBright(1000, 0)
    Sleep(2500)
    SetChrSubChip(0x9, 5)
    Sleep(200)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0xE, 90, 400)
    OP_43(0xB, 0x1, 0x0, 0xA)
    Sleep(300)

    def lambda_2D90():
        OP_8E(0xFE, 0xC5F8, 0x0, 0x26F7A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2D90)
    WaitChrThread(0xE, 0x0)

    def lambda_2DB0():
        OP_8E(0xFE, 0xD0A2, 0x0, 0x27042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2DB0)
    WaitChrThread(0xE, 0x0)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0131   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2C51 end

    def Function_10_2DF5(): pass

    label("Function_10_2DF5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1D")
    OP_95(0xB, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    Jump("Function_10_2DF5")

    label("loc_2E1D")

    Return()

    # Function_10_2DF5 end

    SaveToFile()

Try(main)
