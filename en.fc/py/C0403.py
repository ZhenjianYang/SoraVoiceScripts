from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0403   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 16,
        MapDefaultBGM       = "ed60033",
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
        'Agate',                                # 9
        'Zin',                                  # 10
        'Gheist Bone',                          # 11
        'Professor Alba',                       # 12
        'Joshua',                               # 13
        'Nial',                                 # 14
        'Dorothy',                              # 15
        'Target Camera',                        # 16
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 16,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = -3000,
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 16,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH00390 ._CH',             # 00
        'ED6_DT07/CH00391 ._CH',             # 01
        'ED6_DT07/CH00170 ._CH',             # 02
        'ED6_DT07/CH00171 ._CH',             # 03
        'ED6_DT09/CH10090 ._CH',             # 04
        'ED6_DT09/CH10091 ._CH',             # 05
        'ED6_DT07/CH02050 ._CH',             # 06
        'ED6_DT07/CH00010 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT06/CH20064 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH00390P._CP',             # 00
        'ED6_DT07/CH00391P._CP',             # 01
        'ED6_DT07/CH00170P._CP',             # 02
        'ED6_DT07/CH00171P._CP',             # 03
        'ED6_DT09/CH10090P._CP',             # 04
        'ED6_DT09/CH10091P._CP',             # 05
        'ED6_DT07/CH02050P._CP',             # 06
        'ED6_DT07/CH00010P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT06/CH20064P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4830,
        Z                   = 250,
        Y                   = 7810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 5488,
        Z                   = 0,
        Y                   = 16806,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 1600,
        Y                   = 1000,
        Z                   = -2680,
        Range               = -1600,
        Unknown_10          = 0xFFFFF830,
        Unknown_14          = 0xFFFFE82C,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_309",          # 01, 1
        "Function_2_324",          # 02, 2
        "Function_3_4A1",          # 03, 3
        "Function_4_10AD",         # 04, 4
        "Function_5_156C",         # 05, 5
        "Function_6_157B",         # 06, 6
        "Function_7_1FAE",         # 07, 7
        "Function_8_26C7",         # 08, 8
        "Function_9_48F1",         # 09, 9
        "Function_10_490B",        # 0A, 10
        "Function_11_4931",        # 0B, 11
        "Function_12_494B",        # 0C, 12
        "Function_13_4965",        # 0D, 13
        "Function_14_49A0",        # 0E, 14
        "Function_15_4ADA",        # 0F, 15
        "Function_16_4B76",        # 10, 16
        "Function_17_4BD4",        # 11, 17
        "Function_18_4EE4",        # 12, 18
        "Function_19_4F44",        # 13, 19
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27E")
    EventBegin(0x0)
    OP_28(0x19, 0x1, 0x80)
    Event(0, 8)

    label("loc_27E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_28A"),
        (SWITCH_DEFAULT, "loc_308"),
    )


    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 6)), scpexpr(EXPR_END)), "loc_305")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x108, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, -1000, 0, -1600, 0)
    SetChrPos(0x9, 500, 0, -2620, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x9, 3)
    OP_6D(0, 0, -10700, 0)
    OP_6C(45000, 0)
    Event(0, 17)

    label("loc_305")

    Jump("loc_308")

    label("loc_308")

    Return()

    # Function_0_266 end

    def Function_1_309(): pass

    label("Function_1_309")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_323")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_323")

    Return()

    # Function_1_309 end

    def Function_2_324(): pass

    label("Function_2_324")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_48B")

    label("loc_349")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_48B")

    label("loc_362")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_48B")

    label("loc_37B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_394")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_48B")

    label("loc_394")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_48B")

    label("loc_3AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_48B")

    label("loc_3C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_48B")

    label("loc_3DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_48B")

    label("loc_3F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_48B")

    label("loc_411")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_48B")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_48B")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_48B")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_48B")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_48B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_48B")

    label("loc_4A0")

    Return()

    # Function_2_324 end

    def Function_3_4A1(): pass

    label("Function_3_4A1")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE5")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)
    OP_A2(0x258)

    ChrTalk(    #0
        0xB,
        (
            "#130FOh, hi there...Estelle, was it?\x02\x03",

            "#130FIs your partner feeling all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#000FYeah... He said he just wants\x01",
            "to get a bit of fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "#130FI see. There's certainly a nice\x01",
            "breeze up here, isn't there?\x02\x03",

            "#130FI wanted to say, however, that I'm\x01",
            "impressed that the both of you\x01",
            "are bracers at such a young age.\x02\x03",

            "#130FIf I remember correctly, one must be\x01",
            "at least 16 years of age to qualify\x01",
            "to become a bracer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#001FYou sure know your stuff.\x02\x03",

            "#001FAnd that's right.\x01",
            "I'm exactly 16 myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "#130FHow nice it is to be young. There are\x01",
            "limitless possibilities at that age.\x02\x03",

            "#130FIf I were about 10 years younger, I'd solve the\x01",
            "mysteries of all these ancient ruins across\x01",
            "the entire continent with these very hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#000FThe entire continent, huh?\x01",
            "That's a pretty tall order.\x02\x03",

            "#000FWhich means that you're not from\x01",
            "Liberl, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "#130FNo, I was born in the north.\x02\x03",

            "#130FBut just for the record...\x01",
            "I'm not from Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#001FHa ha. You don't have to worry\x01",
            "about that.\x02\x03",

            "#003FAlthough I hate war with a passion...\x01",
            "that hatred isn't directed at the people\x01",
            "of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        "#130FYou lost someone dear to you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#500F...\x02\x03",

            "#000FYeah...my mother...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "#131FI'm sorry...I didn't mean to bring\x01",
            "up any painful memories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#000FIt's okay. It happened more than\x01",
            "10 years ago.\x02\x03",

            "#000FAnd since then, there's been a\x01",
            "new addition to the family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xB,
        (
            "#130FOh, so you mean that boy over\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#001FYeah, he's like a little brother.\x02\x03",

            "#001FAlthough he's probably trying to\x01",
            "act more like an older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xB,
        "#132FHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#008FI wonder why I'm telling you all\x01",
            "of this...\x02\x03",

            "#008FUsually this isn't the kind of thing\x01",
            "a person tells others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        (
            "#130FIt's perfectly fine. Aren't good relations\x01",
            "such a wonderful thing?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_10A9")

    label("loc_BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1006")
    OP_A2(0x3)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(    #17
        0x101,
        (
            "#000FBy the way, Professor, did you learn\x01",
            "anything new about the tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xB,
        (
            "#130FNo, unfortunately I'm still as puzzled\x01",
            "as I was before I came up here.\x02\x03",

            "#130FIt seems like I'll need to do a comparative\x01",
            "investigation of the other towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#505FBy 'other towers' you mean the\x01",
            "three towers outside of the Rolent\x01",
            "region, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "#130FYes, that's right.\x02\x03",

            "#130FThe Amberl Tower in the Bose region...\x02\x03",

            "#130FThe Sapphirl Tower in the Ruan region...\x02\x03",

            "#130FThe Carnelia Tower in the Zeiss region...\x02\x03",

            "#130FIt seems as though all of these\x01",
            "towers were built at around the\x01",
            "same time as the Esmelas Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#001FYou're definitely knowledgeable on\x01",
            "the subject, that's for sure.\x02\x03",

            "#006FInvestigating is fine and all, but do\x01",
            "try and avoid the dangerous bits.\x02\x03",

            "And I know it'll cost you a little,\x01",
            "but you might want to consider hiring\x01",
            "a bracer as an escort next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "#130FUnfortunately, being a poor scholar\x01",
            "doesn't always leave me with the\x01",
            "necessary funds...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_10A9")

    label("loc_1006")


    ChrTalk(    #23
        0xB,
        (
            "#130FIt appears that this device's functions\x01",
            "have completely stopped.\x02\x03",

            "#130FUnder the right circumstances, however,\x01",
            "it may be possible to activate it anew...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A9")

    TalkEnd(0xB)
    Return()

    # Function_3_4A1 end

    def Function_4_10AD(): pass

    label("Function_4_10AD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AA")
    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    Fade(1000)
    OP_6D(-12280, 250, 14520, 0)
    SetChrPos(0xD, -9000, 0, 4732, 0)
    SetChrPos(0xE, -6000, 0, 8006, 0)
    SetChrPos(0xB, -2610, 0, 10050, 0)
    SetChrPos(0x101, -13260, 250, 12860, 0)
    SetChrPos(0xC, -12660, 250, 14050, 180)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(    #24
        0x101,
        (
            "#002F#2PAre you still feeling sick,\x01",
            "Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#010F#3PNo, I'm much better.\x02\x03",

            "#010FI should be good to head back\x01",
            "whenever everybody's ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#000F#2PI'm relieved to hear that...\x01",
            "What brought this all on anyway?\x02\x03",

            "#000FI doubt it was a lack of oxygen in\x01",
            "the tower because the rest of us\x01",
            "are all right...\x02\x03",

            "#001FMaybe it was a sudden fear\x01",
            "of heights?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "#019F#3PI-I don't think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        "#151FEstelle, Joshua!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)
    TurnDirection(0xC, 0xE, 400)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    OP_43(0xE, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(1300)
    OP_43(0xB, 0x1, 0x0, 0x5)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        "#004F#1PAre you finished taking pictures?\x02",
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0xE,
        (
            "#151F#4PYou bet I am! And I got a lot of\x01",
            "good ones, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        (
            "#141F#2PThen it looks like we're done here.\x01",
            "How about we head back to town?\x02\x03",

            "#141FAll right, greenhorns, lead the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        "#130F#4PI'm counting on you children.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    AddParty(0x1, 0xFF)
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Jump("loc_1568")

    label("loc_14AA")


    ChrTalk(    #33
        0x101,
        "#000FHow are you feeling, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        (
            "#010FI'm still a bit woozy...\x02\x03",

            "#010FI'll be resting here a little longer,\x01",
            "so why don't you keep on looking\x01",
            "around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#000FOkay, if you insist.\x02",
    )

    CloseMessageWindow()

    label("loc_1568")

    TalkEnd(0xC)
    Return()

    # Function_4_10AD end

    def Function_5_156C(): pass

    label("Function_5_156C")

    OP_92(0xFE, 0xF, 0xBB8, 0xBB8, 0x0)
    Return()

    # Function_5_156C end

    def Function_6_157B(): pass

    label("Function_6_157B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C97")
    EventBegin(0x0)
    OP_A2(0x256)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(    #36
        0xD,
        (
            "#145FOh man, the taste of a cigarette\x01",
            "is wonderful.\x02\x03",

            "#141FAt first I wasn't in the mood to come\x01",
            "do a story in a rural place like Rolent,\x01",
            "but...\x02\x03",

            "#141FSometimes these types of places\x01",
            "aren't so bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#009FIf you want to be rude like that\x01",
            "then maybe you shouldn't have\x01",
            "come at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "#142FNo can do. This was a direct order\x01",
            "from the Editor-in-Chief to teach\x01",
            "that blockhead girl a thing or two.\x02\x03",

            "#142FOtherwise, I'd be all over the kingdom\x01",
            "searching for the latest scoop right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#006FWhen you say 'scoop', don't you just\x01",
            "mean gossip for your next article?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "#141FNot that I have anything against gossip,\x01",
            "but reportage is predominantly greater.\x02\x03",

            "#141F...And in that sense, the place that\x01",
            "has my interest piqued is Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#004FThe Bose region?\x01",
            "Did something happen there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "#140FA number of large burglaries have\x01",
            "taken place one after another.\x02\x03",

            "#140FThe identity of the criminals is unknown,\x01",
            "but it seems as though the group has got\x01",
            "a pair of wings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#002FWings...?\x01",
            "Oh, I see, an airship, right?\x02\x03",

            "#002FWhat are they, sky bandits or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "#140FThat seems to be the most logical\x01",
            "conclusion.\x02\x03",

            "#140FBut there's also the possibility that\x01",
            "this could be an imitative deception\x01",
            "by the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x101,
        (
            "#004FWhat...? That's impossible!\x02\x03",

            "#004FWe're supposed to have a peace\x01",
            "treaty with them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "#140FSure, but the Empire incurred some\x01",
            "heavy losses during the war 10 years\x01",
            "ago.\x02\x03",

            "#140FThey can't do much now that every\x01",
            "other nation on the continent has\x01",
            "their eye on them, but...\x02\x03",

            "#140FIt could be a way to get back at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "#141FThat said, nobody really knows\x01",
            "for sure.\x02\x03",

            "#141FWhich is why our job as reporters\x01",
            "is to bring these things to light.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1FAA")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EC3")
    OP_A2(0x4)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(    #49
        0xD,
        (
            "#145FThe Royal Army has also been reported\x01",
            "to be making a number of new pushes\x01",
            "as well.\x02\x03",

            "#145FI tell you what, one of me is just not\x01",
            "enough to cover all the news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#002FWhat do you mean by 'new pushes'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        (
            "#140FYou see, there was a young, smart\x01",
            "apple in the war college.\x02\x03",

            "#140FAnd it seems that he breathed a bit\x01",
            "of new life into the understaffed and\x01",
            "outdated Royal Army.\x02\x03",

            "#140FI'd really like to figure out a way to\x01",
            "get an appointment with the guy...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_1FAA")

    label("loc_1EC3")


    ChrTalk(    #52
        0xD,
        (
            "#141FBut anyway, cigarettes are the way\x01",
            "to go at a time like this.\x02\x03",

            "#141FThe non-smoking boom in the Royal City\x01",
            "has really started to feel oppressive...\x02\x03",

            "#147FBut the more I think about it, this\x01",
            "is the one thing I can't quit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAA")

    TalkEnd(0xD)
    Return()

    # Function_6_157B end

    def Function_7_1FAE(): pass

    label("Function_7_1FAE")

    TalkBegin(0xE)
    SetChrChipByIndex(0xE, 9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_241F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)
    OP_A2(0x257)

    ChrTalk(    #53
        0xE,
        (
            "#151FOh, Estelle. This place is wonderful,\x01",
            "isn't it? \x02\x03",

            "#151FI'm even starting to wonder if the number\x01",
            "of photo-quartz is going to be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#000FThe scenery sure is great like you say.\x02\x03",

            "#000FBy the way, what's a photo-quartz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "#150FIt's an ultra-thin crystal circuit fabricated\x01",
            "from septium.\x02\x03",

            "#150FIt's set up so that you can take a\x01",
            "photograph by burning it with light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#004FThat's just what I'd expect from a\x01",
            "camerawoman. Someone who knows the\x01",
            "tools of the trade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xE,
        (
            "#151FTee hee.\x02\x03",

            "#153FThat reminds me.\x01",
            "What's the deal with Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#000FWell... He says he's getting some\x01",
            "fresh air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "#150FA raven-haired young man standing\x01",
            "silently in the flowing breeze...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0xE,
        (
            "#151FI think I could take a really good picture\x01",
            "with that kind of a setting.\x02\x03",

            "#151FDo you think he'd let me snap a\x01",
            "shot of him if I asked?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#008FHe doesn't seem to be a fan of\x01",
            "that kind of stuff.\x02\x03",

            "#008FI think he'd probably turn you down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xE,
        (
            "#154FAwww... What a waste...\x02\x03",

            "#151FHe's probably just shy, right?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_26C3")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267C")
    OP_A2(0x5)
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xF, 0x320)

    ChrTalk(    #63
        0xE,
        (
            "#151FOh, I know! If Joshua doesn't want\x01",
            "to pose for a photograph then how\x01",
            "about you, Estelle?\x02\x03",

            "#151FWould you mind if I took your\x01",
            "photograph?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#004FWh-Who? Me?\x02\x03",

            "#004FWhat do you want to do with a\x01",
            "picture of me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xE,
        (
            "#151FWe'll, you're cute and I can feel this\x01",
            "strong aura emanating from you.\x02\x03",

            "#151FYou might even be able to grace\x01",
            "the cover of a magazine.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #66
        0x101,
        (
            "#008FP-Pass! No matter which way I think\x01",
            "about it, that's just not my style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xE,
        "#154FI feel like I just got dumped...\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_26C3")

    label("loc_267C")


    ChrTalk(    #68
        0xE,
        (
            "#151FOh well. I wonder what I should take\x01",
            "a photograph of next...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26C3")

    TalkEnd(0xE)
    Return()

    # Function_7_1FAE end

    def Function_8_26C7(): pass

    label("Function_8_26C7")

    EventBegin(0x0)
    OP_A2(0x255)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x101, 90, 0, -4010, 0)
    SetChrPos(0xC, 90, 0, -4010, 0)
    SetChrPos(0xD, 90, 0, -4010, 0)
    SetChrPos(0xE, 90, 0, -4010, 0)
    RemoveParty(0xF, 0xFF)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0xE, 0xFF)
    OP_6D(-2600, 0, 20370, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(5300, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)

    def lambda_2794():
        OP_6D(-60, 0, 2490, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2794)

    def lambda_27AC():
        OP_8E(0xFE, 0xFFFFFFD8, 0x0, 0x11C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_27AC)
    Sleep(500)

    def lambda_27CC():
        OP_8E(0xFE, 0x3FC, 0x0, 0xE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27CC)
    Sleep(500)

    def lambda_27EC():
        OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0xC94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_27EC)
    Sleep(500)

    def lambda_280C():
        OP_8E(0xFE, 0xFFFFFFEC, 0x0, 0x9BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_280C)
    Sleep(3500)
    Fade(1000)
    OP_6D(90, 0, 3680, 0)
    OP_6B(3700, 0)
    OP_8C(0x101, 90, 0)
    OP_8C(0xC, 90, 0)
    OP_8C(0xD, 315, 0)
    OP_8C(0xE, 270, 0)
    OP_0D()

    ChrTalk(    #69
        0x101,
        (
            "#000FWow, it's bright out here...\x02\x03",

            "#000FIt looks like we finally made\x01",
            "it to the rooftop.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0xE,
        (
            "#151FWould you look at the\x01",
            "beautiful scenery!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xD,
        (
            "#147FNow, this is something else.\x01",
            "It looks like we'll be able to get a better\x01",
            "shot than I had originally anticipated.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(300)

    ChrTalk(    #72
        0xD,
        (
            "#141FAnd that's the thing I was\x01",
            "telling you about earlier...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0xC, 0, 400)
    OP_8C(0xE, 0, 400)

    def lambda_29F3():
        OP_6D(430, 950, 12060, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29F3)

    def lambda_2A0B():
        OP_67(0, 5170, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2A0B)

    def lambda_2A23():
        OP_6B(4840, 3000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2A23)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x101,
        (
            "#004F#1PI wonder what that's supposed\x01",
            "to be exactly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "#151F#1PIt looks like a giant orbment-operated\x01",
            "cauldron if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        (
            "#141F#1PAccording to my sources,\x01",
            "it's some sort of ancient device.\x02\x03",

            "#141FAlthough nobody seems to know\x01",
            "what exactly it's used for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#000F#1PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_2B76():
        OP_6D(90, 0, 3680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B76)

    def lambda_2B8E():
        OP_67(0, 6500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B8E)

    def lambda_2BA6():
        OP_6B(3700, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2BA6)
    Sleep(1500)
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #77
        0x101,
        (
            "#501FHey, Joshua.\x01",
            "Did you know something\x01",
            "like this was up here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        "#015F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0xD, 0xC, 400)
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(    #79
        0x101,
        "#002FJoshua?\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 45, 400)
    OP_6D(2710, 250, 5470, 1000)

    ChrTalk(    #80
        0xC,
        (
            "#510F#2PIt's no use hiding...\x02\x03",

            "#510FI think it would be wise to come\x01",
            "out where we can see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#004F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0xB,
        "Man's Voice",
        "Please don't hurt me...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #83
        0xB,
        "Man's Voice",
        (
            "I'll come out already!\x01",
            "I'm coming out right now!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_43(0xB, 0x1, 0x0, 0xD)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xB, 0xDA2, 0xFA, 0x2058, 0xBB8, 0x0)
    OP_8C(0xB, 225, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #84
        0x101,
        "#004F#2PWh-Who is this guy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xD,
        (
            "#143FSo somebody arrived before\x01",
            "we did, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xE,
        (
            "#153FWhat a surprise that was.\x01",
            "Nice find, Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xC,
        "#014F#2P...And you are...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0xB,
        "Spectacled Man",
        (
            "#131FI apologize, please forgive me!\x02\x03",

            "#131FI'll give you every last mira I have!\x01",
            "Please spare my life!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #89
        0x101,
        (
            "#007F#2PLook here, buddy...\x01",
            "Please don't mistake us for\x01",
            "robbers or something weird.\x02\x03",

            "#007FYou do recognize this emblem,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #90
        "\x07\x05Estelle showed the man her guild emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    NpcTalk(    #91
        0xB,
        "Spectacled Man",
        (
            "#130FWait, isn't that the Bracer Guild's...\x02\x03",

            "#130FSo...you're trying to tell me\x01",
            "that you're bracers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#006F#2PIn the flesh.\x02\x03",

            "#006FI'm Estelle, and this is Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        (
            "#141FAnd we're here as reporters\x01",
            "from the Liberl News.\x02\x03",

            "#141FWe're having these two provide\x01",
            "our escort so we can get coverage\x01",
            "on the tower.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3135():
        OP_6D(380, 0, 5840, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3135)
    OP_8E(0xB, 0x1E, 0x0, 0x1B58, 0xBB8, 0x0)
    OP_8C(0xB, 180, 400)

    NpcTalk(    #94
        0xB,
        "Spectacled Man",
        (
            "#131FI'm relieved to hear that.\x01",
            "Please just don't ever scare\x01",
            "me like that again...\x02\x03",

            "#131FThe fact that you came up here like\x01",
            "that made me suspicious of you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xC,
        (
            "#018FLook who's talking.\x01",
            "You seem like quite the\x01",
            "suspicious fellow yourself...\x02\x03",

            "#018FDo you mind telling us\x01",
            "who you are exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xB,
        (
            "#130FI apologize for my belated\x01",
            "introduction. My name is Alba,\x01",
            "and I am an archaeologist.\x02\x03",

            "#130FI came to investigate the tower in\x01",
            "order to further my research of\x01",
            "ancient civilizations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xE,
        (
            "#153FAll alone?\x01",
            "I'm surprised you made it\x01",
            "here in one piece.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xB,
        (
            "#130FAh...ha ha...somewhat...\x01",
            "But actually, I've grown accustomed\x01",
            "to investigating ruins like these.\x02\x03",

            "#130FYou see, I've got a lot of confidence\x01",
            "in my ability to flee from monsters\x01",
            "if need be.\x02\x03",

            "#130F...Although this time I found myself\x01",
            "in a bit of a pickle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#008FYou are one crazy scholar\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        (
            "#140FHowever, being an archaeologist\x01",
            "would mean that you're familiar\x01",
            "with the tower's origins, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        (
            "#130FWell, more than the average\x01",
            "person anyway...\x02\x03",

            "#130FBut since I have only just begun\x01",
            "my investigation, there are still a\x01",
            "lot of things I don't know myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "#141FThat's fine, but is there anything\x01",
            "interesting you could tell us about\x01",
            "this place?\x02\x03",

            "#141FIt'll be used for an article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xB,
        "#130FLet's see...\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xB)
    Sleep(500)

    ChrTalk(    #104
        0xB,
        (
            "#130FHas everyone heard of the\x01",
            "'Sept-Terrions' before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#004FI think Father Divine maybe said\x01",
            "something about that before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xC,
        (
            "#012FYou mean the Seven Treasures endowed\x01",
            "with power and bestowed upon the\x01",
            "ancients by Aidios, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xB,
        (
            "#130FThat's exactly what I'm referring to!\x02\x03",

            "#130FIt seems these ancients ruled\x01",
            "the earth, seas, and skies using\x01",
            "the powers of these treasures.\x02\x03",

            "#130FIt has also been written that\x01",
            "they were even able to unlock\x01",
            "the secrets of time and life...\x02\x03",

            "#130FApproximately 1200 years ago, when this ancient\x01",
            "civilization was destroyed by a mysterious\x01",
            "calamity, these Sept-Terrions were also lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "#140FThat is the legend also recorded\x01",
            "in the scriptures of the Septian\x01",
            "Church.\x02\x03",

            "#140FBut what does that have to do\x01",
            "with this tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xB,
        (
            "#130FA part of the legend states that\x01",
            "one of these Sept-Terrions slumbers\x01",
            "somewhere within Liberl.\x02\x03",

            "#132FIts name: the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#501FThe Aureole...\x01",
            "The word certainly has a\x01",
            "strange ring to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#130FIf the legend is really true, I figured I might be\x01",
            "able to find some clues here at the tower, since\x01",
            "it's one of the oldest ruins in all of Liberl.\x02\x03",

            "#130FSo I came out to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xE,
        "#151FAwww... What an inspiring story!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xB,
        (
            "#130FIt is, isn't it?! You can feel my\x01",
            "passion for things of antiquity,\x01",
            "right?!!!\x02\x03",

            "#130FThis is splendid! I am overjoyed\x01",
            "that there is someone else who\x01",
            "understands the way I feel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xC,
        (
            "#012FSo...did you find any of those\x01",
            "clues you were looking for?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #115
        0xB,
        (
            "#131FI-I'm still working on that part...\x02\x03",

            "#131FBut if I can figure out how this\x01",
            "device works, I might be on to\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xD,
        (
            "#145FI think it's an interesting story,\x01",
            "but as it stands, it's a speculative\x01",
            "one.\x02\x03",

            "#145FFrom what you've told me, I'm\x01",
            "sorry to say, it wouldn't fly\x01",
            "as an article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xB,
        (
            "#131FI see...that's extremely\x01",
            "disappointing to hear.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xB, 0xFF)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #118
        0x101,
        (
            "#006FI'm surprised myself. Contrary\x01",
            "to my expectations, you ARE serious\x01",
            "about the articles you write.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #119
        0xD,
        (
            "#141F#5PThat's because I can't write articles\x01",
            "based on uncertain news sources.\x02\x03",

            "#141FWe may run the occasional gossip\x01",
            "column, but it's the policy of the Liberl\x01",
            "News to verify our information.\x02\x03",

            "#141FThat aside, let's get what we\x01",
            "came here for, shall we?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    TurnDirection(0xD, 0xE, 400)
    TurnDirection(0x101, 0xE, 400)
    OP_21()
    OP_1D(0x1)

    ChrTalk(    #120
        0xD,
        (
            "#140F#5PDorothy, I want you to get several\x01",
            "panorama shots of the Rolent region.\x02\x03",

            "#140FEverything else I'll leave up to\x01",
            "your aesthetic touch.\x02\x03",

            "#140FNow get out there and get me\x01",
            "some good pictures!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)
    OP_62(0xE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0xE,
        (
            "#151FUnderstood!\x02\x03",

            "#151FYour apprentice, Dorothy Hyatt,\x01",
            "is ready for action!\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x2)
    OP_43(0xE, 0x1, 0x0, 0xD)
    OP_8C(0xE, 270, 400)
    OP_8E(0xE, 0xFFFFF0E2, 0xFA, 0xD5C, 0x1388, 0x0)
    OP_8E(0xE, 0xFFFFDD14, 0xFA, 0x12C, 0x1388, 0x0)
    OP_44(0xE, 0xFF)
    Sleep(1000)
    TurnDirection(0xD, 0xB, 400)
    TurnDirection(0xC, 0xB, 400)
    TurnDirection(0x101, 0xB, 400)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #122
        0xD,
        (
            "#141FAnd as for you, Mr. Archaeologist,\x01",
            "how about heading back to town\x01",
            "with us when we're done here?\x02\x03",

            "#141FThese two kids may look like a\x01",
            "couple of brats, but they do a\x01",
            "pretty fine job as escorts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#009FSomething about the way you said\x01",
            "that makes me feel like it wasn't a\x01",
            "compliment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "#130FIf it's all right with you to\x01",
            "have me along, then that's\x01",
            "far more than I could ask for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xD,
        (
            "#141FThen, I guess it's decided.\x02\x03",

            "#141FSo, how about we take a break\x01",
            "until Dorothy finishes getting\x01",
            "her shots?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xB, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_69(0xF, 0x320)
    SetChrPos(0x101, -13260, 250, 12860, 270)
    SetChrPos(0xC, -12660, 250, 14050, 270)
    SetChrPos(0xD, 15093, 250, 5901, 90)
    SetChrPos(0xE, -12962, 0, 3438, 270)
    SetChrPos(0xB, -370, 950, 12896, 0)
    OP_43(0xB, 0x0, 0x0, 0xF)
    OP_43(0xD, 0x0, 0x0, 0x2)
    FadeToBright(1000, 0)
    OP_69(0xD, 0x0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_69(0xB, 0x0)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x0, 0xE)
    Sleep(2900)
    Fade(1000)
    OP_6D(-9350, 250, 760, 0)
    Sleep(2800)
    OP_8C(0xE, 225, 400)
    Sleep(500)
    OP_44(0xE, 0xFF)
    OP_62(0xE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_6D(-18140, 250, 14540, 0)
    Sleep(1000)
    SetChrPos(0xE, -12962, 0, 3438, 270)
    OP_43(0xE, 0x0, 0x0, 0xE)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #126
        0x101,
        (
            "#001F#3PWow! The view is great from here.\x02\x03",

            "#001FFrom this height, I can see all\x01",
            "of Rolent!\x02\x03",

            "#000FWith scenery this good, if someone turned\x01",
            "this place into a tourist spot, they'd\x01",
            "probably make a boatload of mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xC,
        (
            "#013F#3PYeah...you're probably right\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()
    OP_6D(-15070, 250, 13930, 1000)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #128
        0x101,
        (
            "#002F#3P...\x02\x03",

            "#002FWhat's wrong?\x01",
            "You look a little pale.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 225, 400)

    ChrTalk(    #129
        0xC,
        (
            "#019F#3PI can't hide anything from you,\x01",
            "can I?\x02\x03",

            "#019FAfter we stepped onto the roof,\x01",
            "I just started feeling...a little\x01",
            "woozy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#004F#3PAre you going to be okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xC,
        (
            "#010F#3PYeah, I think I'll be all right\x01",
            "once I get a bit of fresh air...\x02\x03",

            "#010FWhy don't you make the best of\x01",
            "this opportunity and have a look\x01",
            "around yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#003F#3PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xC,
        (
            "#011F#3PBroadening one's knowledge during\x01",
            "a time like this is all a part of\x01",
            "being a bracer.\x02\x03",

            "#011FIf you come across anything of\x01",
            "interest then you can tell me\x01",
            "about it later, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#007F#3PSometimes you can be such a\x01",
            "smooth talker, you know that?\x02\x03",

            "#000FAll right, I'll have a look around...\x02\x03",

            "#000FBut...if you start feeling any\x01",
            "worse, you let me know, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        "#019F#3PSure.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    OP_8C(0xC, 270, 400)
    OP_43(0xC, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_8_26C7 end

    def Function_9_48F1(): pass

    label("Function_9_48F1")

    Sleep(1300)
    OP_8E(0x101, 0xFFFFFF00, 0x3B6, 0x32F0, 0xBB8, 0x0)
    Return()

    # Function_9_48F1 end

    def Function_10_490B(): pass

    label("Function_10_490B")

    Sleep(2000)
    OP_8E(0xC, 0x4C2, 0x0, 0x2726, 0xBB8, 0x0)
    Sleep(1000)
    OP_8C(0xC, 45, 400)
    Return()

    # Function_10_490B end

    def Function_11_4931(): pass

    label("Function_11_4931")

    Sleep(1500)
    OP_8E(0xD, 0xFFFFFBC4, 0x3B6, 0x2F52, 0xBB8, 0x0)
    Return()

    # Function_11_4931 end

    def Function_12_494B(): pass

    label("Function_12_494B")

    Sleep(1500)
    OP_8E(0xE, 0xE1, 0x3B6, 0x2EBE, 0xBB8, 0x0)
    Return()

    # Function_12_494B end

    def Function_13_4965(): pass

    label("Function_13_4965")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_499F")
    TurnDirection(0x0, 0xFE, 0)
    TurnDirection(0xC, 0xFE, 0)
    TurnDirection(0xD, 0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4994")
    TurnDirection(0xE, 0xFE, 0)
    Jump("loc_499B")

    label("loc_4994")

    TurnDirection(0xB, 0xFE, 0)

    label("loc_499B")

    OP_48()
    Jump("Function_13_4965")

    label("loc_499F")

    Return()

    # Function_13_4965 end

    def Function_14_49A0(): pass

    label("Function_14_49A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AD9")
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFCD5E, 0x0, 0xD6E, 0x7D0, 0x0)
    OP_8C(0xE, 270, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFD04E, 0x0, 0xFFFFF27C, 0x7D0, 0x0)
    OP_8C(0xE, 225, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1500)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x33, 0x0, 0xFFFFFE09, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    OP_8C(0xE, 180, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x1B82, 0x0, 0x18EE, 0x7D0, 0x0)
    OP_8C(0xE, 90, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0x330E, 0x0, 0x3543, 0x7D0, 0x0)
    OP_8C(0xE, 45, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(3000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFFFE9, 0x0, 0x22F4, 0x7D0, 0x0)
    OP_8C(0xE, 0, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(1000)
    SetChrChipByIndex(0xE, 9)
    OP_8E(0xE, 0xFFFFE978, 0x0, 0x2D03, 0x7D0, 0x0)
    OP_8C(0xE, 45, 400)
    SetChrChipByIndex(0xE, 10)
    Sleep(2000)
    Jump("Function_14_49A0")

    label("loc_4AD9")

    Return()

    # Function_14_49A0 end

    def Function_15_4ADA(): pass

    label("Function_15_4ADA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B75")
    OP_97(0xB, 0x8E, 0x3E1C, 0x7530, 0x3E8, 0x1)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0xFFFFD8F0, 0x1F4, 0x2)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0x1388, 0x2BC, 0x2)
    Sleep(1000)
    OP_97(0xB, 0x8E, 0x3E1C, 0xC350, 0x3E8, 0x1)
    OP_8B(0xB, 0x8E, 0x3E1C, 0x190)
    Sleep(1000)
    Jump("Function_15_4ADA")

    label("loc_4B75")

    Return()

    # Function_15_4ADA end

    def Function_16_4B76(): pass

    label("Function_16_4B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BD3")
    EventBegin(0x1)
    ClearMapFlags(0x1)

    ChrTalk(    #136
        0x101,
        "#000F(I'd better not go off by myself...)\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4BD3")

    Return()

    # Function_16_4B76 end

    def Function_17_4BD4(): pass

    label("Function_17_4BD4")

    OP_43(0x8, 0x0, 0x0, 0x12)
    OP_43(0x9, 0x0, 0x0, 0x13)
    OP_A2(0x0)
    OP_A2(0x1)
    OP_6D(0, 1000, 12000, 4000)
    OP_A5(0x1)
    OP_A5(0x0)
    OP_20(0x5DC)
    Sleep(1000)
    OP_21()

    ChrTalk(    #137
        0x8,
        "#050F………………妙だな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "#050F気配は感じるのに\x01",
            "どこにも魔獣の姿なんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #139
        0x9,
        "#070F#4S上だ、気を付けろ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        "#050Fなにッ！？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x28)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 0, 10000, 16000, 0)

    ChrTalk(    #141
        0xA,
        "#4Sキシャアアアアアアアアッ！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1)
    SetChrChipByIndex(0xA, 5)
    OP_8E(0xA, 0x0, 0x3E8, 0x2DE1, 0x1770, 0x0)
    OP_43(0xA, 0x3, 0x0, 0x2)
    Sleep(500)
    SetChrChipByIndex(0xA, 4)
    OP_A5(0x1)
    OP_A5(0x0)
    Sleep(1000)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0x108, 0x8)
    Battle(0x5E, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x0)
    OP_21()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #142
        (
            "\x07\x05お疲れさまでした。\x01",
            "これで戦闘用体験版は終了です。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #143
        (
            "今回は、戦闘の感覚・手応えを\x01",
            "掴んでもらうためのバージョンで、\x01",
            "入らなかった要素も多々ありました。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #144
        (
            "次回は、プレイしていただいた方々の\x01",
            "意見・感想を元に、より完成度の高い\x01",
            "体験版を提供したいと思っています。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #145
        "──それではメニューに戻ります。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    NewScene("ED6_DT01/T0001   ._SN", 0, 0, 0)
    IdleLoop()
    SetMapFlags(0x1)
    Return()

    # Function_17_4BD4 end

    def Function_18_4EE4(): pass

    label("Function_18_4EE4")

    OP_A6(0x0)
    Sleep(500)
    OP_8E(0xFE, 0xFFFFFF9C, 0x3E8, 0x3019, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    Sleep(500)
    OP_44(0xFE, 0x3)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x1B58)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x0)
    Return()

    # Function_18_4EE4 end

    def Function_19_4F44(): pass

    label("Function_19_4F44")

    OP_A6(0x1)
    Sleep(500)
    OP_8E(0xFE, 0x3A2, 0x0, 0x28DD, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 2)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    Sleep(500)
    OP_44(0xFE, 0x3)
    TurnDirection(0xFE, 0xA, 0)
    OP_95(0xFE, 0x3E8, 0x0, 0xFFFFF448, 0x7D0, 0x1B58)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_A3(0x1)
    Return()

    # Function_19_4F44 end

    SaveToFile()

Try(main)
