from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2110   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Bridget',                              # 9
        'Belden',                               # 10
        'Ciel',                                 # 11
        'Eletta',                               # 12
        'Renzo',                                # 13
        'Liz',                                  # 14
        'Antonio',                              # 15
        'Noria',                                # 16
        'Louis',                                # 17
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
        'ED6_DT07/CH01230 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01170 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01690 ._CH',             # 07
        'ED6_DT07/CH01470 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01230P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01170P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01690P._CP',             # 07
        'ED6_DT07/CH01470P._CP',             # 08
    )

    DeclNpc(
        X                   = 24980,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -28000,
        Z                   = 0,
        Y                   = 61400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 1950,
        Z                   = 0,
        Y                   = 5470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 0,
        Y                   = 1090,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 23690,
        Z                   = 0,
        Y                   = 4490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27150,
        Z                   = 0,
        Y                   = -1550,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 26000,
        Z                   = 4000,
        Y                   = -510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -5740,
        Z                   = 0,
        Y                   = 35100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 5430,
        Z                   = 0,
        Y                   = 64750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_304",          # 02, 2
        "Function_3_31A",          # 03, 3
        "Function_4_33E",          # 04, 4
        "Function_5_362",          # 05, 5
        "Function_6_60E",          # 06, 6
        "Function_7_E1D",          # 07, 7
        "Function_8_153C",         # 08, 8
        "Function_9_1C66",         # 09, 9
        "Function_10_207C",        # 0A, 10
        "Function_11_236A",        # 0B, 11
        "Function_12_2C22",        # 0C, 12
        "Function_13_3416",        # 0D, 13
        "Function_14_3784",        # 0E, 14
        "Function_15_42BE",        # 0F, 15
        "Function_16_4302",        # 10, 16
        "Function_17_4346",        # 11, 17
        "Function_18_6699",        # 12, 18
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_232")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xD, 27250, 0, -1740, 87)
    Jump("loc_2A8")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_24B")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2A8")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_27F")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 1700, 0, 2029, 90)
    Jump("loc_2A8")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_28E")
    SetChrFlags(0xC, 0x80)
    Jump("loc_2A8")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29C")
    Jump("loc_2A8")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2A8")
    SetChrFlags(0xC, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_2B7")
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2DE")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_2D2")
    SetChrPos(0x8, -230, 0, 63820, 270)
    Jump("loc_2DE")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrFlags(0x9, 0x10)

    label("loc_2DE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_2EA"),
        (SWITCH_DEFAULT, "loc_302"),
    )


    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FF")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_2FF")

    Jump("loc_302")

    label("loc_302")

    Return()

    # Function_0_212 end

    def Function_1_303(): pass

    label("Function_1_303")

    Return()

    # Function_1_303 end

    def Function_2_304(): pass

    label("Function_2_304")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_304")

    label("loc_319")

    Return()

    # Function_2_304 end

    def Function_3_31A(): pass

    label("Function_3_31A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33D")
    OP_8D(0xFE, -6630, 65280, -3270, 67330, 1000)
    Jump("Function_3_31A")

    label("loc_33D")

    Return()

    # Function_3_31A end

    def Function_4_33E(): pass

    label("Function_4_33E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_361")
    OP_8D(0xFE, -2620, 970, 1167, -2110, 3000)
    Jump("Function_4_33E")

    label("loc_361")

    Return()

    # Function_4_33E end

    def Function_5_362(): pass

    label("Function_5_362")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404")

    ChrTalk(    #0
        0xFE,
        "My brother said he's helping out our dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Maybe if he's working that hard, I should, too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Okay! Then I'll go help out Mom!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_467")

    label("loc_404")


    ChrTalk(    #3
        0xFE,
        "My brother said he's helping out our dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "If he's helping out Dad, I'll go help out Mom!\x02",
    )

    CloseMessageWindow()

    label("loc_467")

    Jump("loc_60A")

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_500")

    ChrTalk(    #5
        0xFE,
        (
            "With the orbments stopped, my\x01",
            "dad's job's gotten lots harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "He's probably not too worried, though.\x01",
            "I'm sure he'll fix 'em soon!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_55B")

    ChrTalk(    #7
        0xFE,
        "My brother's started workin'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "It sounds like he's helping out our dad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_565")
    Jump("loc_60A")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A1")

    ChrTalk(    #9
        0xFE,
        "My dad's away because of the 'elekshun.'\x02",
    )

    CloseMessageWindow()
    Jump("loc_60A")

    label("loc_5A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_60A")

    ChrTalk(    #10
        0xFE,
        "My brother's not playing with meee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Even though he's home for the\x01",
            "first time in AGES.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A")

    TalkEnd(0xFE)
    Return()

    # Function_5_362 end

    def Function_6_60E(): pass

    label("Function_6_60E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_7E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_744")

    ChrTalk(    #12
        0xFE,
        (
            "This is just a rumor, but I heard there\x01",
            "was an incident at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Well, I'm sure my son Logic's safe,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "He's surprisingly cowardly, so I'm\x01",
            "sure he ran or hid straightaway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "As a parent, it's much greater comfort to\x01",
            "have a cowardly child than a brave one.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_7E2")

    label("loc_744")


    ChrTalk(    #16
        0xFE,
        (
            "I heard there was an incident at the academy,\x01",
            "but I'm sure my son Logic's safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "He's surprisingly cowardly, so I'm\x01",
            "sure he ran or hid straightaway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E2")

    Jump("loc_E19")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_99D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90E")

    ChrTalk(    #18
        0xFE,
        (
            "With the orbments not working,\x01",
            "the harbor block's a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "My husband got called out by the mayor,\x01",
            "and he's been gone all morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "He gets beaten by the man in the election,\x01",
            "but still said he'd do anything he can for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "Really, my husband's way too kind.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_99A")

    label("loc_90E")


    ChrTalk(    #22
        0xFE,
        (
            "With the orbments not working,\x01",
            "the harbor block's a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "My husband got called out by the mayor,\x01",
            "and he's been gone all morning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99A")

    Jump("loc_E19")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_A5E")

    ChrTalk(    #24
        0xFE,
        (
            "I guess at some point I'll go off and\x01",
            "see how he's doing on the front lines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I've gotta make sure to kick some fire into him,\x01",
            "or he'll start giving up too easily, I'm sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E19")

    label("loc_A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_B09")

    ChrTalk(    #26
        0xFE,
        (
            "Seems like there was a fight\x01",
            "between the supporters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Knowing my husband, I'm sure he tried to\x01",
            "stop everyone but just couldn't keep\x01",
            "them under control.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E19")

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B94")

    ChrTalk(    #28
        0xFE,
        "My son's logic sounds like a theory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "He gets so focused on 'reason' when\x01",
            "anything happens, it ticks me off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C5B")

    label("loc_B94")

    OP_A2(0x5)

    ChrTalk(    #30
        0xFE,
        (
            "That reminds me, the royal academy's\x01",
            "going to have a long break soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "That means my son is going to be\x01",
            "around the house all day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "*sigh* Just thinking about it\x01",
            "makes my head hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B")

    Jump("loc_E19")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_D11")

    ChrTalk(    #33
        0xFE,
        (
            "Even though my husband's a mayoral\x01",
            "candidate, he's still got no guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If you wanna see what kind of face he's\x01",
            "got on, go look at the wall of the house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E19")

    label("loc_D11")

    OP_A2(0x5)

    ChrTalk(    #35
        0xFE,
        (
            "Even though my husband's a mayoral\x01",
            "candidate, he's still got no guts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "He's always saying he's not got the goods\x01",
            "for the job. I mean, REALLY. This isn't the\x01",
            "time for such whining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "His supporters are watching, so\x01",
            "I wish he'd get it together a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E19")

    TalkEnd(0xFE)
    Return()

    # Function_6_60E end

    def Function_7_E1D(): pass

    label("Function_7_E1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEB")

    ChrTalk(    #38
        0xFE,
        (
            "This time there's a case at the academy,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Really, what's happening to the Liberl Kingdom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I'm worried whether the admissions\x01",
            "exams will even be held as planned.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_F55")

    label("loc_EEB")


    ChrTalk(    #41
        0xFE,
        (
            "This time there's a case at the academy,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "Really, what's happening to the Liberl Kingdom.\x02",
    )

    CloseMessageWindow()

    label("loc_F55")

    Jump("loc_1538")

    label("loc_F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1120")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1086")

    ChrTalk(    #43
        0xFE,
        (
            "I had Gerome tutor me for the entrance\x01",
            "exams while the academy was on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Thanks to that I'm pretty confident\x01",
            "I'm set for the exams, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "The orbments have stopped, and there are\x01",
            "weird things floating in the sky. How am\x01",
            "I supposed to study at a time like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_111D")

    label("loc_1086")


    ChrTalk(    #46
        0xFE,
        (
            "Thanks to Gerome's advice\x01",
            "I'm all set for exams, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "With all the crazy stuff going on in the world\x01",
            "right now, I can't focus on studying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111D")

    Jump("loc_1538")

    label("loc_1120")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_119E")

    ChrTalk(    #48
        0xFE,
        (
            "Gerome's gonna be my tutor\x01",
            "while he's on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Okay, time to buckle down and\x01",
            "study, study, study!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1243")

    label("loc_119E")

    OP_A2(0x4)

    ChrTalk(    #50
        0xFE,
        (
            "Gerome's gonna be my tutor\x01",
            "while the academy's on break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Having someone that's actually\x01",
            "passed the exam helping me out\x01",
            "should make that thing a breeze.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1243")

    Jump("loc_1538")

    label("loc_1246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1250")
    Jump("loc_1538")

    label("loc_1250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_12AF")

    ChrTalk(    #52
        0xFE,
        "My father was kind of panicking, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "...Is something happening outside?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1332")

    ChrTalk(    #54
        0xFE,
        (
            "Having Gerome help me study would\x01",
            "be best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "My mom has this weird rivalry with our neighbors.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F8")

    label("loc_1332")

    OP_A2(0x4)

    ChrTalk(    #56
        0xFE,
        (
            "My neighbor, Gerome's attending\x01",
            "the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Having him oversee my study for the entrance\x01",
            "exams would be reassuring, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "My mom has this weird rivalry with our neighbors.\x02",
    )

    CloseMessageWindow()

    label("loc_13F8")

    Jump("loc_1538")

    label("loc_13FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1496")

    ChrTalk(    #59
        0xFE,
        (
            "From what I hear, the entrance exams\x01",
            "for the royal academy are pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I'm doing my best, but honestly\x01",
            "I'm kinda nervous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_1496")

    OP_A2(0x4)

    ChrTalk(    #61
        0xFE,
        (
            "My dream is to be part of the\x01",
            "crew for an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "If I can join the royal academy's natural science\x01",
            "courses, I'll be one step closer to that dream.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1538")

    TalkEnd(0xFE)
    Return()

    # Function_7_E1D end

    def Function_8_153C(): pass

    label("Function_8_153C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161E")

    ChrTalk(    #63
        0xFE,
        (
            "This is just a little rumor I picked up,\x01",
            "but I heard there was an INCIDENT over\x01",
            "at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Apparently everything turned out fine\x01",
            "in the end, and now the Royal Army's\x01",
            "guarding it, I hear.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_16BB")

    label("loc_161E")


    ChrTalk(    #65
        0xFE,
        (
            "I heard there was an incident over\x01",
            "at the academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Apparently everything turned out fine\x01",
            "in the end, and now the Royal Army's\x01",
            "guarding it, I hear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BB")

    Jump("loc_1C62")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(    #67
        0xFE,
        (
            "Errr, where did I put the lamp oil,\x01",
            "I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "My son's exam studies are at the\x01",
            "most important time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "No matter what, I've got to keep\x01",
            "the light on that table on!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_17F5")

    label("loc_178D")


    ChrTalk(    #70
        0xFE,
        (
            "Errr, where did I put the lamp oil,\x01",
            "I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Oh, maybe I should have my\x01",
            "husband go buy some.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F5")

    Jump("loc_1C62")

    label("loc_17F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_18A6")

    ChrTalk(    #72
        0xFE,
        (
            "He's got a private tutor lined up,\x01",
            "so he should be set for the upcoming\x01",
            "entrance exams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Now I just have to figure out how\x01",
            "we'll cover his tuition.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196D")

    label("loc_18A6")

    OP_A2(0x3)

    ChrTalk(    #74
        0xFE,
        (
            "While the academy's on break,\x01",
            "we're having Gerome help with my\x01",
            "son's studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "It's frustrating to ask our neighbors\x01",
            "for help, but if it's for my son's sake,\x01",
            "I'll drink back these tears!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196D")

    Jump("loc_1C62")

    label("loc_1970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_19CE")

    ChrTalk(    #76
        0xFE,
        "My son's quite motivated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "He's even studying on his own at\x01",
            "Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C62")

    label("loc_19CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1A0F")

    ChrTalk(    #78
        0xFE,
        (
            "Oh, my, what's that...?\x01",
            "The streets are so noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C62")

    label("loc_1A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AB1")

    ChrTalk(    #79
        0xFE,
        (
            "I suppose we may have no choice but to\x01",
            "ask Gerome to act as his tutor, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "It's a bit frustrating to ask our neighbors...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B64")

    label("loc_1AB1")

    OP_A2(0x3)

    ChrTalk(    #81
        0xFE,
        (
            "As my son said, he needs to be\x01",
            "ready for the entrance exams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I'm sure Gerome would be\x01",
            "a perfect tutor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Well, it's a bit frustrating\x01",
            "to ask our neighbors, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B64")

    Jump("loc_1C62")

    label("loc_1B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1BFB")

    ChrTalk(    #84
        0xFE,
        (
            "I have to make sure my son Antonio\x01",
            "gets into the royal academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I'd appreciate it if you wouldn't\x01",
            "interrupt his studies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C62")

    label("loc_1BFB")

    OP_A2(0x3)

    ChrTalk(    #86
        0xFE,
        "Really, the election campaigners are so loud...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "How's my son supposed to study like this?\x02",
    )

    CloseMessageWindow()

    label("loc_1C62")

    TalkEnd(0xFE)
    Return()

    # Function_8_153C end

    def Function_9_1C66(): pass

    label("Function_9_1C66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1CDA")

    ChrTalk(    #88
        0xFE,
        "Did somethin' really happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Man, everyone's just gabbin' on.\x01",
            "It's hard for me to trust 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2078")

    label("loc_1CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB1")

    ChrTalk(    #90
        0xFE,
        (
            "The ship I was supposed to get on's\x01",
            "apparently stuck on the open sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Apparently the engine's orbment\x01",
            "ain't workin' at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Ain't nothin' for it, so I'm\x01",
            "stuck on standby at home.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1E37")

    label("loc_1DB1")


    ChrTalk(    #93
        0xFE,
        (
            "The ship I was supposed to get on's\x01",
            "apparently stuck on the open sea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Apparently the engine's orbment\x01",
            "ain't workin' at all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E37")

    Jump("loc_2078")

    label("loc_1E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1EBB")

    ChrTalk(    #95
        0xFE,
        (
            "Apparently my son wants to\x01",
            "be a crewman on an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "Heh heh, he really is the son of a sailor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F66")

    label("loc_1EBB")

    OP_A2(0x2)

    ChrTalk(    #97
        0xFE,
        (
            "Apparently my son wants to\x01",
            "be a crewman on an airship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "It may fly in the sky but it's still a ship,\x01",
            "no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "Heh heh, he really is the son of a sailor.\x02",
    )

    CloseMessageWindow()

    label("loc_1F66")

    Jump("loc_2078")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FC1")

    ChrTalk(    #100
        0xFE,
        (
            "Norman's a good guy, but I just don't\x01",
            "like his campaign promises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2078")

    label("loc_1FC1")

    OP_A2(0x2)

    ChrTalk(    #101
        0xFE,
        (
            "Norman's a good guy, but I just don't\x01",
            "like his campaign promises.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Ruan ain't a city of tourism, it's\x01",
            "a city of sailors and fishers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Don't get that wrong, all right?\x02",
    )

    CloseMessageWindow()

    label("loc_2078")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C66 end

    def Function_10_207C(): pass

    label("Function_10_207C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_20F7")

    ChrTalk(    #104
        0xFE,
        (
            "My brother Gerome won't lose to\x01",
            "some stupid 'in-ci-dent.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "After all, my big brother's super strong.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_20F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_215F")

    ChrTalk(    #106
        0xFE,
        (
            "The break's over, so my\x01",
            "brother Gerome has school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "I wonder if the school's okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_215F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_21CC")

    ChrTalk(    #108
        0xFE,
        "The 'elec-tion' voices are gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "I wonder if all those old men went\x01",
            "back to their homes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_21CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_221D")

    ChrTalk(    #110
        0xFE,
        "I've got Sunday School today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "La, la... I can't wait. ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22B4")

    ChrTalk(    #112
        0xFE,
        (
            "My brother Gerome's school is goin'\x01",
            "on break soon too, I heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Heehee. When he comes home\x01",
            "I'm gonna play with him lots. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2366")

    label("loc_22B4")

    OP_A2(0x1)

    ChrTalk(    #114
        0xFE,
        (
            "Heehee. It's been a while since\x01",
            "Mama was at home all day. ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "My brother Gerome's school is goin'\x01",
            "on break soon too, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "It's nice havin' everyone at home. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_2366")

    TalkEnd(0xFE)
    Return()

    # Function_10_207C end

    def Function_11_236A(): pass

    label("Function_11_236A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_24DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244E")

    ChrTalk(    #117
        0xFE,
        (
            "Apparently something happened at the\x01",
            "academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "I've got to go ask my neighbor\x01",
            "for the details later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Anyway, with information in such scarcity as\x01",
            "it is now, all we can rely on are rumors.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_24DA")

    label("loc_244E")


    ChrTalk(    #120
        0xFE,
        (
            "Is it true that there was some kind of\x01",
            "incident at the academy, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I've got to go ask my neighbor\x01",
            "for the details later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DA")

    Jump("loc_2C1E")

    label("loc_24DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2613")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_259E")

    ChrTalk(    #122
        0xFE,
        (
            "With the orbments not working,\x01",
            "day to day stuff is kinda messed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I hope our new mayor does something\x01",
            "about this soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Can't they at least fix the bridge?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2610")

    label("loc_259E")


    ChrTalk(    #125
        0xFE,
        (
            "With the orbments not working,\x01",
            "day to day stuff is kinda messed up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Can't they at least fix the bridge?\x02",
    )

    CloseMessageWindow()

    label("loc_2610")

    Jump("loc_2C1E")

    label("loc_2613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_274F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_26B8")

    ChrTalk(    #127
        0xFE,
        (
            "My son's going to help tutor\x01",
            "our neighbor's son, Antonio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Apparently Antonio's family is thinking\x01",
            "about sending him to the royal academy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_274C")

    label("loc_26B8")

    OP_A2(0x0)

    ChrTalk(    #129
        0xFE,
        (
            "My son, Gerome, will be tutoring\x01",
            "our neighbor's son, Antonio.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "It's only while he's on break, but I'm\x01",
            "sure they'll get a fair bit done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_274C")

    Jump("loc_2C1E")

    label("loc_274F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_28D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2820")

    ChrTalk(    #131
        0xFE,
        (
            "Whenever I've suddenly got some\x01",
            "free time, I waste it all thinking up\x01",
            "how to spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Strange, isn't it? I can always think\x01",
            "of a million other things I could be\x01",
            "doing while busy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28D2")

    label("loc_2820")

    OP_A2(0x0)

    ChrTalk(    #133
        0xFE,
        (
            "Cleaning and laundry is done, my daughter's\x01",
            "off at Sunday School... Hmm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Phew! It's been a while since I've had\x01",
            "some free time. I'm not sure what to do\x01",
            "with myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D2")

    Jump("loc_2C1E")

    label("loc_28D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2941")

    ChrTalk(    #135
        0xFE,
        "It's getting noisy outside again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I didn't think there was a speech\x01",
            "today, was there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1E")

    label("loc_2941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_29AF")

    ChrTalk(    #137
        0xFE,
        "My daughter Eletta's made a friend recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "It's all thanks to Sunday School.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A40")

    label("loc_29AF")

    OP_A2(0x0)

    ChrTalk(    #139
        0xFE,
        "My daughter Eletta's made a friend recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I'm very happy to hear it. I've been away\x01",
            "a lot lately, so I'm sure she's been lonely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A40")

    Jump("loc_2C1E")

    label("loc_2A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2B1F")

    ChrTalk(    #141
        0xFE,
        (
            "During the election there haven't been\x01",
            "many tourists, so I'm off from my work\x01",
            "as a guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "My husband's busy supporting his\x01",
            "candidate in the election, I believe,\x01",
            "but I'm taking it easy at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C1E")

    label("loc_2B1F")

    OP_A2(0x0)

    ChrTalk(    #143
        0xFE,
        (
            "Me and my husband both work as\x01",
            "tour guides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "During the election there haven't been\x01",
            "many tourists, so I'm off from my work\x01",
            "as a guide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "My husband's busy supporting his\x01",
            "candidate in the election, I believe,\x01",
            "but I'm taking it easy at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C1E")

    TalkEnd(0xFE)
    Return()

    # Function_11_236A end

    def Function_12_2C22(): pass

    label("Function_12_2C22")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2DDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D57")

    ChrTalk(    #146
        0xFE,
        (
            "My son Belden is doing very well\x01",
            "at the mayor's manor it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I hope this will be a chance for him to\x01",
            "start thinking about his future, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "First it's important to not be too\x01",
            "worried about the immediate future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "Right now I've got to compliment him\x01",
            "for working.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2DDA")

    label("loc_2D57")


    ChrTalk(    #150
        0xFE,
        (
            "My son Belden is doing very well\x01",
            "at the mayor's manor it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "This time it's time for us parents\x01",
            "to acknowledge him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDA")

    Jump("loc_3412")

    label("loc_2DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED8")

    ChrTalk(    #152
        0xFE,
        (
            "My husband Norman hasn't come back\x01",
            "from the mayor's manor for days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I can understand he feels the pressure\x01",
            "to get the situation under control as\x01",
            "the new mayor, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        "I wish he wouldn't get so wrapped up in it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2F77")

    label("loc_2ED8")


    ChrTalk(    #155
        0xFE,
        (
            "My husband Norman hasn't come back\x01",
            "from the mayor's manor for days now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "*sigh* Why is it just one thing after\x01",
            "another since my husband became\x01",
            "mayor?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F77")

    Jump("loc_3412")

    label("loc_2F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_30E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3044")

    ChrTalk(    #157
        0xFE,
        (
            "My son Belden has apparently been\x01",
            "off helping at my husband's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "I don't know how long this will go on for,\x01",
            "but I can't do much else except watch\x01",
            "over and encourage him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30DF")

    label("loc_3044")

    OP_A2(0x7)

    ChrTalk(    #159
        0xFE,
        (
            "My son Belden has apparently been\x01",
            "off helping at my husband's office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "He hated it so much before... I wonder\x01",
            "why he suddenly decided to help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DF")

    Jump("loc_3412")

    label("loc_30E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_315F")

    ChrTalk(    #161
        0xFE,
        "I wonder where Belden's gone now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "It seems he didn't go back to the\x01",
            "warehouse, but then where did he go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3412")

    label("loc_315F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3277")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_31EC")

    ChrTalk(    #163
        0xFE,
        (
            "Regardless of the reason, I'm just\x01",
            "glad that boy is back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "It's enough that he'll be at home for a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3274")

    label("loc_31EC")

    OP_A2(0x7)

    ChrTalk(    #165
        0xFE,
        (
            "Regardless of the reason, I'm just\x01",
            "glad that boy is back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "We can think about the future later\x01",
            "and just take our time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3274")

    Jump("loc_3412")

    label("loc_3277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3412")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_3351")

    ChrTalk(    #167
        0xFE,
        (
            "It would be nice if my husband and my son\x01",
            "had a chance to talk to each other, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "He's been so busy with the election\x01",
            "going on now that he can't even take\x01",
            "a few minutes to come back home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3412")

    label("loc_3351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_33AA")

    ChrTalk(    #169
        0xFE,
        (
            "Belden is on the second floor,\x01",
            "so by all means, feel free to go\x01",
            "upstairs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3412")

    label("loc_33AA")


    ChrTalk(    #170
        0xFE,
        "Really! I just can't believe that boy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "How long does he intend to stay\x01",
            "locked up in his room?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3412")

    TalkEnd(0x8)
    Return()

    # Function_12_2C22 end

    def Function_13_3416(): pass

    label("Function_13_3416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_END)), "loc_3755")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_3566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_34BE")

    ChrTalk(    #172
        0xFE,
        (
            "In this case, there's no choice, so I guess\x01",
            "that part-time job's okay, but, maaan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "Working at my dad's office is gonna\x01",
            "be kinda...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3563")

    label("loc_34BE")

    OP_A2(0x6)

    ChrTalk(    #174
        0xFE,
        (
            "I went looking for work in the North Block,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "World's a hard place now, huh. The only\x01",
            "places hirin' are basically part-time jobs\x01",
            "for the election.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3563")

    Jump("loc_374F")

    label("loc_3566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3612")

    ChrTalk(    #176
        0xFE,
        "Guess I've got to search for a place to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "Still, I'm worried about one of my buddies\x01",
            "seeing me, so I'd like to avoid work in\x01",
            "the harbor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CC")

    label("loc_3612")

    OP_A2(0x6)

    ChrTalk(    #178
        0xFE,
        (
            "No point in staying holed up like this,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "It'd be pretty hard to go back to\x01",
            "my friends at the warehouse now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "*siiigh* Guess I've gotta search\x01",
            "for a place to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CC")

    Jump("loc_374F")

    label("loc_36CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_374F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_36E9")

    ChrTalk(    #181
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_374F")

    label("loc_36E9")

    OP_A2(0x6)

    ChrTalk(    #182
        0xFE,
        (
            "No point in running from my dad forever,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I know that better than anyone.\x01",
            "Still...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374F")

    TalkEnd(0x9)
    Jump("loc_3783")

    label("loc_3755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 7)), scpexpr(EXPR_END)), "loc_3763")
    Call(0, 17)
    Jump("loc_3783")

    label("loc_3763")

    TalkBegin(0x9)

    ChrTalk(    #184
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "*siiigh*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_3783")

    Return()

    # Function_13_3416 end

    def Function_14_3784(): pass

    label("Function_14_3784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3795")
    Call(0, 18)

    label("loc_3795")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -4580, 0, 62980, 360)
    SetChrPos(0xF7, -5200, 0, 62110, 360)
    SetChrPos(0x8, 2720, 0, 67920, 167)
    ClearMapFlags(0x1)
    OP_6D(-5070, 0, 64220, 0)
    OP_67(0, 8900, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #186
        0x101,
        "#1015F#2PUm... Is THIS that Belden dude's home?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38B1")

    ChrTalk(    #187
        0x106,
        (
            "#051F'Just to the right of the mayor's mansion'...\x01",
            "Looks like the place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3914")

    label("loc_38B1")


    ChrTalk(    #188
        0x103,
        (
            "#020FWell, the directions were just 'to the right\x01",
            "of the mayor's mansion.' This should be it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3914")


    def lambda_391A():
        OP_6D(210, 0, 64230, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_391A)

    def lambda_3932():
        OP_67(0, 8900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3932)
    Sleep(1000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xBB8, 0x0, 0xFEB0, 0x7D0, 0x0)
    ClearChrFlags(0x8, 0x4)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 256, 500)

    ChrTalk(    #189
        0x8,
        "Oh, welcome.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0xF7, 0x8, 500)

    def lambda_39BF():
        OP_8E(0xFE, 0xFFFFFF1A, 0x0, 0xF94C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_39BF)
    Sleep(300)

    def lambda_39DF():
        OP_6D(-1590, 0, 64160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39DF)

    def lambda_39F7():
        OP_67(0, 8900, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_39F7)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(300)
    OP_43(0xF7, 0x1, 0x0, 0x10)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #190
        0x8,
        (
            "#2PI'm sorry, but my husband isn't home\x01",
            "at the moment. He's busy at the hotel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x8,
        "#2PI would ask that you go see him there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1004F#3PHuh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3B48")

    ChrTalk(    #193
        0x106,
        (
            "#053FAh, we're not actually here to\x01",
            "see your husband, ma'am.\x02\x03",

            "#050FWe were hoping we could speak\x01",
            "with Belden.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BC7")

    label("loc_3B48")


    ChrTalk(    #194
        0x103,
        (
            "#026FOur apologies, but our business\x01",
            "isn't with your husband, ma'am.\x02\x03",

            "#020FWe were hoping to speak with\x01",
            "Belden, actually.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BC7")


    ChrTalk(    #195
        0x8,
        "#2POh, goodness, you're here for Belden?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x8,
        (
            "#2PI'm sorry, I thought you were\x01",
            "here on election business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        (
            "#1015F#3PElection...?\x02\x03",

            "#1004FEr, wait, ma'am, is your husband--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#2PYes, my husband is Norman,\x01",
            "one of the mayoral candidates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        (
            "#2PHe's using the top floor of the hotel as\x01",
            "his election headquarters, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "#2PHis supporters are doing...whatever it is\x01",
            "people working for an election do up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        (
            "#1011F#3POkay, I see.\x02\x03",

            "Oh, uh, we're from the Bracer\x01",
            "Guild, actually.\x02\x03",

            "We kinda wanted to ask your son\x01",
            "some questions, if that's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x8,
        "#2PThe Bracer Guild?\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #203
        0x8,
        (
            "#2POh, no, has Belden done\x01",
            "something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F1C")

    ChrTalk(    #204
        0x106,
        (
            "#050FNo, ma'am, nothing like that.\x02\x03",

            "We believe he may have witnessed\x01",
            "something strange, though.\x02\x03",

            "We'd like to ask him some\x01",
            "questions, if you'll let us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBC")

    label("loc_3F1C")


    ChrTalk(    #205
        0x103,
        (
            "#020FNo, you needn't worry about that.\x02\x03",

            "We've heard he witnessed something\x01",
            "strange, however.\x02\x03",

            "We'd like to ask him about what\x01",
            "he saw, if you'll permit it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBC")


    ChrTalk(    #206
        0x8,
        "#2PSomething...strange?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#3PUh, he didn't tell YOU about\x01",
            "what he saw, ma'am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        "#2PI'm afraid not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "#2PI'm happy to have him home for the\x01",
            "first time in ages, but he's barely\x01",
            "spoken to me since he got back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x8,
        (
            "#2PAnd my husband's time is so\x01",
            "dominated by the election that he\x01",
            "won't even talk to his son...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#1025F#3PI see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_41A6")

    ChrTalk(    #212
        0x106,
        (
            "#050FHmm... Do you mind if we talk\x01",
            "to Belden, ma'am?\x02\x03",

            "If he's got some problems, we can\x01",
            "at least let him talk about 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_424D")

    label("loc_41A6")


    ChrTalk(    #213
        0x103,
        (
            "#020FIn that case, I think it may be a very\x01",
            "good idea for us to speak to him.\x02\x03",

            "If something is on his mind, having\x01",
            "a sympathetic ear available could\x01",
            "really help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_424D")


    ChrTalk(    #214
        0x8,
        (
            "#2PThat sounds like a great idea.\x01",
            "Please, go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        "#2PBelden's room is on the second floor.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x120F)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_14_3784 end

    def Function_15_42BE(): pass

    label("Function_15_42BE")

    OP_8E(0x101, 0xFFFFEEA8, 0x0, 0xFF00, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFFF7C2, 0x0, 0xFF96, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFFF88A, 0x0, 0xF7EE, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 500)
    Return()

    # Function_15_42BE end

    def Function_16_4302(): pass

    label("Function_16_4302")

    OP_8E(0xF7, 0xFFFFEEA8, 0x0, 0xFF00, 0xBB8, 0x0)
    OP_8E(0xF7, 0xFFFFF7C2, 0x0, 0xFF96, 0xBB8, 0x0)
    OP_8E(0xF7, 0xFFFFF916, 0x0, 0xFB22, 0xBB8, 0x0)
    TurnDirection(0xF7, 0x8, 500)
    Return()

    # Function_16_4302 end

    def Function_17_4346(): pass

    label("Function_17_4346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4357")
    Call(0, 18)

    label("loc_4357")

    FadeToBright(0, 0)
    EventBegin(0x0)
    OP_4A(0x9, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4446")
    Fade(1000)
    SetChrPos(0x101, -29130, 0, 62760, 135)
    SetChrPos(0x106, -27990, 0, 62950, 180)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_0D()

    NpcTalk(    #216
        0x9,
        "Young Man",
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #217
        0x9,
        "Young Man",
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        (
            "#1015FUh, 'scuse me!\x01",
            "Could we talk to you for a sec?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_451C")

    label("loc_4446")

    Fade(1000)
    SetChrPos(0x101, -27990, 0, 62950, 180)
    SetChrPos(0x103, -29130, 0, 62760, 135)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x103, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_0D()

    NpcTalk(    #219
        0x9,
        "Young Man",
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x9,
        "Young Man",
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1015FUh, 'scuse me!\x01",
            "Could we talk to you for a sec?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_451C")


    NpcTalk(    #222
        0x9,
        "Young Man",
        "What the hell am I doing...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #223
        0x9,
        "Young Man",
        (
            "Came runnin' back home just\x01",
            "'cause Dad ain't here...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #224
        0x9,
        "Young Man",
        "I'm pathetic...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54E6")

    ChrTalk(    #225
        0x106,
        (
            "#551FHey.\x02\x03",

            "Look at people when they're\x01",
            "talkin' to you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #226
        0x9,
        "Young Man",
        "Eh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_463C():
        OP_91(0x9, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_463C)
    WaitChrThread(0x9, 0x1)

    NpcTalk(    #227
        0x9,
        "Young Man",
        "#1PUWAAAAAAH!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #228
        0x9,
        "Young Man",
        "#1PWh-Who're YOU guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x106,
        (
            "#050FCome on, Belden. Don't tell me\x01",
            "you don't know me by reputation,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x9,
        "#1PWha...\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #231
        0x9,
        "#1PA-A-AGATE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x9,
        "#1PWh-What're you doin' in my HOUSE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x106,
        (
            "#051FHave some questions for ya,\x01",
            "and your old lady let us in.\x02\x03",

            "Got some time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x9,
        "#1PU-Umm, I...guess...\x02",
    )

    CloseMessageWindow()

    def lambda_47DF():
        OP_91(0x9, 0x0, 0x0, 0x15E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_47DF)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #235
        0x9,
        "#1PWhat did you want to ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#1011FWell, we heard you saw a 'white\x01",
            "shadow' recently.\x02\x03",

            "We were wondering if you'd\x01",
            "mind telling us about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x9,
        "#1POh, that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x9,
        (
            "#1PI'd...rather not talk about it,\x01",
            "to be honest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x9,
        (
            "#1PAny time I remember too much about\x01",
            "it, I just get scared all over again...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #240
        0x106,
        (
            "#057FThe heck is THIS? You're a Raven!\x01",
            "Man up! Talk already!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #241
        0x9,
        "#1PAh! I'll talk, I'll talk!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #242
        0x101,
        (
            "#1019FAgate, stop scaring the poor kid.\x01",
            "He doesn't need to wet himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x106,
        (
            "#053FHey, he's talking, right?\x02\x03",

            "#050FC'mon, details, make with 'em.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #244
        0x9,
        "#1POkay, okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "#1PI was living in the warehouse\x01",
            "where the crew hangs out until\x01",
            "about a week ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "#1PI usually only come back here\x01",
            "for food, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "#1PI slept over there, you know,\x01",
            "so I could chill with my bros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1007FYyyyou've got to be kidding.\x02\x03",

            "How in the name of the Goddess\x01",
            "could you not want to live in a big\x01",
            "comfy house like this...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #249
        0x101,
        (
            "#1006FAlthough...didn't you use to live\x01",
            "like that too, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#552F...Don't change the subject.\x02\x03",

            "#050FSo, you were with the crew.\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #251
        0x9,
        "#1PLike I said, it was a week ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x9,
        (
            "#1PThe crew was all boozed up and asleep,\x01",
            "but I woke up for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x9,
        (
            "#1PThought I'd go outside, feel the night\x01",
            "air, y'know...and then I saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1020FYou mean...the white shadow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x9,
        (
            "#1PYeah...a white shadow floating\x01",
            "up in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x9,
        (
            "#1PIt was in some kinda old-fashioned\x01",
            "getup, cape and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x9,
        "#1PAnd it was...dancing in the air.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #258
        0x101,
        "#1016FAhaha, that's...rather specific.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x106,
        (
            "#050FSure you weren't just drunk,\x01",
            "tired, and seein' things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x9,
        "#1PNah, no way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x9,
        (
            "#1PThis scared me right out of bein'\x01",
            "drunk, and I tried to scream but\x01",
            "couldn't even do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "#1PAfter the thing flew off to the northeast,\x01",
            "I ran into the warehouse, yelling, and\x01",
            "woke everyone up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "#1PThat just got me a punch from\x01",
            "Rocco, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x106,
        (
            "#053FHmph... Okay, I see.\x02\x03",

            "#050FSo WHEN did this happen?\x01",
            "Do you remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x9,
        "#1PI guess...around two in the morning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x9,
        "#1PAaaargh, now I remember the whole thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x9,
        "#1PI came home to try and FORGET all that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#1007FNow I get why you ran home...\x02\x03",

            "#1019FYou just didn't want to sleep in some place\x01",
            "where you'd seen something scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x106,
        (
            "#552FPff. You're a failure of a punk,\x01",
            "you know that?\x02\x03",

            "You'd be better off just quitting\x01",
            "the Ravens and staying home.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #270
        0x9,
        (
            "#1PAww... Yeah, I know I'm not\x01",
            "cut out for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x9,
        "#1PBut, well, I just can't face my dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x9,
        (
            "#1PHe's busy with the election and not home\x01",
            "much, and that's why I came back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x9,
        (
            "#1POnce the election is over, I'll have\x01",
            "to face him, one way or another...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x9,
        (
            "#1PAnd if he manages to win, my\x01",
            "life'll get even MORE restrictive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        (
            "#1015FSo, basically...you're just running away\x01",
            "from something you don't like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x9,
        "#1PWellllll...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x106,
        (
            "#050FYeah, and you damn well know it, too.\x02\x03",

            "#053FThe answer, genius, is to find your OWN\x01",
            "answer, and stop relying on other people.\x02\x03",

            "I'll tell your old lady the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x9,
        "#1PA-Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x106,
        "#053FWe're done here.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)
    Sleep(500)

    ChrTalk(    #280
        0x106,
        "#051FEstelle, let's go.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 82, 400)

    ChrTalk(    #281
        0x101,
        "#1006FRight.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #282
        0x101,
        "#1001FBelden, thanks for talking to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x9,
        "#1PYeah...\x02",
    )

    CloseMessageWindow()
    Jump("loc_667E")

    label("loc_54E6")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #284
        0x101,
        (
            "#1019FOh, for crying out...\x02\x03",

            "Hel-loooo? Look at people when\x01",
            "they're TRYING to talk to you!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #285
        0x9,
        "Young Man",
        "Eh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_55B0():
        OP_91(0x9, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55B0)
    WaitChrThread(0x9, 0x1)

    NpcTalk(    #286
        0x9,
        "Young Man",
        "#1PUWAAAAAAH!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #287
        0x9,
        "Young Man",
        "#1PWh-Who're YOU guys?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#1011FAnd he finally notices us!\x02\x03",

            "So I guess you're Belden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x9,
        "#1PYeah... That's right.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #290
        0x9,
        (
            "#1PWait, you--you're that bracer from\x01",
            "the tournament, ain't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1006FYep! I'm Estelle Bright.\x02\x03",

            "This is my superior, Scherazard Harvey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x103,
        "#021FA pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x9,
        "#1PUh, r-right...\x02",
    )

    CloseMessageWindow()

    def lambda_574A():
        OP_91(0x9, 0x0, 0x0, 0x15E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_574A)
    WaitChrThread(0x9, 0x1)
    Sleep(500)

    ChrTalk(    #294
        0x9,
        "#1PSo what do you guys need?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1011FWell, we heard you saw a 'white\x01",
            "shadow' recently.\x02\x03",

            "We were wondering if you'd mind\x01",
            "telling us about it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #296
        0x9,
        "#1POh, that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x9,
        (
            "#1PI'd...rather not talk about it,\x01",
            "to be honest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x9,
        (
            "#1PAny time I remember too much about\x01",
            "it, I just get scared all over again...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #299
        0x101,
        (
            "#1020FNnngah...\x02\x03",

            "Was it...really that scary...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x103,
        (
            "#021FNow, now. Don't say that.\x02\x03",

            "How about you tell me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x103, 400)
    Sleep(500)

    ChrTalk(    #301
        0x9,
        "#1PUh, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x103,
        (
            "#027FIf you tell me I might do...\x01",
            "something nice for you. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #303
        0x9,
        "#1PWhoa...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #304
        0x101,
        (
            "#1019FSchera. I've told you before that\x01",
            "sex appeal is not a guild-approved\x01",
            "weapon.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 82, 400)

    ChrTalk(    #305
        0x103,
        "#021FYes, yes.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x9, 400)

    ChrTalk(    #306
        0x103,
        (
            "#027FNow, then...really.\x01",
            "Do you feel like talking?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #307
        0x9,
        "#1PWell, I guess it couldn't hurt...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x9,
        (
            "#1PI was living in the warehouse\x01",
            "where the crew hangs out until\x01",
            "about a week ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x9,
        (
            "#1PI usually only come back here\x01",
            "for food, see?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x9,
        (
            "#1PI slept over there, you know,\x01",
            "so I could chill with my bros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        (
            "#1007FYou've gotta be kidding.\x02\x03",

            "How in the name of the Goddess\x01",
            "could you not want to live in a big\x01",
            "comfy house like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x103,
        (
            "#021FHe's just young, is all.\x02\x03",

            "#027FPlease, continue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        "#1PLike I said, it was a week ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x9,
        (
            "#1PThe crew was all boozed up and asleep,\x01",
            "but I woke up for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x9,
        (
            "#1PThought I'd go outside, feel the night air,\x01",
            "y'know...and then I saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        "#1020FYou mean...the white shadow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x9,
        (
            "#1PYeah...a white shadow\x01",
            "floating up in the air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x9,
        (
            "#1PIt was in some kinda old-fashioned\x01",
            "getup, cape and all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x9,
        "#1PAnd it was...dancing in the air.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #320
        0x101,
        "#1016FAhhaha, that's...rather specific.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x103,
        (
            "#020FYou're certain the alcohol and exhaustion\x01",
            "weren't clouding your senses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x9,
        "#1PNah, no way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x9,
        (
            "#1PThis scared me right out of bein'\x01",
            "drunk, and I tried to scream but\x01",
            "couldn't even do that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x9,
        (
            "#1PAfter the thing flew off to the northeast,\x01",
            "I ran into the warehouse, yelling, and\x01",
            "woke everyone up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x9,
        (
            "#1PThat just got me a punch from\x01",
            "Rocco, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x103,
        (
            "#026FI'd...imagine, yes.\x02\x03",

            "#020FDo you remember exactly when\x01",
            "during the night this happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x9,
        (
            "#1PI guess...around two in\x01",
            "the morning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x9,
        (
            "#1PAaaargh, now I remember\x01",
            "the whole thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x9,
        (
            "#1PI came home to try and\x01",
            "FORGET all that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        (
            "#1007FNow I get why you ran home...\x02\x03",

            "#1019FYou just didn't want to sleep in some place\x01",
            "where you'd seen something scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x103,
        (
            "#027FSo you learned how nice it is to\x01",
            "have a home to come back to, yes?\x02\x03",

            "Call me crazy, but this might be a good\x01",
            "opportunity to leave the Ravens behind.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #332
        0x9,
        (
            "#1PAww... Yeah, I know I'm not\x01",
            "cut out for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x9,
        "#1PBut, well, I just can't face my dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0x9,
        (
            "#1PHe's busy with the election and not home\x01",
            "much, and that's why I came back, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x9,
        (
            "#1POnce the election is over, I'll have\x01",
            "to face him, one way or another...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x9,
        (
            "#1PAnd if he manages to win, my\x01",
            "life'll get even MORE restrictive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        (
            "#1015FSo, basically...you're just running\x01",
            "away from what you don't like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x9,
        "#1PWellllll...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x103,
        "#021FNow, now. Cheer up.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x103, 0x40)
    OP_8F(0x103, 0xFFFF90FC, 0x0, 0xF0FA, 0x3E8, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #340
        "\x07\x05Schera placed a quick peck on Belden's cheek.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #341
        0x9,
        "#1PWhoooa!\x02",
    )

    OP_96(0x9, 0xFFFF9304, 0x0, 0xEEB6, 0x1F4, 0x1388)
    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x103, 0xFFFF8F30, 0x0, 0xF42E, 0x4B0, 0x0)
    ClearChrFlags(0x103, 0x40)
    TurnDirection(0x9, 0x103, 800)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(    #342
        0x101,
        "#1013FEr, Schera?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x103,
        (
            "#021FHeehee!\x01",
            "Just a little something to perk you up,\x01",
            "and say thanks for the info.\x02\x03",

            "#027FNow it's up to you to think for yourself,\x01",
            "and find your own answer to this problem.\x02\x03",

            "Remember: you're the only one who can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x9,
        "#1PM-Miss...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x103,
        "#026FWell...this is certainly a start.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 82, 400)
    Sleep(500)

    ChrTalk(    #346
        0x103,
        "#020FEstelle, let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        "#1007FRight, right... Really...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #348
        0x101,
        "#1008FBelden, thanks for talking to us.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #349
        0x9,
        "#1PYeah, you're welcome!\x02",
    )

    CloseMessageWindow()

    label("loc_667E")

    OP_A2(0x1210)
    OP_28(0x82, 0x2, 0x20)
    OP_28(0x82, 0x1, 0x40)
    OP_4B(0x9, 255)
    ClearChrFlags(0x9, 0x10)
    EventEnd(0x0)
    Return()

    # Function_17_4346 end

    def Function_18_6699(): pass

    label("Function_18_6699")

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
        (0, "loc_6712"),
        (1, "loc_6718"),
        (SWITCH_DEFAULT, "loc_671E"),
    )


    label("loc_6712")

    OP_A2(0x1200)
    Jump("loc_671E")

    label("loc_6718")

    OP_A2(0x1201)
    Jump("loc_671E")

    label("loc_671E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_672C")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_6730")

    label("loc_672C")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_6730")

    Return()

    # Function_18_6699 end

    SaveToFile()

Try(main)
