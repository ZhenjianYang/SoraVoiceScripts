from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2320   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2320.x',
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
        'Creda',                                # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 500,
        Y                   = 8800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -4040,
        TriggerZ            = 500,
        TriggerY            = 7530,
        TriggerRange        = 400,
        ActorX              = -4000,
        ActorZ              = 2000,
        ActorY              = 8800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_170",          # 02, 2
        "Function_3_186",          # 03, 3
        "Function_4_18B",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_100")
    Jump("loc_14D")

    label("loc_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_10A")
    Jump("loc_14D")

    label("loc_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_114")
    Jump("loc_14D")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_11E")
    Jump("loc_14D")

    label("loc_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_128")
    Jump("loc_14D")

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_132")
    Jump("loc_14D")

    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13C")
    Jump("loc_14D")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_146")
    Jump("loc_14D")

    label("loc_146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14D")

    label("loc_14D")

    Return()

    # Function_0_F6 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166")
    OP_B1("t2320_y")
    Jump("loc_16F")

    label("loc_166")

    OP_B1("t2320_n")

    label("loc_16F")

    Return()

    # Function_1_14E end

    def Function_2_170(): pass

    label("Function_2_170")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_185")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_170")

    label("loc_185")

    Return()

    # Function_2_170 end

    def Function_3_186(): pass

    label("Function_3_186")

    Call(0, 4)
    Return()

    # Function_3_186 end

    def Function_4_18B(): pass

    label("Function_4_18B")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB")
    OP_0D()
    OP_A9(0x28)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC")
    TalkEnd(0x8)
    Return()

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_27E")

    ChrTalk(    #0
        0x8,
        (
            "My back's been feeling better,\x01",
            "ever since the children came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Maybe some of their energy\x01",
            "is rubbing off on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_3CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339")
    OP_A2(0x0)

    ChrTalk(    #2
        0x8,
        (
            "The suspect is at the\x01",
            "Windmill Lodge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "He should be made to personally\x01",
            "apologize to the children before\x01",
            "he's handed over to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "Don't you agree?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C9")

    label("loc_339")


    ChrTalk(    #5
        0x8,
        (
            "The suspect is at the\x01",
            "Windmill Lodge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "He should be made to personally\x01",
            "apologize to the children before\x01",
            "he's handed over to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C9")

    Jump("loc_B2A")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_4C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    OP_A2(0x0)

    ChrTalk(    #7
        0x8,
        (
            "The children don't even have\x01",
            "families, and to do this to\x01",
            "them is just horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "How can Aidios allow such\x01",
            "things to happen...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_46A")


    ChrTalk(    #9
        0x8,
        (
            "The children don't even have\x01",
            "families, and to do this to\x01",
            "them is just horrible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF")

    Jump("loc_B2A")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_597")
    OP_A2(0x0)

    ChrTalk(    #10
        0x8,
        (
            "It's so good of you to come play\x01",
            "with the kids at the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "It's as if they've suddenly become\x01",
            "everyone's grandchildren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I tend to prefer the quiet,\x01",
            "but I don't mind that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61F")

    label("loc_597")


    ChrTalk(    #13
        0x8,
        (
            "It's so good of you to come play\x01",
            "with the kids at the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "It's as if they've suddenly become\x01",
            "everyone's grandchildren.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61F")

    Jump("loc_B2A")

    label("loc_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #15
        0x8,
        (
            "It must have taken a truly\x01",
            "heartless individual to set\x01",
            "fire to an orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "It's just not the kind of thing any\x01",
            "human should be capable of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "Whoever did it must be brought\x01",
            "to justice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_6F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_741")

    ChrTalk(    #18
        0x8,
        "The village certainly seems busy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_84A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EC")
    OP_A2(0x0)

    ChrTalk(    #20
        0x8,
        (
            "Aren't the flowers overlooking\x01",
            "the village beautiful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "It's very convenient, having a city\x01",
            "like Ruan so close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "I quite like it here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_847")

    label("loc_7EC")


    ChrTalk(    #23
        0x8,
        (
            "It's very convenient, having a city\x01",
            "like Ruan so close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "I quite like it here.\x02",
    )

    CloseMessageWindow()

    label("loc_847")

    Jump("loc_B2A")

    label("loc_84A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_9AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_941")
    OP_A2(0x0)

    ChrTalk(    #25
        0x8,
        (
            "Some people say the airships are the\x01",
            "reason no one comes here anymore, and\x01",
            "why all the young people leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "I, for one, enjoy the peace\x01",
            "and quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I just want a nice, quiet place\x01",
            "where I can grow old gracefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AB")

    label("loc_941")


    ChrTalk(    #28
        0x8,
        (
            "Some people are sad that this\x01",
            "place is getting lonelier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "I, for one, enjoy the peace\x01",
            "and quiet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AB")

    Jump("loc_B2A")

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_A1E")

    ChrTalk(    #30
        0x8,
        "A boy in a cap, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "He hasn't come into the store.\x01",
            "Perhaps Sadie's seen him\x01",
            "pass by?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD6")
    OP_A2(0x0)

    ChrTalk(    #32
        0x8,
        (
            "My granddaughter, Sadie, really\x01",
            "is the sweetest girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "Her parents left to find work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "But Sadie stays here to be\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "I'm truly grateful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B2A")

    label("loc_AD6")


    ChrTalk(    #36
        0x8,
        (
            "My granddaughter, Sadie, really\x01",
            "is the sweetest girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        "I'm truly grateful.\x02",
    )

    CloseMessageWindow()

    label("loc_B2A")

    TalkEnd(0x8)
    Return()

    # Function_4_18B end

    SaveToFile()

Try(main)
