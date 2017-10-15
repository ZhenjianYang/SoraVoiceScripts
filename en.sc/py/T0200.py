from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0200   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0200.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0200_1 ._SN',
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
        'Mayor Klaus',                          # 9
        'Private Clay',                         # 10
        'Crow',                                 # 11
        'Kitty',                                # 12
        'Rolent',                               # 13
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
        'ED6_DT07/CH02350 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT27/CH03870 ._CH',             # 02
        'ED6_DT27/CH03871 ._CH',             # 03
        'ED6_DT27/CH03005 ._CH',             # 04
        'ED6_DT07/CH01770 ._CH',             # 05
        'ED6_DT26/CH20311 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02350P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT27/CH03870P._CP',             # 02
        'ED6_DT27/CH03871P._CP',             # 03
        'ED6_DT27/CH03005P._CP',             # 04
        'ED6_DT07/CH01770P._CP',             # 05
        'ED6_DT26/CH20311P._CP',             # 06
    )

    DeclNpc(
        X                   = 8700,
        Z                   = 3650,
        Y                   = 2510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 7070,
        Z                   = 450,
        Y                   = 1530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 7640,
        Z                   = 0,
        Y                   = 11140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4940,
        Z                   = 0,
        Y                   = 6680,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -20690,
        Z                   = 0,
        Y                   = -180,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 8130,
        TriggerZ            = 0,
        TriggerY            = -13900,
        TriggerRange        = 1000,
        ActorX              = 8130,
        ActorZ              = 2100,
        ActorY              = -13700,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1FB",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_299",          # 03, 3
        "Function_4_4A6",          # 04, 4
        "Function_5_863",          # 05, 5
        "Function_6_A16",          # 06, 6
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE")
    ClearChrFlags(0xB, 0x80)

    label("loc_1BE")

    Jump("loc_1D2")

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D2")
    ClearChrFlags(0x8, 0x80)

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E3")
    ClearChrFlags(0x9, 0x80)

    label("loc_1E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1FA")
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x3)

    label("loc_1FA")

    Return()

    # Function_0_1A6 end

    def Function_1_1FB(): pass

    label("Function_1_1FB")

    OP_16(0x2, 0xFA0, 0xFFFE36F8, 0xFFFE0C00, 0x230002)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_238")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_24D")

    label("loc_238")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_24D")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_271")
    OP_65(0x0, 0x1)

    label("loc_271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_282")
    SoundLoad(347)
    SoundLoad(140)

    label("loc_282")

    Return()

    # Function_1_1FB end

    def Function_2_283(): pass

    label("Function_2_283")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_283")

    label("loc_298")

    Return()

    # Function_2_283 end

    def Function_3_299(): pass

    label("Function_3_299")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 5590, 13090, 9980, 9010, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46E")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_354")

    def lambda_338():

        label("loc_338")

        OP_97(0xFE, 0x28D2, 0x4272, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_338")

    QueueWorkItem2(0xFE, 1, lambda_338)
    Jump("loc_373")

    label("loc_354")


    def lambda_35A():

        label("loc_35A")

        OP_97(0xFE, 0x28D2, 0x4272, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_35A")

    QueueWorkItem2(0xFE, 1, lambda_35A)

    label("loc_373")

    SetChrChipByIndex(0xFE, 2)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    OP_22(0x15B, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C4")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BC")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_3C4")

    label("loc_3BC")

    Sleep(15)
    Jump("loc_38C")

    label("loc_3C4")

    OP_44(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 7640, 0, 11140, 270)

    label("loc_3E3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46B")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4650), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_463")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 3)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 5590, 13090, 9980, 9010, 0)
    Jump("loc_46B")

    label("loc_463")

    Sleep(500)
    Jump("loc_3E3")

    label("loc_46B")

    Jump("loc_4A2")

    label("loc_46E")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")

    def lambda_48A():
        OP_8D(0xFE, 5590, 13090, 9980, 9010, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_48A)

    label("loc_4A2")

    Jump("loc_2CD")

    label("loc_4A5")

    Return()

    # Function_3_299 end

    def Function_4_4A6(): pass

    label("Function_4_4A6")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_6A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_569")

    ChrTalk(    #0
        0x8,
        (
            "#602FOur Estelle knows these roads\x01",
            "like her own backyard.\x02\x03",

            "Well, then, I ask that you do\x01",
            "be very careful.\x02\x03",

            "With the fog as thick as it is,\x01",
            "it's almost impossible to see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A1")

    label("loc_569")


    ChrTalk(    #1
        0x8,
        (
            "#602FThe fog has gotten even thicker than\x01",
            "last night, that much is certain.\x02\x03",

            "Estelle, I've heard your group will help\x01",
            "evacuate those in the countryside.\x02\x03",

            "The city will be patrolled by army\x01",
            "forces very soon, but the more remote\x01",
            "locations will be defenseless.\x02\x03",

            "Please, get them quickly to a safe\x01",
            "location.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6A1")

    Jump("loc_85F")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_85F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_739")

    ChrTalk(    #2
        0x8,
        (
            "#602FThe fog has gotten even thicker than\x01",
            "last night, that much is certain.\x02\x03",

            "If you go out onto the roads,\x01",
            "do be very careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85F")

    label("loc_739")


    ChrTalk(    #3
        0x8,
        (
            "#602FOh, hello, everyone. It's so early\x01",
            "in morning and yet you're already\x01",
            "hard at work.\x02\x03",

            "Hmm... The fog has gotten even\x01",
            "thicker than last night, that much\x01",
            "is certain.\x02\x03",

            "If you go out onto the roads for work,\x01",
            "be very careful.\x02\x03",

            "With the mist as thick as it is,\x01",
            "it's almost impossible to see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_85F")

    TalkEnd(0x8)
    Return()

    # Function_4_4A6 end

    def Function_5_863(): pass

    label("Function_5_863")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_990")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8E8")

    ChrTalk(    #4
        0xFE,
        (
            "Mr. Ashton is a great soldier,\x01",
            "but his unit isn't very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "*sigh* I can almost feel his\x01",
            "suffering...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98D")

    label("loc_8E8")


    ChrTalk(    #6
        0xFE,
        (
            "Mr. Ashton is a great soldier,\x01",
            "but his unit isn't very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "...Man, none of them have\x01",
            "any sense at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "*sigh* I can almost feel his\x01",
            "suffering...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_98D")

    Jump("loc_A12")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_END)), "loc_A12")

    ChrTalk(    #9
        0xFE,
        (
            "Mr. Ashton's a pretty capable\x01",
            "guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I've been told that he was in a force\x01",
            "in the capital, but that's no surprise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A12")

    TalkEnd(0x9)
    Return()

    # Function_5_863 end

    def Function_6_A16(): pass

    label("Function_6_A16")

    TalkBegin(0xB)

    ChrTalk(    #11
        0xFE,
        (
            "I just came to deliver some goods\x01",
            "to the Mayor's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "My delivery? Oh, I delivered it ages\x01",
            "ago! But his garden is so lovely,\x01",
            "I can't help but admire it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I know I should get back to the shop,\x01",
            "but I can't help but stay a while.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_A16 end

    SaveToFile()

Try(main)
